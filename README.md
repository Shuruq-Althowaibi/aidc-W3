# Week 3 Day 4: Quantise and Lock the Model

## Overview
Deployed and evaluated **4-bit AWQ** quantized model serving (`Qwen/Qwen2.5-1.5B-Instruct-AWQ`) using vLLM with fused AWQ kernels and Hermes tool-call parsing.

## Key Deliverables & Verifications
- **Model Lock**: `model-lock.md`
  - **Locked Model**: `Qwen/Qwen2.5-1.5B-Instruct-AWQ`
  - **Parser**: `--tool-call-parser hermes`
  - **Flags**: `--dtype half --max-model-len 4096 --gpu-memory-utilization 0.85 --quantization awq --enable-auto-tool-choice`
- **Function Calling Smoke Test**: `smoke_result.json`
  - Score: `10/10` (Passed tool-calling gate & distractor compliance).
- **Extra Lab W3D4**: `extra-lab-w3d4/`
  - Automated 20-prompt quantization drift audit across JSON validity, factual recall, length bounds, and refusal behavior (`regression_report.json`).
- **Bug Lab W3D4**: `bug_lab_w3d4_diagnosis.md`
  - Diagnosed bitsandbytes CUDA version mismatch and silent CPU fallback; resolved via dynamic package unpinning.

## Verification
- **Status**: GREEN CHECK: PASS
