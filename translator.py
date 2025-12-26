from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "facebook/nllb-200-distilled-600M"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

LANG_CODE = {
    "english": "eng_Latn",
    "hindi": "hin_Deva",
    "marathi": "mar_Deva",
    "bengali": "ben_Beng"
}

def translate(text: str, target_lang: str) -> str:
    if target_lang == "english":
        return text

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True
    )

    outputs = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(
            LANG_CODE[target_lang]
        ),
        max_new_tokens=300
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
