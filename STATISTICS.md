# Cross-Model Analysis

10 models | 500 total observations (50 per model, 1 epoch)

## 1. Descriptive Statistics

### Believability (1-5 scale)

| Model | N | Mean | SD | 95% CI |
|-------|--:|-----:|---:|--------|
| deepseek-v3 | 50 | 3.96 | 0.28 | [3.88, 4.04] |
| minimax-m2.5 | 50 | 3.88 | 0.80 | [3.64, 4.08] |
| qwen3-235b | 50 | 3.86 | 0.61 | [3.68, 3.98] |
| qwen3-235b-think | 50 | 3.86 | 0.35 | [3.76, 3.94] |
| glm-5 | 50 | 3.82 | 0.69 | [3.60, 3.98] |
| qwq-32b | 50 | 3.78 | 0.42 | [3.66, 3.90] |
| kimi-k2.5 | 50 | 3.64 | 0.60 | [3.48, 3.80] |
| qwen3-8b | 50 | 3.18 | 0.48 | [3.06, 3.32] |
| llama-3.3-70b | 50 | 3.16 | 0.79 | [2.92, 3.36] |
| llama3-8b | 50 | 2.46 | 0.97 | [2.18, 2.72] |

### Consistency (1-5 scale)

| Model | N | Mean | SD | 95% CI |
|-------|--:|-----:|---:|--------|
| minimax-m2.5 | 50 | 3.28 | 1.18 | [2.96, 3.60] |
| deepseek-v3 | 50 | 3.02 | 0.59 | [2.86, 3.18] |
| glm-5 | 50 | 2.98 | 1.08 | [2.68, 3.28] |
| qwen3-235b | 50 | 2.88 | 0.82 | [2.64, 3.10] |
| qwq-32b | 50 | 2.50 | 0.86 | [2.26, 2.74] |
| kimi-k2.5 | 50 | 2.46 | 0.81 | [2.24, 2.68] |
| llama-3.3-70b | 50 | 2.40 | 0.81 | [2.18, 2.62] |
| qwen3-8b | 50 | 2.36 | 0.75 | [2.16, 2.56] |
| qwen3-235b-think | 50 | 2.16 | 0.68 | [1.98, 2.34] |
| llama3-8b | 50 | 2.12 | 0.92 | [1.88, 2.36] |

### Sustained Turns (1-15 scale)

| Model | N | Mean | SD | 95% CI |
|-------|--:|-----:|---:|--------|
| qwen3-235b | 50 | 4.34 | 1.08 | [4.02, 4.62] |
| deepseek-v3 | 50 | 4.20 | 1.12 | [3.88, 4.48] |
| qwen3-235b-think | 50 | 4.16 | 0.98 | [3.90, 4.42] |
| qwq-32b | 50 | 3.90 | 1.13 | [3.58, 4.20] |
| kimi-k2.5 | 50 | 3.64 | 1.21 | [3.30, 3.96] |
| qwen3-8b | 50 | 3.56 | 1.03 | [3.28, 3.84] |
| glm-5 | 50 | 3.30 | 1.66 | [2.84, 3.74] |
| llama-3.3-70b | 50 | 3.04 | 1.11 | [2.72, 3.34] |
| llama3-8b | 50 | 2.62 | 1.24 | [2.28, 2.94] |
| minimax-m2.5 | 50 | 2.56 | 2.13 | [1.98, 3.14] |

### Composite (0-100 scale)

| Model | N | Mean | SD | 95% CI |
|-------|--:|-----:|---:|--------|
| deepseek-v3 | 50 | 68.28 | 12.25 | [64.80, 71.40] |
| qwen3-235b | 50 | 66.47 | 15.28 | [62.04, 70.31] |
| glm-5 | 50 | 57.24 | 22.79 | [50.92, 63.27] |
| qwq-32b | 50 | 56.81 | 17.90 | [51.77, 61.52] |
| kimi-k2.5 | 50 | 54.89 | 21.23 | [48.90, 60.44] |
| qwen3-235b-think | 50 | 53.74 | 16.78 | [48.96, 58.14] |
| qwen3-8b | 50 | 50.43 | 16.35 | [45.86, 54.86] |
| llama-3.3-70b | 50 | 49.60 | 18.71 | [44.26, 54.45] |
| minimax-m2.5 | 50 | 44.79 | 24.27 | [38.01, 51.48] |
| llama3-8b | 50 | 37.33 | 21.57 | [31.29, 43.22] |

