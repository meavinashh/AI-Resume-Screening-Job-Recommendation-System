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

def get_missing_skills(found_skills):

    missing_skills = []

    for skill in skills_db:
        if skill not in found_skills:
            missing_skills.append(skill)

    return missing_skills