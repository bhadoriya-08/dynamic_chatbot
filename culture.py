def culturally_adapt(text: str, language: str) -> str:
    if language == "hindi":
        return f"आपके प्रश्न के लिए धन्यवाद।\n\n{text}"

    elif language == "marathi":
        return f"तुमच्या प्रश्नाबद्दल धन्यवाद.\n\n{text}"

    elif language == "bengali":
        return f"আপনার প্রশ্নের জন্য ধন্যবাদ।\n\n{text}"

    else:
        return text