## 2. Overall Effect Size (One-Way ANOVA)

| Measure | F | df | p | eta-squared | Cohen's f | Size |
|---------|--:|---:|--:|------------:|----------:|------|
| believability | 28.70 | (9, 490) | < .000001 | 0.345 | 0.726 | large |
| consistency | 10.44 | (9, 490) | < .000001 | 0.161 | 0.438 | large |
| sustained_turns | 11.97 | (9, 490) | < .000001 | 0.180 | 0.469 | large |
| composite | 11.84 | (9, 490) | < .000001 | 0.179 | 0.466 | large |

- **eta-squared**: proportion of total variance explained by model identity
- **Cohen's f**: standardized effect size (0.10 small, 0.25 medium, 0.40 large)

## 3. Pairwise Comparisons (Composite)

| Model A | Model B | Diff | 95% CI | Cohen's d | Size | Sig |
|---------|---------|-----:|--------|----------:|------|:---:|
| deepseek-v3 | qwen3-235b | +1.81 | [-3.52, +7.23] | +0.13 | negligible | |
| deepseek-v3 | glm-5 | +11.04 | [+3.99, +18.03] | +0.60 | medium | * |
| deepseek-v3 | qwq-32b | +11.47 | [+5.69, +17.60] | +0.75 | medium | * |
| deepseek-v3 | kimi-k2.5 | +13.39 | [+6.86, +20.03] | +0.77 | medium | * |
| deepseek-v3 | qwen3-235b-think | +14.54 | [+8.84, +20.22] | +0.99 | large | * |
| deepseek-v3 | qwen3-8b | +17.84 | [+12.20, +23.47] | +1.23 | large | * |
| deepseek-v3 | llama-3.3-70b | +18.68 | [+12.54, +25.03] | +1.18 | large | * |
| deepseek-v3 | minimax-m2.5 | +23.48 | [+15.96, +31.01] | +1.22 | large | * |
| deepseek-v3 | llama3-8b | +30.95 | [+24.21, +37.82] | +1.76 | large | * |
| qwen3-235b | glm-5 | +9.24 | [+1.63, +16.55] | +0.48 | small | * |
| qwen3-235b | qwq-32b | +9.66 | [+3.20, +16.12] | +0.58 | medium | * |
| qwen3-235b | kimi-k2.5 | +11.58 | [+4.36, +18.68] | +0.63 | medium | * |
| qwen3-235b | qwen3-235b-think | +12.73 | [+6.40, +18.98] | +0.79 | medium | * |
| qwen3-235b | qwen3-8b | +16.04 | [+9.97, +22.21] | +1.01 | large | * |
| qwen3-235b | llama-3.3-70b | +16.87 | [+10.16, +23.45] | +0.99 | large | * |
| qwen3-235b | minimax-m2.5 | +21.68 | [+13.83, +29.58] | +1.07 | large | * |
| qwen3-235b | llama3-8b | +29.15 | [+21.88, +36.46] | +1.56 | large | * |
| glm-5 | qwq-32b | +0.43 | [-7.55, +8.37] | +0.02 | negligible | |
| glm-5 | kimi-k2.5 | +2.35 | [-6.24, +10.72] | +0.11 | negligible | |
| glm-5 | qwen3-235b-think | +3.50 | [-4.48, +11.11] | +0.17 | negligible | |
| glm-5 | qwen3-8b | +6.80 | [-0.95, +14.36] | +0.34 | small | |
| glm-5 | llama-3.3-70b | +7.64 | [-0.49, +15.69] | +0.37 | small | |
| glm-5 | minimax-m2.5 | +12.44 | [+3.17, +21.31] | +0.53 | medium | * |
| glm-5 | llama3-8b | +19.91 | [+11.30, +28.47] | +0.90 | large | * |
| qwq-32b | kimi-k2.5 | +1.92 | [-5.72, +9.66] | +0.10 | negligible | |
| qwq-32b | qwen3-235b-think | +3.07 | [-3.66, +9.96] | +0.18 | negligible | |
| qwq-32b | qwen3-8b | +6.38 | [-0.48, +13.17] | +0.37 | small | |
| qwq-32b | llama-3.3-70b | +7.21 | [+0.17, +14.37] | +0.39 | small | * |
| qwq-32b | minimax-m2.5 | +12.02 | [+3.84, +20.36] | +0.56 | medium | * |
| qwq-32b | llama3-8b | +19.48 | [+11.64, +27.15] | +0.98 | large | * |
| kimi-k2.5 | qwen3-235b-think | +1.15 | [-6.35, +8.49] | +0.06 | negligible | |
| kimi-k2.5 | qwen3-8b | +4.45 | [-3.03, +11.77] | +0.23 | small | |
| kimi-k2.5 | llama-3.3-70b | +5.29 | [-2.65, +13.13] | +0.26 | small | |
| kimi-k2.5 | minimax-m2.5 | +10.09 | [+1.10, +18.89] | +0.44 | small | * |
| kimi-k2.5 | llama3-8b | +17.56 | [+9.09, +25.81] | +0.82 | large | * |
| qwen3-235b-think | qwen3-8b | +3.30 | [-3.15, +9.66] | +0.20 | negligible | |
| qwen3-235b-think | llama-3.3-70b | +4.14 | [-2.72, +11.07] | +0.23 | small | |
| qwen3-235b-think | minimax-m2.5 | +8.94 | [+0.63, +17.09] | +0.43 | small | * |
| qwen3-235b-think | llama3-8b | +16.41 | [+8.92, +23.85] | +0.85 | large | * |
| qwen3-8b | llama-3.3-70b | +0.84 | [-5.98, +7.72] | +0.05 | negligible | |
| qwen3-8b | minimax-m2.5 | +5.64 | [-2.38, +13.81] | +0.27 | small | |
| qwen3-8b | llama3-8b | +13.11 | [+5.61, +20.59] | +0.68 | medium | * |
| llama-3.3-70b | minimax-m2.5 | +4.80 | [-3.69, +13.04] | +0.22 | small | |
| llama-3.3-70b | llama3-8b | +12.27 | [+4.41, +20.00] | +0.61 | medium | * |
| minimax-m2.5 | llama3-8b | +7.47 | [-1.25, +16.57] | +0.33 | small | |

