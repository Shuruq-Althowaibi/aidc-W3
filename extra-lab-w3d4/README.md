# Extra Lab W3D4: Quantisation Drift Audit

## Overview
Automated regression audit comparing `Qwen2.5-1.5B-Instruct` (fp16) vs `Qwen2.5-1.5B-Instruct-AWQ` (4-bit) across four key evaluation categories:
- JSON Validity
- Factual Recall
- Length Boundedness
- Refusal Behavior

## Results
- Tolerance: 10.0 percentage points
- Regression Status: Passed audit within acceptable tolerance.
- Status: GREEN CHECK: PASS
