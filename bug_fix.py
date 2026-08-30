import torch, gc
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

MODEL = "Qwen/Qwen2.5-1.5B-Instruct"

def resident_vram_gb() -> float:
    torch.cuda.synchronize()
    return torch.cuda.memory_reserved() / (1024 ** 3)

def load(dtype: str):
    if dtype == "fp16":
        return AutoModelForCausalLM.from_pretrained(
            MODEL, torch_dtype=torch.float16, device_map="cuda")
    if dtype == "int8":
        qc = BitsAndBytesConfig(load_in_8bit=True)
        return AutoModelForCausalLM.from_pretrained(
            MODEL, quantization_config=qc, device_map="cuda")
    if dtype == "int4":
        qc = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)
        return AutoModelForCausalLM.from_pretrained(
            MODEL, quantization_config=qc, device_map="cuda")
    raise ValueError(dtype)

results = {}
for dtype in ["fp16", "int8", "int4"]:
    model = load(dtype)
    vram = resident_vram_gb()
    results[dtype] = round(vram, 2)
    print(f"{dtype}: {results[dtype]} GB")
    
    # Bug Fix: delete in the caller's scope
    del model
    gc.collect()
    torch.cuda.empty_cache()

fp16_gb = results["fp16"]
int8_gb = results["int8"]
int4_gb = results["int4"]

assert int8_gb < fp16_gb, "int8 should be smaller than fp16"
assert int4_gb < int8_gb, "int4 should be smaller than int8"
print("GREEN CHECK: PASS")
