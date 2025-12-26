import json   # 👈 ADD THIS

CS_CATEGORIES = ["cs.AI", "cs.LG", "cs.CL", "cs.CV", "cs.SE"]

def load_cs_papers(path, limit=500):
    papers = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            paper = json.loads(line)
            if any(cat in paper["categories"] for cat in CS_CATEGORIES):
                papers.append({
                    "title": paper["title"],
                    "abstract": paper["abstract"],
                    "categories": paper["categories"]
                })
            if len(papers) >= limit:
                break
    return papers
