
def retrieve(query, index, texts, model, k=5):
    q_emb = model.encode([query])
    distances, ids = index.search(q_emb, k)
    return [texts[i] for i in ids[0]]
