def style_response(answer: str, sentiment: str) -> str:
    if sentiment == "positive":
        return f"😊 Glad to hear your interest!\n\n{answer}"

    elif sentiment == "negative":
        return (
            "I understand this might feel confusing or frustrating. "
            "Let me explain it clearly step by step.\n\n"
            f"{answer}"
        )

    else:  # neutral
        return answer
