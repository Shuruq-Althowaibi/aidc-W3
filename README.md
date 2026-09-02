# Week 3 Day 3: Engine Swap with vLLM

## Overview
Replaced the naive Hugging Face static inference server with a high-throughput **vLLM** engine utilizing PagedAttention and continuous batching on an NVIDIA T4 GPU.

## Key Deliverables & Verifications
- **A/B Benchmark Report**: `ab_report.json`
  - Validated throughput speedups at concurrencies [1, 4, 8].
  - Engine continuous batching verified.
- **Extra Lab W3D3**: `extra-lab-w3d3/`
  - Client-side load shedding under burst traffic (50 requests vs. cap 8).
  - Protected p95 latency for admitted requests.
- **Bug Lab W3D3**: `bug_lab_w3d3_diagnosis.md`
  - Diagnosed and resolved the `KeyError: 'factor'` RoPE scaling compatibility gap between Qwen2.5 configs and legacy vLLM parsers.

## Verification
- **Status**: GREEN CHECK: PASS
