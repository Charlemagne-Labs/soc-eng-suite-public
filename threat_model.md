# Threat Model: Social Engineering Attack Categories

This document models different categories of social engineering attacks, their operational stages, and potential LLM involvement at each stage.

## Attack Categories

| Category | Targeting | Attacker Knowledge | Interaction Model | Example Objective |
|----------|-----------|-------------------|-------------------|-------------------|
| Phishing | Mass | Minimal (email, possibly name/address) | Single-turn | Click malicious link, enter credentials |
| Spearphishing | Targeted | Detailed (org, role, tools, vendors, counterparties) | Single-turn | Authorize payment, install software, share credentials |
| Social Engineering | Mass or Targeted | Varies | Multi-turn | Build trust over time, manipulate into complex actions |

### Phishing

**Definition**: Mass attacks targeting large numbers of potential victims with minimal personalization.

**Attacker Knowledge**:
- Email address (required)
- Possibly name, physical address, or other basic PII from data breaches

**Interaction Model**: Single-turn. The attack succeeds or fails based on one message. No back-and-forth conversation.

**Typical Objectives**:
- Click a malicious link
- Download malware
- Enter credentials on a fake login page
- Call a fraudulent phone number

**Examples**:
- "Your package could not be delivered" SMS with tracking link
- "Verify your account" email mimicking a bank
- "Invoice attached" email with malicious PDF

---

### Spearphishing

**Definition**: Targeted attacks against specific individuals, leveraging detailed knowledge of the target's context within an organization.

**Attacker Knowledge**:
- Target's name, role, and responsibilities
- Organizational structure (manager, reports, peers)
- Tools and systems in use (Slack, Salesforce, specific vendors)
- Current projects, deals, or initiatives
- Counterparties and business relationships
- Communication style and patterns

**Interaction Model**: Single-turn. Despite the sophistication, the attack still relies on a single convincing message to trigger action.

**Typical Objectives**:
- Authorize a fraudulent wire transfer (BEC)
- Provide access credentials
- Install "required" software
- Share sensitive documents
- Approve a fake vendor invoice

**Examples**:
- Email appearing to be from CEO requesting urgent wire transfer
- Message from "IT" about required security update
- Invoice from a known vendor with altered payment details

---

### Social Engineering (Multi-turn)

**Definition**: Attacks requiring sustained interaction over multiple exchanges to build trust, gather information, or manipulate the target into action.

**Attacker Knowledge**: Varies from minimal (mass) to extensive (targeted). Knowledge may also be gathered during the interaction itself.

**Interaction Model**: Multi-turn. The attack unfolds over multiple messages, calls, or interactions. May span hours, days, or weeks.

**Typical Objectives**:
- Build a relationship to exploit later
- Gradually extract sensitive information
- Manipulate target into actions they would refuse if asked directly
- Overcome skepticism through repeated "legitimate" interactions

**Examples**:
- Romance scams building trust over weeks before requesting money
- Fake recruiter gathering information about target's employer
- "Wrong number" text evolving into investment scam
- Technical support scam with extended phone interaction

---

## Operational Stages

Social engineering attacks generally follow a seven-stage lifecycle, though not all stages apply to every attack type.

| Stage | Description | Phishing | Spearphishing | Social Engineering |
|-------|-------------|----------|---------------|-------------------|
| 1. Setup | Prepare infrastructure and assets | Yes | Yes | Yes |
| 2. Reconnaissance | Identify and research victims | Minimal | Extensive | Varies |
| 3. First Turn | First communication with victim | Yes | Yes | Yes |
| 4. Ongoing Turns | Impersonation or sustained manipulation | Minimal | Moderate | Extensive |
| 5. Execution | Induce victim to take desired action | Yes | Yes | Yes |
| 6. Monetization | Convert extracted value to usable assets | Yes | Yes | Yes |
| 7. Evasion | Delay detection and destroy evidence | Minimal | Moderate | Extensive |

---

### Stage 1: Setup

The attacker prepares the infrastructure, identities, and materials needed to execute the attack.

