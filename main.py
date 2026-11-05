"""AI Refusal Tone Softener"""

def soften_refusal(raw_refusal):
    if "as an ai language model" in raw_refusal.lower():
        return "I am unable to perform that action directly, but I can assist with related architecture and design."
    return raw_refusal

if __name__ == "__main__":
    print("[RUN] Refusal Tone Softener...")
    softened = soften_refusal("As an AI language model, I cannot do that.")
    print(f"[OK] Softened Response: '{softened}'")
