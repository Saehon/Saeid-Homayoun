# Replication gate checklist

For each main claim, record:

| Gate | Evidence to record | Pass condition |
| --- | --- | --- |
| Provenance | repository/file, commit or modified date, license, access | A reviewer can identify the exact inputs |
| Environment | language/runtime, package lock, OS/container, seed | The run environment is reproducible or its limits are explicit |
| Sample | unit, period, filters, attrition, exclusions | Counts reconcile from raw input to analysis sample |
| Measures | variable map, codebook, transformations, missingness | Treatment, outcome, and controls match the manuscript |
| Execution | command/entry point, logs, failures, run time | The stated pipeline completes or failure is documented |
| Match | estimate/table/figure, tolerance, discrepancy explanation | Result matches the pre-specified tolerance |
| Stress test | temporal holdout, placebo/negative control, alternatives | Material fragility is disclosed, not silently selected away |

Use `R0` through `R4` from the skill instructions. “Available online” is not a pass condition.

