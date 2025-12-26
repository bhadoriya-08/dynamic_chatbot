# backend/llm.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def generate_answer(context, question):
    prompt = f"""
Context:
{context}

Question:
{question}

Explain clearly for a computer science student.
"""
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(
        **inputs,
        max_new_tokens=200
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
