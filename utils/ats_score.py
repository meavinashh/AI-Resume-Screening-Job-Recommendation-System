skills_db = [
    "python",
    "sql",
    "power bi",
    "excel",
    "react",
    "javascript",
    "html",
    "css",
    "nodejs",
    "express",
    "mongodb",
    "scikit-learn",
    "pandas",
    "numpy",
    "machine learning",
    "deep learning"
]

def calculate_ats_score(found_skills):

    total_skills = len(skills_db)

    matched_skills = len(found_skills)

    score = (matched_skills / total_skills) * 100

    return round(score, 2)