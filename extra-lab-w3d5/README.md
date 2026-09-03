# Extra Lab W3D5: Cost per Million Tokens & Scale-Out Breakeven

## Overview
Calculated operational cost per million tokens across concurrency levels and modeled scale-out replica planning using measured knee capacity to preserve target p95 SLO.

## Key Findings
- **Knee Concurrency**: Selected based on target SLO (p95 <= 3.0s).
- **Economic Insight**: Concurrency past the knee flatters cost-per-token on paper while violating production latency guarantees.
- **Scale-Out Strategy**: Horizontal scaling at the knee concurrency maintains latency bounds under higher aggregate load.
- **Report**: `cost_report.json`
- **Status**: GREEN CHECK: PASS
