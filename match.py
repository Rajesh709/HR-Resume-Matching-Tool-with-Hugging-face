from sentence_transformers import SentenceTransformer, util
import os

model = SentenceTransformer('all-MiniLM-L6-v2')

def read_texts(folder):
    texts = {}
    for file in os.listdir(folder):
        if file.endswith('.txt'):
            with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
                texts[file] = f.read()
    return texts

def load_job_description(path="job_description.txt"):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def match_resumes(jd_text, resumes):
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    results = []

    for name, text in resumes.items():
        embedding = model.encode(text, convert_to_tensor=True)
        score = util.cos_sim(jd_embedding, embedding).item()
        results.append((name, score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results