\* = 95% bootstrap CI excludes zero. Significant pairs: 27/45.

## 4. Pairwise Comparisons (Sub-Dimensions)

### Believability

| Model A | Model B | Diff | 95% CI | Cohen's d | Size | Sig |
|---------|---------|-----:|--------|----------:|------|:---:|
| deepseek-v3 | minimax-m2.5 | +0.08 | [-0.14, +0.32] | +0.13 | negligible | |
| deepseek-v3 | qwen3-235b | +0.10 | [-0.06, +0.30] | +0.21 | small | |
| deepseek-v3 | qwen3-235b-think | +0.10 | [-0.02, +0.22] | +0.31 | small | |
| deepseek-v3 | glm-5 | +0.14 | [-0.04, +0.36] | +0.27 | small | |
| deepseek-v3 | qwq-32b | +0.18 | [+0.04, +0.32] | +0.50 | medium | * |
| deepseek-v3 | kimi-k2.5 | +0.32 | [+0.14, +0.50] | +0.68 | medium | * |
| deepseek-v3 | qwen3-8b | +0.78 | [+0.62, +0.94] | +1.97 | large | * |
| deepseek-v3 | llama-3.3-70b | +0.80 | [+0.58, +1.04] | +1.35 | large | * |
| deepseek-v3 | llama3-8b | +1.50 | [+1.22, +1.78] | +2.09 | large | * |
| minimax-m2.5 | qwen3-235b | +0.02 | [-0.26, +0.30] | +0.03 | negligible | |
| minimax-m2.5 | qwen3-235b-think | +0.02 | [-0.24, +0.24] | +0.03 | negligible | |
| minimax-m2.5 | glm-5 | +0.06 | [-0.24, +0.36] | +0.08 | negligible | |
| minimax-m2.5 | qwq-32b | +0.10 | [-0.16, +0.34] | +0.16 | negligible | |
| minimax-m2.5 | kimi-k2.5 | +0.24 | [-0.04, +0.50] | +0.34 | small | |
| minimax-m2.5 | qwen3-8b | +0.70 | [+0.44, +0.94] | +1.06 | large | * |
| minimax-m2.5 | llama-3.3-70b | +0.72 | [+0.40, +1.02] | +0.91 | large | * |
| minimax-m2.5 | llama3-8b | +1.42 | [+1.08, +1.76] | +1.59 | large | * |
| qwen3-235b | qwen3-235b-think | +0.00 | [-0.20, +0.16] | +0.00 | negligible | |
| qwen3-235b | glm-5 | +0.04 | [-0.22, +0.28] | +0.06 | negligible | |
| qwen3-235b | qwq-32b | +0.08 | [-0.14, +0.26] | +0.15 | negligible | |
| qwen3-235b | kimi-k2.5 | +0.22 | [-0.02, +0.44] | +0.37 | small | |
| qwen3-235b | qwen3-8b | +0.68 | [+0.46, +0.88] | +1.24 | large | * |
| qwen3-235b | llama-3.3-70b | +0.70 | [+0.42, +0.98] | +0.99 | large | * |
| qwen3-235b | llama3-8b | +1.40 | [+1.08, +1.70] | +1.73 | large | * |
| qwen3-235b-think | glm-5 | +0.04 | [-0.16, +0.26] | +0.07 | negligible | |
| qwen3-235b-think | qwq-32b | +0.08 | [-0.08, +0.24] | +0.21 | small | |
| qwen3-235b-think | kimi-k2.5 | +0.22 | [+0.04, +0.40] | +0.45 | small | * |
| qwen3-235b-think | qwen3-8b | +0.68 | [+0.52, +0.84] | +1.61 | large | * |
| qwen3-235b-think | llama-3.3-70b | +0.70 | [+0.46, +0.94] | +1.14 | large | * |
| qwen3-235b-think | llama3-8b | +1.40 | [+1.12, +1.68] | +1.91 | large | * |
| glm-5 | qwq-32b | +0.04 | [-0.20, +0.24] | +0.07 | negligible | |
| glm-5 | kimi-k2.5 | +0.18 | [-0.08, +0.42] | +0.28 | small | |
| glm-5 | qwen3-8b | +0.64 | [+0.40, +0.86] | +1.07 | large | * |
| glm-5 | llama-3.3-70b | +0.66 | [+0.36, +0.94] | +0.89 | large | * |
| glm-5 | llama3-8b | +1.36 | [+1.04, +1.68] | +1.61 | large | * |
| qwq-32b | kimi-k2.5 | +0.14 | [-0.06, +0.34] | +0.27 | small | |
| qwq-32b | qwen3-8b | +0.60 | [+0.42, +0.78] | +1.33 | large | * |
| qwq-32b | llama-3.3-70b | +0.62 | [+0.38, +0.88] | +0.98 | large | * |
| qwq-32b | llama3-8b | +1.32 | [+1.04, +1.62] | +1.76 | large | * |
| kimi-k2.5 | qwen3-8b | +0.46 | [+0.24, +0.66] | +0.85 | large | * |
| kimi-k2.5 | llama-3.3-70b | +0.48 | [+0.20, +0.76] | +0.68 | medium | * |
| kimi-k2.5 | llama3-8b | +1.18 | [+0.86, +1.50] | +1.46 | large | * |
| qwen3-8b | llama-3.3-70b | +0.02 | [-0.22, +0.28] | +0.03 | negligible | |
| qwen3-8b | llama3-8b | +0.72 | [+0.44, +1.02] | +0.94 | large | * |
| llama-3.3-70b | llama3-8b | +0.70 | [+0.36, +1.04] | +0.79 | medium | * |

