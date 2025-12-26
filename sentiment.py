from transformers import pipeline

# Load once (cached by Streamlit)
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def detect_sentiment(text: str) -> str:
    result = sentiment_analyzer(text)[0]
    label = result["label"]
    score = result["score"]

    if label == "POSITIVE" and score > 0.6:
        return "positive"
    elif label == "NEGATIVE" and score > 0.6:
        return "negative"
    else:
        return "neutral"
