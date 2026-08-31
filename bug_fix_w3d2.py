from transformers import AutoTokenizer

MODEL = "Qwen/Qwen2.5-1.5B-Instruct"
tok = AutoTokenizer.from_pretrained(MODEL)

def prompt_of_len(n_tokens: int) -> str:
    base = "Explain the following in detail.\n"
    filler_unit = "A data center serves many inference requests at once. "
    text = base
    while len(tok(text)["input_ids"]) < n_tokens:
        text += filler_unit
    ids = tok(text)["input_ids"][:n_tokens]
    assert len(ids) == n_tokens, f"only produced {len(ids)} tokens, wanted {n_tokens}"
    return tok.decode(ids)

for n in [128, 512, 2048, 4096]:
    p = prompt_of_len(n)
    actual = len(tok(p)["input_ids"])
    assert actual == n, f"prompt_of_len({n}) produced {actual} tokens"

print("GREEN CHECK: PASS")