**Identity Infrastructure**:
- Disposable email accounts (Gmail, ProtonMail, corporate lookalikes)
- VoIP phone numbers for calls and SMS
- Social media profiles and messaging accounts
- Personas with backstories, profile photos, employment history

**Technical Infrastructure**:
- Phishing websites and credential capture pages
- Cloned corporate login portals
- URL shorteners and redirect chains
- Malware hosting and delivery mechanisms

**Financial Infrastructure**:
- Cryptocurrency wallets
- Bank accounts (often via money mules)
- Payment processor accounts
- Gift card redemption channels

**Content Assets**:
- Message templates for various scenarios
- Forged documents (invoices, contracts, IDs, screenshots)
- Operational playbooks standardizing execution
- Voice scripts for phone-based attacks

---

### Stage 2: Reconnaissance

The attacker identifies potential victims and gathers information based on vulnerability, value, and accessibility.

**Selection Criteria**:

| Factor | Description | Examples |
|--------|-------------|----------|
| Demographic vulnerability | Groups more susceptible to specific tactics | Elderly for tech support scams, young adults for job scams |
| Financial capacity | Ability to pay or transfer funds | Business executives, real estate buyers, investors |
| Behavioral signals | Activities suggesting receptiveness | Active on dating apps, job hunting, posting about travel |
| Role-based access | Position grants access to valuable systems/data | Finance staff, IT administrators, executive assistants |
| Data availability | Information exposed in breaches or public sources | Leaked credentials, social media details, corporate directories |

**Reconnaissance Approaches**:
- **Passive**: Harvest emails/numbers and blast messages at scale
- **Active research**: Investigate specific individuals via LinkedIn, company websites, social media
- **Inbound attraction**: Use ads, fake job postings, or social media to draw victims in

---

### Stage 3: First Turn

The attacker initiates communication through a channel that appears legitimate and invites response.

**Private Channels**:
- Email (spoofed sender, lookalike domain, compromised account)
- SMS and messaging apps (WhatsApp, Telegram, Signal)
- Phone calls (spoofed caller ID)
- Direct messages on social platforms

**Platform Channels**:
- Comments or posts on social media
- Listings on marketplaces (job boards, real estate, e-commerce)
- Dating app profiles and messages
- Forum posts and community engagement

**First Turn Strategies**:
- **Impersonation**: Pose as trusted entity (bank, employer, government, vendor)
- **Opportunity**: Offer something desirable (job, investment, relationship, prize)
- **Problem**: Create urgency around a fake issue (account compromise, missed delivery, legal threat)

---

### Stage 4: Ongoing Turns

The attacker deceives the victim through impersonation, false pretenses, or sustained manipulation to overcome rational resistance.

**Psychological Levers**:

| Lever | Mechanism | Example |
|-------|-----------|---------|
| Trust | Establish credibility and rapport | "I've been in your situation before..." |
| Authority | Leverage perceived power or expertise | "This is the fraud department calling..." |
| Urgency | Create time pressure | "Your account will be closed in 24 hours" |
| Fear | Threaten negative consequences | "We'll have to involve law enforcement" |
| Greed | Promise exceptional returns | "Early investors are seeing 40% monthly returns" |
| Reciprocity | Create sense of obligation | "I helped you, now I need a small favor" |
| Scarcity | Imply limited availability | "Only 3 spots left in this program" |

**Ongoing Turns Intensity by Attack Type**:
- **Phishing**: Minimal—relies primarily on urgency and authority in a single message
- **Spearphishing**: Moderate—adds trust through contextual details and personalization
- **Social Engineering**: Extensive—builds relationships over time, combines multiple levers

---

### Stage 5: Execution

The attacker induces the victim to perform a specific action that delivers value to the attacker.

**Action Types**:

| Target | Method | Example |
|--------|--------|---------|
| Money | Wire transfer, crypto payment, gift cards | "Transfer the funds to this account for the vendor payment" |
| Credentials | Phishing page, direct request | "Please verify your login at this link" |
| Access | Remote desktop, malware installation | "Install this tool so I can help fix your computer" |
| Data | Document request, screen sharing | "Send me the customer list for the audit" |
| Identity | ID documents, personal information | "I need a photo of your driver's license to verify your account" |

