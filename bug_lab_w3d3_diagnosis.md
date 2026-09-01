# Bug Lab W3D3: Config Compatibility Gap

## Three Diagnostic Facts
1. **Model Config**: `Qwen2.5-1.5B-Instruct` uses newer `rope_scaling` schema (`rope_type: default`) without a standalone `factor` key.
2. **Engine Parser**: Older vLLM releases (`<=0.6.2`) expect legacy `rope_scaling` dictionary layout and raise `KeyError: 'factor'`.
3. **Issue Nature**: Version compatibility mismatch between modern Hugging Face configs and engine-side parsing logic.

## Resolution
Upgraded to a compatible vLLM release that correctly handles modern RoPE schemas.

## Verification
- Endpoint: `GET /v1/models` returns `200 OK`
- Status: GREEN CHECK: PASS
