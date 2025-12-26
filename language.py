from langdetect import detect

LANG_MAP = {
    "en": "english",
    "hi": "hindi",
    "mr": "marathi",
    "bn": "bengali"
}

def detect_language(text: str) -> str:
    try:
        lang = detect(text)
        return LANG_MAP.get(lang, "english")
    except:
        return "english"
