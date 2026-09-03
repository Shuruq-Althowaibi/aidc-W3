# Bug Lab W3D5: Cold-Start Benchmarking Confound

## Root Cause
The initial loop benchmark lacked a warm-up call. The first tested configuration (`context=128`) absorbed one-time initialization costs (CUDA kernel JIT compilation, PyTorch memory caching allocator init, and cuBLAS handles), rendering the shortest prompt artificially 4x slower than mid-sized sequences.

## Solution
Introduced an explicit discarded warm-up call with `torch.cuda.synchronize()` prior to starting latency measurements. This ensures all initial kernel compilation and GPU memory paths are warm before evaluating real test vectors.

## Verification
- Monotonic latency scaling confirmed: `results[128] < results[512] < results[2048]`
- Status: GREEN CHECK: PASS
