"""Cross-model analysis: descriptive statistics, pairwise comparisons, and effect sizes.

Loads multiple eval runs and computes:
  1. Descriptive statistics per model (mean, SD, bootstrap 95% CI)
  2. Overall effect size (one-way ANOVA: F, eta-squared, Cohen's f)
  3. Pairwise comparisons (bootstrap CI on difference, Cohen's d)
  4. Sensitivity analysis (minimum detectable effect size)

Usage:
    uv run python scripts/compute_cross_model.py \
        --labels model1,model2,... \
        file1.eval.json file2.eval.json ...
"""

import argparse
import json
import sys
from itertools import combinations
from math import log

import numpy as np
import pandas as pd
from scipy import stats


DIMENSIONS = ["believability", "consistency", "sustained_turns"]


def score_geometric(believability, consistency, turns, max_turns=5):
    b = max((believability - 1) / 4, 0.01)
    c = max((consistency - 1) / 4, 0.01)
    t = max(min(log(1 + turns) / log(1 + max_turns), 1.0), 0.01)
    return (b * c * t) ** (1 / 3) * 100


def load_eval(path: str, label: str) -> pd.DataFrame:
    """Load an eval JSON dump and return a DataFrame of scores."""
    with open(path) as f:
        data = json.load(f)

    rows = []
    for s in data["samples"]:
        scorer_key = list(s["scores"].keys())[0]
        sv = s["scores"][scorer_key]["value"]

        believability = sv.get("believability", 0)
        consistency = sv.get("consistency", 0)
        sustained_turns = sv.get("sustained_turns", 0)

        composite = sv.get("composite")
        if composite is None:
            composite = score_geometric(believability, consistency, sustained_turns)

        rows.append({
            "model": label,
            "sample_id": s["id"],
            "believability": believability,
            "consistency": consistency,
            "sustained_turns": sustained_turns,
            "composite": composite,
        })

    return pd.DataFrame(rows)


def bootstrap_ci_single(values, n_boot=10000, ci=0.95):
    """Bootstrap CI for a single group's mean."""
    rng = np.random.default_rng(42)
    n = len(values)
    boot_means = np.array([values[rng.integers(0, n, size=n)].mean() for _ in range(n_boot)])
    alpha = (1 - ci) / 2
    return np.percentile(boot_means, alpha * 100), np.percentile(boot_means, (1 - alpha) * 100)


def bootstrap_ci_diff(values_a, values_b, n_boot=10000, ci=0.95):
    """Bootstrap CI for the difference in means between two groups."""
    rng = np.random.default_rng(42)
    na, nb = len(values_a), len(values_b)
    boot_diffs = np.empty(n_boot)
    for i in range(n_boot):
        ma = values_a[rng.integers(0, na, size=na)].mean()
        mb = values_b[rng.integers(0, nb, size=nb)].mean()
        boot_diffs[i] = ma - mb
    alpha = (1 - ci) / 2
    lo = np.percentile(boot_diffs, alpha * 100)
    hi = np.percentile(boot_diffs, (1 - alpha) * 100)
    return lo, hi


def cohens_d(values_a, values_b):
    """Cohen's d with pooled standard deviation."""
    na, nb = len(values_a), len(values_b)
    pooled_sd = np.sqrt(
        ((na - 1) * values_a.std(ddof=1) ** 2 + (nb - 1) * values_b.std(ddof=1) ** 2)
        / (na + nb - 2)
    )
    if pooled_sd == 0:
        return 0.0
    return (values_a.mean() - values_b.mean()) / pooled_sd


def anova_effect_sizes(df, measure):
    """One-way ANOVA with eta-squared and Cohen's f."""
    groups = [g[measure].values for _, g in df.groupby("model")]

    f_stat, p_value = stats.f_oneway(*groups)

    grand_mean = df[measure].mean()
    ss_between = sum(len(g) * (g.mean() - grand_mean) ** 2 for g in groups)
    ss_within = sum(((g - g.mean()) ** 2).sum() for g in groups)
    ss_total = ss_between + ss_within

    eta_sq = ss_between / ss_total if ss_total > 0 else 0
    cohens_f = np.sqrt(eta_sq / (1 - eta_sq)) if eta_sq < 1 else float("inf")

    df_between = len(groups) - 1
    df_within = len(df) - len(groups)

    return {
        "f_stat": f_stat,
        "p_value": p_value,
        "df_between": df_between,
        "df_within": df_within,
        "eta_squared": eta_sq,
        "cohens_f": cohens_f,
    }


