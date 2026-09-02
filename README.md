# Week 3 Day 1: Profile Inference

## Overview
Profiled and analyzed single-request LLM inference stages (prefill vs. decode) on an NVIDIA T4 GPU using a baseline Hugging Face inference setup.

## Key Deliverables & Verifications
- **Inference Profiling**:
  - Measured Time-To-First-Token (TTFT) across variable prompt lengths (prefill phase: compute-bound).
  - Measured Inter-Token Latency (ITL) across generation lengths (decode phase: memory-bandwidth bound).
- **Baseline Measurements**: Documented baseline throughput and single-stream latency profile.
- **Verification**: Verified profiling outputs and runtime metrics.

## Verification
- **Status**: GREEN CHECK: PASS
