# Source and rights gate — FT50 auditing replication
**Status:** authoritative source metadata inspected; empirical replication not claimed.

## Source A: JAR article and corrections
- Yang Bao, Bin Ke, Bin Li, Julia Yu, and Jie Zhang (2020), "Detecting Accounting Fraud in Publicly Traded U.S. Firms Using a Machine Learning Approach", *Journal of Accounting Research* 58(1), 199–235. DOI 10.1111/1475-679X.12292.
- 2022 corrigendum DOI 10.1111/1475-679X.12454; treat corrigendum as a mandatory separate methodological review.
- Official author repository: https://github.com/JarFraud/FraudDetection
- Observed verified Git blob hashes: run_RUSBoost.m = 2ae5c04c54ddee2ecd999817e4ab21ad211ecc78; data_reader.m = de15ae2e5d6af43edabbdfb5bcecc8f2cee743f3; evaluate.m = 10764403e3ca9a7a3eefada9e292b39f0a3fb7ce.
- Author's README describes a final public dataset and MATLAB 2020b code (Windows 10); original COMPUSTAT fundamental inputs commercially sourced; AAER material assembled from SEC releases and CFRM.
- The original baseline is RUSBoost with 300 trees, MinLeafSize=5, LearnRate=0.1, RatioToSmallest=[1,1]; test years 2003–2014; each year's training ends at year_test-2 (two-year gap). MATLAB code also excludes matching serial PAAER frauds from positive training labels. See original run_RUSBoost.m before claiming replication.
- The author repository does not by itself grant blanket redistribution or commercial reuse rights to original commercial source data. No dataset copied to NAAIL.
- No MATLAB available in the current development session. **Original empirical replication status: BLOCKED.**

## Source B: Paper2Agent
- Miao et al. (2026), Nature, DOI 10.1038/s41586-026-11044-y; public upstream https://github.com/jmiao24/Paper2Agent.
- Upstream skill: https://github.com/jmiao24/Paper2Agent/blob/main/skills/paper2agent/SKILL.md
- Upstream converts paper PDFs and/or author code into independently verified skills and MCP tools using a supported coding agent host, shell and subagent execution; NAAIL implements a purpose-built read-only MCP proof of concept, **not** upstream full conversion.

## Source C: audit standards
- PCAOB AS 3101: https://pcaobus.org/oversight/standards/auditing-standards/details/AS3101. CAM requires materiality, audit committee communication, especially challenging/subjective/complex judgment; a missing CAM cannot be characterized as audit failure from a numerical risk score.

## Historic open data and outcome design
- Existing 10-company NAAIL sample: MSFT AAPL GOOGL AMZN NVDA META JPM WMT XOM TSLA — exploratory convenience sample, not validated material-weakness or fraud risk training panel; ten clean 2025/26 observations alone cannot estimate binary classification performance.
- Real ICFR positive and negative cases and independently dated fraud/restatement outcomes must be assembled before training. Declare labels, information availability dates, exclusion rules and usage licenses.
- CAM text must not leak into before-audit risk prediction. Crosswalk CAM by auditor report date and account/topic, not by firm-year alone.
- Use chronological held-outs, auditor/industry holdouts, calibration, base-rate metrics and preregistered model selection. No post-hoc search to maximize significance.

## Dataset manifest schema
Required: source_owner, source_uri, retrieved_at, access_rights, version/git_sha, source_file_sha256, firm_id, fiscal_period, first_public_timestamp, label_definition, label_observation_timestamp, transformation_code_commit, usage_restrictions.
