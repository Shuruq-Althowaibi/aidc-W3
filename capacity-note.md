# Capacity Note: Qwen2.5-1.5B-Instruct-AWQ

## Benchmark Configuration
- **Model ID**: Qwen/Qwen2.5-1.5B-Instruct-AWQ
- **Hardware**: NVIDIA T4 GPU (16GB)
- **Engine**: vLLM (PagedAttention + Continuous Batching)
- **Quantization**: AWQ (4-bit)

## Capacity & SLO Findings
- **Target p95 SLO**: 3.0 seconds
- **Knee Concurrency**: 16
- **Throughput at Knee**: 1143.0 tokens/s
- **p95 Latency at Knee**: 1.458 seconds
- **Limiting Factor Family**: Memory-bandwidth bound during decode phase, transitioning to queue overhead under high concurrency.

## Operational Recommendation
The production endpoint can safely promise concurrency up to 16 while strictly maintaining our 3.0s p95 latency SLO.
