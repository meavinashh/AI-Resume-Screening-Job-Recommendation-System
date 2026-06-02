from utils.skill_extractor import extract_skills
from utils.recommender import recommend_jobs
from utils.ats_score import calculate_ats_score
from utils.missing_skills import get_missing_skills

sample_resume = """
Dhruva Singh

Skills:
Python
SQL
Power BI
React
MongoDB
NodeJS
"""

skills = extract_skills(sample_resume)

print("Skills Found:")
print(skills)

ats_score = calculate_ats_score(skills)

print("\nATS Score:")
print(f"{ats_score}%")

missing_skills = get_missing_skills(skills)

print("\nMissing Skills:")
print(missing_skills)

print("\nRecommended Jobs:")
print(recommend_jobs(skills))