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

def extract_skills(text):

    text = text.lower()

    skills_found = []

    for skill in skills_db:
        if skill in text:
            skills_found.append(skill)

    return skills_found