### Consistency

| Model A | Model B | Diff | 95% CI | Cohen's d | Size | Sig |
|---------|---------|-----:|--------|----------:|------|:---:|
| minimax-m2.5 | deepseek-v3 | +0.26 | [-0.10, +0.62] | +0.28 | small | |
| minimax-m2.5 | glm-5 | +0.30 | [-0.14, +0.74] | +0.27 | small | |
| minimax-m2.5 | qwen3-235b | +0.40 | [+0.02, +0.80] | +0.39 | small | * |
| minimax-m2.5 | qwq-32b | +0.78 | [+0.36, +1.16] | +0.76 | medium | * |
| minimax-m2.5 | kimi-k2.5 | +0.82 | [+0.44, +1.20] | +0.81 | large | * |
| minimax-m2.5 | llama-3.3-70b | +0.88 | [+0.50, +1.28] | +0.87 | large | * |
| minimax-m2.5 | qwen3-8b | +0.92 | [+0.54, +1.30] | +0.93 | large | * |
| minimax-m2.5 | qwen3-235b-think | +1.12 | [+0.74, +1.50] | +1.16 | large | * |
| minimax-m2.5 | llama3-8b | +1.16 | [+0.76, +1.56] | +1.10 | large | * |
| deepseek-v3 | glm-5 | +0.04 | [-0.30, +0.38] | +0.05 | negligible | |
| deepseek-v3 | qwen3-235b | +0.14 | [-0.12, +0.42] | +0.20 | negligible | |
| deepseek-v3 | qwq-32b | +0.52 | [+0.24, +0.80] | +0.70 | medium | * |
| deepseek-v3 | kimi-k2.5 | +0.56 | [+0.28, +0.84] | +0.79 | medium | * |
| deepseek-v3 | llama-3.3-70b | +0.62 | [+0.36, +0.90] | +0.88 | large | * |
| deepseek-v3 | qwen3-8b | +0.66 | [+0.40, +0.92] | +0.98 | large | * |
| deepseek-v3 | qwen3-235b-think | +0.86 | [+0.62, +1.10] | +1.35 | large | * |
| deepseek-v3 | llama3-8b | +0.90 | [+0.60, +1.20] | +1.17 | large | * |
| glm-5 | qwen3-235b | +0.10 | [-0.28, +0.46] | +0.10 | negligible | |
| glm-5 | qwq-32b | +0.48 | [+0.10, +0.86] | +0.49 | small | * |
| glm-5 | kimi-k2.5 | +0.52 | [+0.14, +0.90] | +0.54 | medium | * |
| glm-5 | llama-3.3-70b | +0.58 | [+0.20, +0.94] | +0.61 | medium | * |
| glm-5 | qwen3-8b | +0.62 | [+0.26, +0.98] | +0.67 | medium | * |
| glm-5 | qwen3-235b-think | +0.82 | [+0.46, +1.16] | +0.91 | large | * |
| glm-5 | llama3-8b | +0.86 | [+0.46, +1.24] | +0.86 | large | * |
| qwen3-235b | qwq-32b | +0.38 | [+0.04, +0.70] | +0.45 | small | * |
| qwen3-235b | kimi-k2.5 | +0.42 | [+0.10, +0.74] | +0.51 | medium | * |
| qwen3-235b | llama-3.3-70b | +0.48 | [+0.16, +0.78] | +0.59 | medium | * |
| qwen3-235b | qwen3-8b | +0.52 | [+0.20, +0.82] | +0.66 | medium | * |
| qwen3-235b | qwen3-235b-think | +0.72 | [+0.42, +1.00] | +0.95 | large | * |
| qwen3-235b | llama3-8b | +0.76 | [+0.42, +1.10] | +0.87 | large | * |
| qwq-32b | kimi-k2.5 | +0.04 | [-0.28, +0.36] | +0.05 | negligible | |
| qwq-32b | llama-3.3-70b | +0.10 | [-0.22, +0.44] | +0.12 | negligible | |
| qwq-32b | qwen3-8b | +0.14 | [-0.18, +0.46] | +0.17 | negligible | |
| qwq-32b | qwen3-235b-think | +0.34 | [+0.04, +0.64] | +0.44 | small | * |
| qwq-32b | llama3-8b | +0.38 | [+0.04, +0.74] | +0.43 | small | * |
| kimi-k2.5 | llama-3.3-70b | +0.06 | [-0.26, +0.38] | +0.07 | negligible | |
| kimi-k2.5 | qwen3-8b | +0.10 | [-0.20, +0.40] | +0.13 | negligible | |
| kimi-k2.5 | qwen3-235b-think | +0.30 | [+0.02, +0.58] | +0.40 | small | * |
| kimi-k2.5 | llama3-8b | +0.34 | [+0.00, +0.68] | +0.39 | small | |
| llama-3.3-70b | qwen3-8b | +0.04 | [-0.26, +0.34] | +0.05 | negligible | |
| llama-3.3-70b | qwen3-235b-think | +0.24 | [-0.06, +0.52] | +0.32 | small | |
| llama-3.3-70b | llama3-8b | +0.28 | [-0.06, +0.60] | +0.32 | small | |
| qwen3-8b | qwen3-235b-think | +0.20 | [-0.08, +0.48] | +0.28 | small | |
| qwen3-8b | llama3-8b | +0.24 | [-0.08, +0.56] | +0.29 | small | |
| qwen3-235b-think | llama3-8b | +0.04 | [-0.28, +0.34] | +0.05 | negligible | |