**Execution Characteristics by Attack Type**:
- **Phishing**: Automated capture (credential harvesting, malware download)
- **Spearphishing**: High-value single action (wire transfer, access grant)
- **Social Engineering**: May involve multiple smaller actions building to larger ones

---

### Stage 6: Monetization

The attacker converts extracted value into usable, untraceable assets.

**Monetization Methods**:

| Extracted Value | Conversion Method |
|-----------------|-------------------|
| Wire transfers | Layered transfers through multiple accounts, often via money mules |
| Cryptocurrency | Mixing services, cross-chain bridges, conversion to privacy coins |
| Credentials | Sold on dark web markets, used for account takeover, lateral movement |
| Identity documents | Used to open fraudulent accounts, sold to other criminals |
| Corporate access | Ransomware deployment, data exfiltration, sold to other threat actors |
| Gift cards | Redeemed immediately, resold at discount |

---

### Stage 7: Evasion

The attacker delays detection, destroys evidence, and avoids enforcement to lower chances of recovery.

**Evasion Techniques**:

| Technique | Description | Examples |
|-----------|-------------|----------|
| Log destruction | Remove or alter records of attacker activity | Delete email trails, clear access logs, wipe chat histories |
| Infrastructure teardown | Dismantle attack infrastructure before forensic analysis | Take down phishing sites, abandon domains, rotate IPs |
| Anti-forensics | Interfere with incident response and investigation | Use encrypted channels, employ steganography, tamper with timestamps |
| Identity obfuscation | Prevent attribution to the attacker | VPNs, Tor, disposable identities, compromised third-party accounts |
| Misdirection | Redirect investigators toward false leads | Plant false indicators of compromise, frame other actors |

**Evasion Intensity by Attack Type**:
- **Phishing**: Minimal—infrastructure is disposable and high-volume, little effort spent on individual campaigns
- **Spearphishing**: Moderate—targeted nature means higher risk of investigation, some cleanup required
- **Social Engineering**: Extensive—prolonged engagement creates more evidence trails requiring active management

---

## LLM Assistance Analysis

This section analyzes how LLMs and other AI systems could potentially automate or enhance each operational stage across different attack types.

---

### Stage 1: Setup — AI Automation Opportunities

| Capability | Description | Attack Types |
|------------|-------------|--------------|
| Persona generation | Create coherent fake identities with backstories, employment history, interests | All |
| Profile photo generation | Generate realistic synthetic faces for social profiles | All |
| Template authoring | Write message templates for various scenarios and demographics | Phishing, Spearphishing |
| Document forgery | Generate fake invoices, contracts, ID cards, screenshots | Spearphishing, Social Engineering |
| Website content | Write convincing copy for phishing sites and fake company pages | All |
| Script writing | Create phone scripts and conversation playbooks | Social Engineering |
| Translation | Localize attack materials to multiple languages | Phishing |

**Examples**:
- Generate 50 unique "account verification" email templates to evade spam filters
- Create a complete fake LinkedIn profile with realistic job history and recommendations
- Produce a fake invoice matching a target company's vendor format

---

### Stage 2: Reconnaissance — AI Automation Opportunities

| Capability | Description | Attack Types |
|------------|-------------|--------------|
| Social media analysis | Scrape and summarize target's posts, interests, relationships | Spearphishing, Social Engineering |
| Organizational mapping | Build org charts from LinkedIn, identify reporting structures | Spearphishing |
| Writing style analysis | Analyze target's communications to mimic their tone | Spearphishing |
| Vulnerability identification | Flag targets showing behavioral signals (job seeking, financial stress) | All |
| Data correlation | Combine breach data, public records, social media into unified profiles | Spearphishing, Social Engineering |
| Batch enrichment | Enrich large contact lists with contextual data | Phishing |

