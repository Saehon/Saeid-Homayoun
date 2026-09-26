# GAN / Synthetic-Adversarial Layer for Lemon-ICFR-US

## Architectural placement
This is a **supporting Technology-layer capability**, not a permanent core and not an evidence authority.

The Mother repository already identifies GAN Lab / synthetic-data tooling as a reference for adversarial and synthetic scenario generation. Lemon uses that idea only behind an adapter and only in WATCH/EVALUATE/SANDBOX until frozen benchmarks justify promotion.

## ICFR use cases
Synthetic generation can create controlled test populations for:
- revenue cut-off exceptions;
- missing/late approvals;
- duplicate or overridden journal entries;
- segregation-of-duties conflicts;
- reconciliation breaks;
- access-control anomalies;
- management-review-control edge cases;
- rare material-weakness patterns;
- population/sampling stress tests.

## Evidence firewall
Synthetic data must carry:
- `evidence_class = synthetic`;
- generator/provider/version;
- configuration and random seed where relevant;
- source schema;
- transformation lineage;
- scenario purpose;
- explicit statement that the output is not company evidence.

A real-world ICFR conclusion cannot be supported solely by synthetic evidence.

## Blind benchmark rule
Generator agents must not have access to private gold labels for promotion-grade evaluation. Synthetic training/scenario data, benchmark prompts and private gold keys must remain separated.

## Provider strategy
Potential implementations may include GANs, diffusion/tabular generators, rule-based generators or other synthetic-data methods. Lemon is intentionally **method-neutral**; the scientific/evidence contract remains fixed while the generator is replaceable.

## Current state
`SANDBOX`

No claim is made that a GAN model has been trained or scientifically validated for Lemon merely because this layer exists.
