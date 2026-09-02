# AIDC Bootcamp - Week 3: LLM Inference & Serving Architecture

## Overview
Comprehensive implementation, benchmarking, and optimization of large language model (LLM) inference pipelines on NVIDIA T4 GPU infrastructure. Covers prefill/decode profiling, KV-cache dynamics, engine replacement with vLLM, continuous batching, and 4-bit AWQ model locking.

---

## Daily Branch Navigation & Deliverables

### [Day 1: Profile Inference (`w3d1`)](https://github.com/Shuruq-Althowaibi/aidc-W3/tree/w3d1)
- Profiled TTFT (prefill / compute-bound) and ITL (decode / memory-bound) stages.
- Established baseline latency and throughput benchmarks.
- **Status**: GREEN CHECK: PASS

### [Day 2: Inference Anatomy & KV Cache (`w3d2`)](https://github.com/Shuruq-Althowaibi/aidc-W3/tree/w3d2)
- Calculated theoretical vs. allocated KV-cache VRAM utilization (`kv_check.json`).
- Profiled static batching ceiling and CUDA OOM boundaries (`baselines.json`).
- Extra Lab: Multi-tenant memory fragmentation analysis.
- Bug Lab: Dynamic sequence padding and shape mismatch resolution (`bug_fix_w3d2.py`).
- **Status**: GREEN CHECK: PASS

### [Day 3: Engine Swap with vLLM (`w3d3`)](https://github.com/Shuruq-Althowaibi/aidc-W3/tree/w3d3)
- Migrated engine to vLLM featuring PagedAttention and continuous batching.
- Completed A/B benchmark sweep across concurrencies [1, 4, 8] (`ab_report.json`).
- Extra Lab: Client-side admission control and load shedding (`extra-lab-w3d3/shedding_report.json`).
- Bug Lab: Resolved RoPE scaling schema compatibility gap (`bug_lab_w3d3_diagnosis.md`).
- **Status**: GREEN CHECK: PASS

### [Day 4: Quantise & Lock the Model (`w3d4`)](https://github.com/Shuruq-Althowaibi/aidc-W3/tree/w3d4)
- Served and locked 4-bit AWQ quantized build (`Qwen/Qwen2.5-1.5B-Instruct-AWQ`).
- Integrated Hermes tool-call parser (`--tool-call-parser hermes`).
- Function-calling smoke test validated with a score of 10/10 (`smoke_result.json`).
- Model lock specification finalized (`model-lock.md`).
- Extra Lab: Automated 20-prompt quantization drift audit (`extra-lab-w3d4/regression_report.json`).
- Bug Lab: Diagnosed and resolved CUDA mismatch and silent CPU fallback (`bug_lab_w3d4_diagnosis.md`).
- **Status**: GREEN CHECK: PASS

---

## Hardware & Environment
- **Accelerator**: NVIDIA T4 GPU (16GB VRAM)
- **Environment**: Linux / Google Colab T4 Runtime
- **Primary Engine**: vLLM (v0.6.3+)