**Examples**:
- Summarize a target executive's recent LinkedIn posts, conference talks, and company announcements
- Identify employees likely to have wire transfer authority based on job titles
- Correlate a leaked email list with social media profiles to add names and employers

---

### Stage 3: First Turn — AI Automation Opportunities

| Capability | Description | Attack Types |
|------------|-------------|--------------|
| Message personalization | Insert target-specific details into templates at scale | All |
| Tone matching | Adjust formality, urgency, friendliness based on target profile | Spearphishing, Social Engineering |
| A/B generation | Create multiple message variants for testing effectiveness | Phishing |
| Platform adaptation | Rewrite content for email vs SMS vs LinkedIn vs dating apps | All |
| Translation and localization | Adapt messages for different languages and cultural contexts | Phishing |
| Timing optimization | Analyze target behavior to suggest optimal send times | Spearphishing |

**Examples**:
- Generate 1000 personalized "package delivery" SMS messages with recipient names
- Rewrite a BEC email in the CEO's typical communication style
- Create casual dating app openers based on target's profile interests

---

### Stage 4: Ongoing Turns — AI Automation Opportunities

| Capability | Description | Attack Types |
|------------|-------------|--------------|
| Real-time conversation | Handle multi-turn chat/email exchanges autonomously | Social Engineering |
| Objection handling | Generate responses to victim skepticism or questions | Social Engineering |
| Persona consistency | Maintain coherent identity across many interactions | Social Engineering |
| Backstory elaboration | Invent plausible details on demand when questioned | Social Engineering |
| Emotional manipulation | Adapt tone to build trust, create urgency, or apply pressure | Social Engineering |
| Voice synthesis | Clone voices for phone-based impersonation | Spearphishing, Social Engineering |
| Video deepfakes | Generate synthetic video for video call impersonation | Spearphishing |

**Examples**:
- Conduct a week-long romance scam conversation with minimal human oversight
- Generate believable answers when victim asks unexpected questions about attacker's "job"
- Clone a CEO's voice from earnings call recordings for a vishing attack

---

### Stage 5: Execution — AI Automation Opportunities

| Capability | Description | Attack Types |
|------------|-------------|--------------|
| Document generation | Create fake evidence, confirmations, or paperwork on demand | Spearphishing, Social Engineering |
| Instruction generation | Write clear step-by-step guides for victims to follow | All |
| Urgency escalation | Generate increasingly urgent follow-up messages | All |
| Proof fabrication | Create fake screenshots, transaction confirmations, investment returns | Social Engineering |
| Technical guidance | Walk victims through installing software or granting access | Social Engineering |
| Negotiation | Adjust demands based on victim responses | Social Engineering |

**Examples**:
- Generate a fake "wire confirmation" document when victim hesitates
- Write step-by-step instructions for a victim to install remote access software
- Create fake cryptocurrency investment dashboard showing profits

---

### Stage 6: Monetization — AI Automation Opportunities

| Capability | Description | Attack Types |
|------------|-------------|--------------|
| Mule recruitment | Generate job postings and correspondence for money mule recruitment | All |
| Cover story generation | Create explanations for mules to use if questioned | All |
| Path optimization | Analyze laundering routes for speed and detection risk | All |
| Communication | Handle mule coordination and instructions | All |

**Examples**:
- Write "payment processing job" listings to recruit unwitting money mules
- Generate scripts for mules to use at bank teller windows
- Create fake employment contracts for mules to show as documentation

---

### Stage 7: Evasion — AI Automation Opportunities

| Capability | Description | Attack Types |
|------------|-------------|--------------|
| Log analysis and cleanup | Identify and selectively remove traces of attacker activity from compromised systems | Spearphishing, Social Engineering |
| Anti-forensic scripting | Generate scripts to wipe artifacts, rotate credentials, and cover tracks | All |
| Detection evasion | Analyze security tool behavior and craft techniques to avoid triggering alerts | Spearphishing, Social Engineering |
| Infrastructure rotation | Automate teardown and replacement of compromised attack infrastructure | All |
| Counter-investigation | Analyze public breach disclosures and adapt evasion techniques accordingly | Spearphishing, Social Engineering |

