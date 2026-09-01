# Extra Lab W3D3: Load Shedding Under Overload

## Overview
Demonstrates client-side admission control (load shedding) using an asyncio semaphore to protect p95 latency under heavy burst traffic.

## Key Takeaway
- **Unbounded Burst (n=50)**: High p95 latency due to unbounded queuing.
- **Shedded Burst (cap=8)**: Protects accepted requests' p95 latency by rejecting excess requests immediately.
- **Status**: GREEN CHECK: PASS
