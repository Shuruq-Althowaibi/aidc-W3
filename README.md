# Week 3 Day 5: The Benchmark Harness & Capacity Note

## Overview
Evaluated full throughput and p95 latency scaling across multiple concurrency levels [1, 2, 4, 8, 16] using the automated benchmark harness against the locked `Qwen2.5-1.5B-Instruct-AWQ` build.

## Key Deliverables & Verifications
- **Benchmark Suite Output**: `bench_report.json`
- **Knee Identification**: `knee.json`
- **Capacity Analysis Note**: `capacity-note.md`
  - Target SLO: p95 latency <= 3.0s
  - Identified Knee Concurrency
- **Status**: GREEN CHECK: PASS
