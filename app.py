# app.py
import streamlit as st
from load_data import load_cs_papers
from embed_store import build_faiss, model
from retriever import retrieve
from summarizer import summarize
from llm import generate_answer
from sentiment import detect_sentiment
from response_style import style_response
from language import detect_language
from translator import translate
from culture import culturally_adapt

st.set_page_config(page_title="arXiv CS Expert Chatbot")

st.title("📚 arXiv Computer Science Expert Chatbot")

query = st.text_input("Ask a research-level question:")

@st.cache_resource
def setup():
    papers = load_cs_papers("data/arxiv-metadata-oai-snapshot.json", limit=500)
    index, texts = build_faiss(papers)
    return index, texts

index, texts = setup()

if query:
    # 1. Detect language
    user_lang = detect_language(query)
    # 2. Retrieve relevant content (multilingual embeddings)
    retrieved = retrieve(query, index, texts, model)
    summary = summarize(retrieved[0])
    # 3. Generate answer in English
    english_answer = generate_answer(summary, query)
    # 4. Translate answer
    translated_answer = translate(english_answer, user_lang)
    final_answer = culturally_adapt(translated_answer, user_lang)

    st.subheader("Detected Language")
    st.write(user_lang.capitalize())

    st.subheader("Answer")
    st.write(final_answer)

