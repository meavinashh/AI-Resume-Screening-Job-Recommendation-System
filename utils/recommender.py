import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_jobs(skills):

    jobs = pd.read_csv("data/jobs.csv")

    resume_text = " ".join(skills)

    documents = [resume_text]

    documents.extend(jobs["Skills"].tolist())

    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(documents)

    similarity_scores = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    )

    jobs["Match %"] = similarity_scores[0] * 100

    jobs = jobs.sort_values(
        by="Match %",
        ascending=False
    )

    return jobs[["Job Title", "Match %"]]