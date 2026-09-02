# Bug Lab W3D4: CUDA Binary Mismatch in Quantizer

## Diagnostic Findings
1. **Platform CUDA Version**: Runtime uses modern CUDA versions (e.g., CUDA 12.8 / 13.0).
2. **Binary Availability**: Pinned `bitsandbytes==0.44.1` lacks compiled binaries for newer CUDA targets (`libbitsandbytes_cuda128.so`), triggering silent CPU fallback.
3. **Cascade Failure**: CPU fallback tries to reach deprecated `triton.ops`, causing runtime crash.

## Resolution
Upgraded to dynamic / floating minor pin (`bitsandbytes>=0.45` or `-U bitsandbytes`) to automatically resolve prebuilt wheels matching the host CUDA environment, followed by a session restart.

## Verification
- Model loaded on GPU (`torch.cuda.memory_allocated() > 0`)
- Status: GREEN CHECK: PASS
