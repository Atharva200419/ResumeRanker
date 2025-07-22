import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text(file_path):
    doc = fitz.open(file_path)
    return " ".join(page.get_text() for page in doc)

def rank_resumes(job_description, resume_paths):
    docs = [job_description]
    names = []

    for path in resume_paths:
        docs.append(extract_text(path))
        names.append(path.split('/')[-1])

    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform(docs)

    jd_vector = vectors[0]
    resume_vectors = vectors[1:]

    scores = cosine_similarity(jd_vector, resume_vectors).flatten()
    ranked = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)
    return ranked