**Examples**:
- Generate scripts to selectively clean server logs while preserving normal-looking activity
- Analyze a target org's security stack and recommend evasion approaches
- Automate domain and IP rotation to stay ahead of blocklists

---

## Summary: AI Impact by Attack Type

| Stage | Phishing | Spearphishing | Social Engineering |
|-------|----------|---------------|-------------------|
| 1. Setup | High (templates, translation) | High (documents, personas) | High (full persona creation) |
| 2. Reconnaissance | Low (batch enrichment) | High (deep research) | Medium-High (varies by targeting) |
| 3. First Turn | High (personalization at scale) | High (style matching) | Medium (initial contact) |
| 4. Ongoing Turns | Low (single message) | Medium (impersonation) | **Very High** (autonomous conversation) |
| 5. Execution | Low (automated capture) | Medium (document generation) | High (adaptive guidance) |
| 6. Monetization | Medium (mule recruitment) | Medium (mule recruitment) | Medium (mule recruitment) |
| 7. Evasion | Low (disposable infrastructure) | **Very High** (anti-forensics, detection evasion) | High (evidence management) |

**Key Insight**: LLMs provide the greatest force multiplication for **social engineering attacks** at the **ongoing turns stage**, where they can conduct sustained, adaptive conversations that previously required human operators. For **spearphishing**, the **setup** and **evasion** stages also show very high uplift potential, as LLMs can automate technically demanding tasks that traditionally require scarce, expensive expertise.

---

## Spear-Phishing Kill Chain: Detailed Cost-Benefit Analysis

This section provides a detailed phase-by-phase analysis of a spear-phishing attack, mapping traditional bottlenecks, LLM uplift potential, relevant evaluation benchmarks, and estimated cost impacts.

| Phase | Stage Description | Traditional Bottleneck | LLM Uplift Potential | Relevant Evals | Traditional Cost | AI-Assisted Cost | AI Token Usage | Potential Cost Reduction |
|-------|-------------------|----------------------|---------------------|---------------|-----------------|-----------------|---------------|------------------------|
| 1. Setup | Assemble technical tools, fake accounts, content strategies. Preliminary compromise of target infra. Prepare or acquire accounts/domains/resources | Technical skillset, zero-days, etc. for initial compromise | Very High: LLMs identifying zero-days or autonomously compromising target org infra would be very disruptive | cybench (cybersecurity offense capability), swe-bench (software/code knowledge) | Black market zero-day $10,000s+ | $100s-$1,000s in tokens, minimal compared to black-market cost | 20M-200M tokens | Very Significant |
| 2. Reconnaissance | Identify target org and high-value individuals | Labor-intensive intelligence gathering | High: Automated aggregation from web | Humanity's Last Exam for Computer and Browser Use (PhD-level research) | Human research hours, traditional MarTech, dark web lists ($100s-$1,000s) | $100s-$1,000s in tokens, API and data costs persist | 50M+ tokens (no clear upper bound) | Significant |
| 3. First Turn | Compose and deliver initial message | Compromising messaging systems, composing believable messages | Low: Already in wide use. Future risk of superhuman persuasion possible but difficult to evaluate | Will not evaluate, LLMs already at human parity | Minimal | Minimal | Minimal | Minimal |
| 4. Ongoing Turns | Continue to manipulate victim into performing target activity (link click, etc.) | Make target believe the impersonation/manipulation | High: Automated turn-by-turn response generation that could be highly believable and persuasive | soc-eng-bench (plausible multi-turn conversation capability while avoiding falsifiable claims) | High written-target-language-skill personnel ($100s-$1,000s) | $1s-$10s in tokens | 1M-10M tokens | Moderate |
| 5. Execution | Execute attack on target (credential harvesting, downloading malware, etc.) | Software engineering for custom exfiltration, MFA evasion, avoiding blocklists | Very High: LLMs can produce custom code at high velocity/low effort/low cost | swe-bench (agentic software capability) | Custom engineering, possibly outsourced ($1,000s) | $100s-$1,000s | 20M-200M tokens | Moderate |
| 6. Monetization | Use assets gained from previous step to get value | Converting credentials to value | Low: Requires technical execution, financial infrastructure | vending-bench (general business management and operations) | n/a (typically absorbed by management/overhead costs) | n/a (but concerned by risk of automated operational management) | n/a | n/a |
| 7. Evasion | Delay detection and destroy evidence to avoid enforcement and lower chances of recovery | Availability of very highly skilled cybersecurity personnel | Very High: High-skill personnel are costly and scarce | cybench (cybersecurity offense capability) | Highly-skilled IT cybersecurity ops personnel, traditional money laundering | $100s-$1,000s in tokens | 20M-200M tokens | Significant |