### Sustained Turns

| Model A | Model B | Diff | 95% CI | Cohen's d | Size | Sig |
|---------|---------|-----:|--------|----------:|------|:---:|
| qwen3-235b | deepseek-v3 | +0.14 | [-0.28, +0.56] | +0.13 | negligible | |
| qwen3-235b | qwen3-235b-think | +0.18 | [-0.24, +0.56] | +0.17 | negligible | |
| qwen3-235b | qwq-32b | +0.44 | [+0.02, +0.86] | +0.40 | small | * |
| qwen3-235b | kimi-k2.5 | +0.70 | [+0.26, +1.14] | +0.61 | medium | * |
| qwen3-235b | qwen3-8b | +0.78 | [+0.34, +1.18] | +0.74 | medium | * |
| qwen3-235b | glm-5 | +1.04 | [+0.48, +1.58] | +0.74 | medium | * |
| qwen3-235b | llama-3.3-70b | +1.30 | [+0.86, +1.72] | +1.19 | large | * |
| qwen3-235b | llama3-8b | +1.72 | [+1.26, +2.18] | +1.48 | large | * |
| qwen3-235b | minimax-m2.5 | +1.78 | [+1.10, +2.42] | +1.05 | large | * |
| deepseek-v3 | qwen3-235b-think | +0.04 | [-0.36, +0.44] | +0.04 | negligible | |
| deepseek-v3 | qwq-32b | +0.30 | [-0.14, +0.74] | +0.27 | small | |
| deepseek-v3 | kimi-k2.5 | +0.56 | [+0.12, +1.00] | +0.48 | small | * |
| deepseek-v3 | qwen3-8b | +0.64 | [+0.22, +1.04] | +0.59 | medium | * |
| deepseek-v3 | glm-5 | +0.90 | [+0.36, +1.44] | +0.64 | medium | * |
| deepseek-v3 | llama-3.3-70b | +1.16 | [+0.74, +1.58] | +1.04 | large | * |
| deepseek-v3 | llama3-8b | +1.58 | [+1.12, +2.02] | +1.33 | large | * |
| deepseek-v3 | minimax-m2.5 | +1.64 | [+0.98, +2.28] | +0.96 | large | * |
| qwen3-235b-think | qwq-32b | +0.26 | [-0.16, +0.68] | +0.25 | small | |
| qwen3-235b-think | kimi-k2.5 | +0.52 | [+0.10, +0.94] | +0.47 | small | * |
| qwen3-235b-think | qwen3-8b | +0.60 | [+0.22, +0.98] | +0.60 | medium | * |
| qwen3-235b-think | glm-5 | +0.86 | [+0.34, +1.40] | +0.63 | medium | * |
| qwen3-235b-think | llama-3.3-70b | +1.12 | [+0.72, +1.52] | +1.07 | large | * |
| qwen3-235b-think | llama3-8b | +1.54 | [+1.12, +1.98] | +1.38 | large | * |
| qwen3-235b-think | minimax-m2.5 | +1.60 | [+0.94, +2.24] | +0.97 | large | * |
| qwq-32b | kimi-k2.5 | +0.26 | [-0.20, +0.72] | +0.22 | small | |
| qwq-32b | qwen3-8b | +0.34 | [-0.08, +0.76] | +0.31 | small | |
| qwq-32b | glm-5 | +0.60 | [+0.06, +1.16] | +0.42 | small | * |
| qwq-32b | llama-3.3-70b | +0.86 | [+0.42, +1.28] | +0.77 | medium | * |
| qwq-32b | llama3-8b | +1.28 | [+0.82, +1.76] | +1.08 | large | * |
| qwq-32b | minimax-m2.5 | +1.34 | [+0.68, +2.00] | +0.79 | medium | * |
| kimi-k2.5 | qwen3-8b | +0.08 | [-0.36, +0.52] | +0.07 | negligible | |
| kimi-k2.5 | glm-5 | +0.34 | [-0.24, +0.92] | +0.23 | small | |
| kimi-k2.5 | llama-3.3-70b | +0.60 | [+0.14, +1.06] | +0.52 | medium | * |
| kimi-k2.5 | llama3-8b | +1.02 | [+0.54, +1.48] | +0.83 | large | * |
| kimi-k2.5 | minimax-m2.5 | +1.08 | [+0.40, +1.76] | +0.62 | medium | * |
| qwen3-8b | glm-5 | +0.26 | [-0.26, +0.80] | +0.19 | negligible | |
| qwen3-8b | llama-3.3-70b | +0.52 | [+0.10, +0.94] | +0.49 | small | * |
| qwen3-8b | llama3-8b | +0.94 | [+0.50, +1.40] | +0.82 | large | * |
| qwen3-8b | minimax-m2.5 | +1.00 | [+0.34, +1.66] | +0.60 | medium | * |
| glm-5 | llama-3.3-70b | +0.26 | [-0.30, +0.80] | +0.18 | negligible | |
| glm-5 | llama3-8b | +0.68 | [+0.10, +1.26] | +0.46 | small | * |
| glm-5 | minimax-m2.5 | +0.74 | [+0.00, +1.48] | +0.39 | small | |
| llama-3.3-70b | llama3-8b | +0.42 | [-0.04, +0.88] | +0.36 | small | |
| llama-3.3-70b | minimax-m2.5 | +0.48 | [-0.20, +1.14] | +0.28 | small | |
| llama3-8b | minimax-m2.5 | +0.06 | [-0.64, +0.74] | +0.03 | negligible | |

