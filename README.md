# Week 3 Day 2: Inference Anatomy & KV Cache

## Overview
Investigated the memory anatomy of transformer inference, focusing on KV-cache memory allocation, batching limits, and out-of-memory (OOM) failure boundaries under static batching.

## Key Deliverables & Verifications
- **KV Cache Allocation & Math**: `kv_check.json`
  - Computed theoretical vs. allocated KV-cache VRAM usage per sequence length.
- **Baseline Batching Profiles**: `baselines.json`
  - Evaluated static batching throughput ceilings on standard PyTorch / Hugging Face servers before hitting CUDA OOM.
- **Extra Lab W3D2**: `extra-lab-w3d2/`
  - Memory fragmentation and multi-tenant resource contention experiments.
- **Bug Lab W3D2**: `bug_fix_w3d2.py`
  - Diagnosed and resolved static padding waste and dynamic sequence dimension mismatches.

## Verification
- **Status**: GREEN CHECK: PASS