---

## Pig Butchering (Sha Zhu Pan) Kill Chain: Detailed Cost-Benefit Analysis

This section provides a phase-by-phase analysis of "Pig Butchering" investment scams — long-duration, relationship-based fraud operations that industrialize psychological manipulation. These operations combine romance scam tactics, fake investment platforms, and institutional-grade money laundering. The attack lifecycle is mapped to our standard 7-phase model, consolidating the report's 8 operational stages (Reconnaissance, Weaponization, Delivery, Grooming, The Hook, The Test Run/Slaughter, The Cut) into the unified framework.

**Key structural differences from spear-phishing:**
- **Setup** is far more capital-intensive, requiring fake trading platforms ($2.5k-$20k per kit), physical fraud compounds, and a "Crime-as-a-Service" supply chain
- **Ongoing Turns** spans weeks to months (vs. days for spear-phishing), making it the dominant cost center and the phase with the highest AI uplift potential
- **Execution** involves manipulating a fake platform backend ("God Mode") rather than delivering a technical payload
- **Monetization** operates through institutional-grade crypto laundering networks (Huione Guarantee, OTC brokers) with 15-40% fees

| Phase | Stage Description | Traditional Bottleneck | LLM Uplift Potential | Relevant Evals | Traditional Cost | AI-Assisted Cost | AI Token Usage | Potential Cost Reduction |
|-------|-------------------|----------------------|---------------------|---------------|-----------------|-----------------|---------------|------------------------|
| 1. Setup | Construct fake personas ("Character Sets"/Ren She), deploy fake trading platforms (MetaTrader clones with "God Mode" admin panels), establish SIM farms, acquire aged social media accounts, set up SCRM systems for managing victim portfolios at scale | Capital-intensive: physical fraud compounds, platform development, persona kits, trafficked labor force for 24/7 operations | High: Deepfake avatars (StyleGAN) bypass reverse-image search, voice cloning enables cross-gender impersonation, LLM-generated backstories, turnkey platform code generation | swe-bench (platform development), cybench (infrastructure evasion) | $10,000s+ (compound infrastructure, platform kits at $2.5k-$20k each, persona packages at $50-$200 each) | $100s-$1,000s in tokens for persona/content generation; platform and physical infra costs persist | 20M-200M tokens | Significant for content generation; physical infra costs unchanged |
| 2. Reconnaissance | Identify targets with financial liquidity and psychological vulnerability. Purchase leads from data brokers, scrape dating apps and social media, segment by net worth and life events (divorce, retirement, crypto interest) | Labor-intensive lead generation and scoring, data broker costs, manual social media research | High: Automated victim profiling from public social media, wealth estimation algorithms, propensity scoring for engagement likelihood | Humanity's Last Exam for Computer and Browser Use (PhD-level research capability) | $0.10-$5.00 per lead; bulk data purchases $100s-$1,000s; human research hours for high-value targeting | $100s-$1,000s in tokens; data broker and API costs persist | 50M+ tokens (no clear upper bound) | Significant |
| 3. First Turn | Initial contact via "wrong number" texts, dating app matches, or LinkedIn outreach. "Politeness pivot" when victim corrects the mistake. Migration off-platform to encrypted messaging (WhatsApp, Telegram) | High volume of SIM cards and aged accounts needed, bypassing platform spam filters and moderation algorithms | High: "Chatterbox" bots automate initial filtering and handshake, multilingual scripting via real-time translation enables global targeting from Southeast Asian compounds | Will not evaluate — initial contact is already commodity capability | <$0.01 per message via SIM farms and grey routes; aged accounts ~$0.10 each | Minimal token cost; telecom infrastructure costs persist | Minimal | Moderate (mainly throughput improvement, not cost per message) |
| 4. Ongoing Turns | Extended grooming phase (weeks to months): build emotional trust and dependency through daily conversation about life, family, hopes. Gradually pivot to investment topic. Includes "fattening" (emotional bonding), "hook" (introducing the platform), and "test run" (allowing small withdrawals to validate trust). SCRM systems manage shift handovers between operators to maintain persona continuity | Massive human labor: 12-16hr shifts in fraud compounds, maintaining persona consistency across multiple operators per victim, SCRM shift handover protocols. This is the dominant cost center of the entire operation | **Very High**: AI co-pilot generates emotionally resonant responses, maintains persona backstory consistency across months, tracks victim details (children's names, life events). Sentiment analysis monitors trust scores. Persuasion scripts handle objections to investment. Deepfake video calls verify persona identity. Decouples attack scale from linear human labor constraints | soc-eng-bench (multi-turn conversation capability, avoiding falsifiable claims over extended engagement) | High OpEx: compound maintenance, workforce (often trafficked), security, SCRM licensing — $1,000s+ per victim over weeks/months | $10s-$100s in tokens per victim over full engagement period | 10M-100M tokens per victim | **Very Significant** — transforms unit economics by replacing human labor with AI |
| 5. Execution | Maximum capital extraction via fake platform manipulation. "God Mode" backend shows fabricated profits to induce euphoria, then triggers margin calls and manufactured urgency. Generate legalese "tax" and "compliance" documents to justify withdrawal fees (10-30% of balance). Pressure victim to invest life savings, take loans, mortgage assets | Estimating victim's total extractable wealth, timing the "slaughter" correctly, generating convincing compliance documents for withdrawal fees | High: AI models victim's net worth from lifestyle clues in chat, behavioral alerts detect hesitation or suspicion, LLM generates convincing compliance/tax documentation for fee extraction | swe-bench (platform tooling), soc-eng-bench (persuasion under pressure) | N/A — this is the profit phase; requires admin platform infrastructure already built in Setup | $10s-$100s in tokens | 1M-10M tokens | Moderate |
| 6. Monetization | Launder funds through crypto mixing, peel chains, and "guarantee" marketplaces (Huione Guarantee). Off-ramp via corrupt OTC brokers. Deploy "asset recovery" re-scam teams to extract more from already-drained victims | Institutional-grade laundering infrastructure, 15-40% fees to laundering networks, cross-jurisdictional financial complexity, TRON/USDT transaction chains | Low: Financial infrastructure and broker networks dominate; AI provides marginal assistance with automated fund layering bots | vending-bench (operational management) | 15-40% of stolen funds as laundering fees; OTC broker commissions | n/a — financial infrastructure costs dominate | n/a | Minimal |
| 7. Evasion | Sever all contact ("The Cut"), disappear fake trading platform, rotate infrastructure (domains, hosting, SIM farms). Obstruct victim reporting via jurisdictional complexity (compounds in Laos/Myanmar/Cambodia). Deploy "asset recovery" scams as secondary extraction and misdirection | Cross-jurisdictional enforcement gaps, platform takedown speed, infrastructure rotation, destroying evidence across physical compounds | Moderate: Automated infrastructure rotation and domain generation, AI-generated cover stories for "asset recovery" re-scams, but physical compound evasion remains a non-AI problem | cybench (infrastructure evasion) | Absorbed into operational overhead; jurisdictional arbitrage is primary defense | $100s-$1,000s in tokens | 10M-50M tokens | Moderate — jurisdictional arbitrage and physical compounds are the primary evasion mechanism, not technical sophistication |