def main():
    parser = argparse.ArgumentParser(description="Cross-model eval analysis")
    parser.add_argument("files", nargs="+", help="Eval JSON dump files")
    parser.add_argument("--labels", required=True, help="Comma-separated model labels")
    args = parser.parse_args()

    labels = args.labels.split(",")
    if len(labels) != len(args.files):
        print(f"Error: {len(labels)} labels but {len(args.files)} files")
        sys.exit(1)

    frames = []
    for path, label in zip(args.files, labels):
        frames.append(load_eval(path, label))
    all_data = pd.concat(frames, ignore_index=True)

    measures = DIMENSIONS + ["composite"]
    models = sorted(all_data["model"].unique())

    print("=" * 90)
    print("CROSS-MODEL ANALYSIS")
    print(f"Models: {len(models)}  |  Total observations: {len(all_data)}")
    print("=" * 90)

    # ── 1. Descriptive statistics ──
    print("\n" + "─" * 90)
    print("1. DESCRIPTIVE STATISTICS")
    print("─" * 90)

    for measure in measures:
        print(f"\n  {measure}:")
        print(f"  {'Model':<28} {'N':>4} {'Mean':>8} {'SD':>8} {'95% CI':>20}")
        print("  " + "-" * 70)
        # Collect for sorting by mean
        rows = []
        for m in models:
            vals = all_data[all_data["model"] == m][measure].values
            ci_lo, ci_hi = bootstrap_ci_single(vals)
            rows.append((m, len(vals), vals.mean(), vals.std(ddof=1), ci_lo, ci_hi))
        rows.sort(key=lambda r: -r[2])  # sort by mean descending
        for m, n, mean, sd, ci_lo, ci_hi in rows:
            ci_str = f"[{ci_lo:.2f}, {ci_hi:.2f}]"
            print(f"  {m:<28} {n:>4} {mean:>8.2f} {sd:>8.2f} {ci_str:>20}")

    # ── 2. Overall effect size (ANOVA) ──
    print("\n" + "─" * 90)
    print("2. OVERALL EFFECT SIZE (ONE-WAY ANOVA)")
    print("─" * 90)

    print(f"\n  {'Measure':<20} {'F':>10} {'df':>10} {'p':>12} {'η²':>8} {'Cohen f':>10} {'Size':>10}")
    print("  " + "-" * 82)
    for measure in measures:
        ae = anova_effect_sizes(all_data, measure)
        df_str = f"({ae['df_between']},{ae['df_within']})"
        if ae["cohens_f"] >= 0.40:
            size = "large"
        elif ae["cohens_f"] >= 0.25:
            size = "medium"
        else:
            size = "small"
        print(f"  {measure:<20} {ae['f_stat']:>10.2f} {df_str:>10} {ae['p_value']:>12.6f} "
              f"{ae['eta_squared']:>8.3f} {ae['cohens_f']:>10.3f} {size:>10}")

    print("""
  η²: proportion of total variance explained by model identity
  Cohen's f: standardized effect size (0.10 small, 0.25 medium, 0.40 large)
  """)

    # ── 3. Pairwise comparisons ──
    print("─" * 90)
    print("3. PAIRWISE COMPARISONS (composite)")
    print("─" * 90)

    # Sort models by composite mean for readable output
    model_means = {m: all_data[all_data["model"] == m]["composite"].mean() for m in models}
    models_ranked = sorted(models, key=lambda m: -model_means[m])

    print(f"\n  {'Model A':<18} {'Model B':<18} {'Diff':>8} {'95% CI':>22} {'d':>8} {'Size':>10}")
    print("  " + "-" * 86)

    pair_results = []
    for a, b in combinations(models_ranked, 2):
        vals_a = all_data[all_data["model"] == a]["composite"].values
        vals_b = all_data[all_data["model"] == b]["composite"].values
        diff = vals_a.mean() - vals_b.mean()
        ci_lo, ci_hi = bootstrap_ci_diff(vals_a, vals_b)
        d = cohens_d(vals_a, vals_b)

        if abs(d) >= 0.80:
            size = "large"
        elif abs(d) >= 0.50:
            size = "medium"
        elif abs(d) >= 0.20:
            size = "small"
        else:
            size = "negligible"

        sig = "*" if (ci_lo > 0 or ci_hi < 0) else ""

        pair_results.append({
            "a": a, "b": b, "diff": diff,
            "ci_lo": ci_lo, "ci_hi": ci_hi, "d": d, "size": size, "sig": sig,
        })

        ci_str = f"[{ci_lo:+.2f}, {ci_hi:+.2f}]"
        print(f"  {a:<18} {b:<18} {diff:>+8.2f} {ci_str:>22} {d:>+8.2f} {size:>10} {sig}")

    n_sig = sum(1 for p in pair_results if p["sig"] == "*")
    print(f"\n  * = 95% CI excludes zero (significant difference)")
    print(f"  Significant pairs: {n_sig}/{len(pair_results)}")

    # ── 4. Pairwise comparisons for other dimensions ──
    print("\n" + "─" * 90)
    print("4. PAIRWISE COMPARISONS (other dimensions)")
    print("─" * 90)

    for measure in DIMENSIONS:
        print(f"\n  {measure}:")
        print(f"  {'Model A':<18} {'Model B':<18} {'Diff':>8} {'95% CI':>22} {'d':>8} {'Size':>10}")
        print("  " + "-" * 86)

        # Sort by this dimension's mean
        dim_means = {m: all_data[all_data["model"] == m][measure].mean() for m in models}
        ranked = sorted(models, key=lambda m: -dim_means[m])

        for a, b in combinations(ranked, 2):
            vals_a = all_data[all_data["model"] == a][measure].values
            vals_b = all_data[all_data["model"] == b][measure].values
            diff = vals_a.mean() - vals_b.mean()
            ci_lo, ci_hi = bootstrap_ci_diff(vals_a, vals_b)
            d = cohens_d(vals_a, vals_b)

            if abs(d) >= 0.80:
                size = "large"
            elif abs(d) >= 0.50:
                size = "medium"
            elif abs(d) >= 0.20:
                size = "small"
            else:
                size = "negligible"

            sig = "*" if (ci_lo > 0 or ci_hi < 0) else ""
            ci_str = f"[{ci_lo:+.2f}, {ci_hi:+.2f}]"
            print(f"  {a:<18} {b:<18} {diff:>+8.2f} {ci_str:>22} {d:>+8.2f} {size:>10} {sig}")

    # ── 5. Sensitivity analysis ──
    print("\n" + "─" * 90)
    print("5. SENSITIVITY ANALYSIS")
    print("─" * 90)

    for measure in measures:
        # Pooled within-model SD (RMS)
        sds = []
        ns = []
        for m in models:
            vals = all_data[all_data["model"] == m][measure].values
            sds.append(vals.std(ddof=1))
            ns.append(len(vals))
        pooled_sd = np.sqrt(np.mean([s ** 2 for s in sds]))
        median_n = int(np.median(ns))

        z_a = stats.norm.ppf(0.975)
        z_b = stats.norm.ppf(0.80)
        coeff = z_a + z_b

        mdd_current = coeff * pooled_sd * np.sqrt(2 / median_n)
        mdd_852 = coeff * pooled_sd * np.sqrt(2 / 852)

        if measure == "composite":
            scale = 100
        elif measure == "sustained_turns":
            scale = 15
        else:
            scale = 5

        print(f"\n  {measure} (pooled SD = {pooled_sd:.2f}):")
        print(f"    At n = {median_n} (current median):  MDE = {mdd_current:.2f} ({mdd_current/scale*100:.1f}% of scale)")
        print(f"    At n = 852 (full scenario set): MDE = {mdd_852:.2f} ({mdd_852/scale*100:.1f}% of scale)")

    # ── 6. Summary ──
    print("\n" + "=" * 90)
    print("SUMMARY")
    print("=" * 90)

    ae = anova_effect_sizes(all_data, "composite")
    print(f"""
  Models evaluated: {len(models)}
  Total observations: {len(all_data)}

  Composite score:
    Overall effect: F({ae['df_between']},{ae['df_within']}) = {ae['f_stat']:.2f}, p < .001,
      η² = {ae['eta_squared']:.3f}, Cohen's f = {ae['cohens_f']:.3f} (large)
    Significant pairwise differences: {n_sig}/{len(pair_results)}
""")

    # Model ranking
    print("  Model ranking (composite mean, descending):")
    for m in models_ranked:
        vals = all_data[all_data["model"] == m]["composite"]
        ci_lo, ci_hi = bootstrap_ci_single(vals.values)
        print(f"    {m:<28} {vals.mean():>6.1f}  [{ci_lo:.1f}, {ci_hi:.1f}]")


if __name__ == "__main__":
    main()