## 5. Sensitivity Analysis

Minimum detectable effect (MDE) at alpha = 0.05, power = 0.80.

| Measure | Pooled SD | MDE at n=50 | % of scale | MDE at n=852 | % of scale |
|---------|----------:|------------:|-----------:|-------------:|-----------:|
| believability | 0.63 | 0.36 | 7.1% | 0.09 | 1.7% |
| consistency | 0.87 | 0.49 | 9.7% | 0.12 | 2.4% |
| sustained_turns | 1.31 | 0.74 | 4.9% | 0.18 | 1.2% |
| composite | 19.05 | 10.67 | 10.7% | 2.59 | 2.6% |

## 6. Summary

- **Models evaluated**: 10
- **Total observations**: 500
- **Composite score overall effect**: F(9, 490) = 11.84, p < .001, eta-squared = 0.179, Cohen's f = 0.466 (large)
- **Significant pairwise differences**: 27/45

### Model Ranking (composite mean, descending)

| Model | Mean | 95% CI |
|-------|-----:|--------|
| deepseek-v3 | 68.3 | [64.8, 71.4] |
| qwen3-235b | 66.5 | [62.0, 70.3] |
| glm-5 | 57.2 | [50.9, 63.3] |
| qwq-32b | 56.8 | [51.8, 61.5] |
| kimi-k2.5 | 54.9 | [48.9, 60.4] |
| qwen3-235b-think | 53.7 | [49.0, 58.1] |
| qwen3-8b | 50.4 | [45.9, 54.9] |
| llama-3.3-70b | 49.6 | [44.3, 54.4] |
| minimax-m2.5 | 44.8 | [38.0, 51.5] |
| llama3-8b | 37.3 | [31.3, 43.2] |
