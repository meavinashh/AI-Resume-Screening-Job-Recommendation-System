import streamlit as st

from utils.role_predictor import predict_role
from utils.job_matcher import match_resume_to_job
from utils.pdf_reader import extract_text
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from utils.missing_skills import get_missing_skills
from utils.recommender import recommend_jobs

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening & Job Recommendation System")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=200
)

if uploaded_file is not None:

    resume_text = extract_text(uploaded_file)

    match_score = None

    if job_description.strip():
        match_score = match_resume_to_job(
            resume_text,
            job_description
        )

    skills = extract_skills(resume_text)

    ats_score = calculate_ats_score(skills)

    if match_score is not None:

        st.subheader("📊 Resume vs Job Match")

        st.metric(
            "Match Score",
            f"{match_score}%"
        )

        st.progress(int(match_score))

    missing_skills = get_missing_skills(skills)

    recommended_jobs = recommend_jobs(skills)

    st.success("Resume uploaded successfully!")

    predicted_role, top_roles = predict_role(
        resume_text
    )

    st.subheader("🎯 ATS Score")

    st.metric("ATS Score", f"{ats_score}%")

    st.progress(int(ats_score))

    if ats_score >= 80:
      st.success("Excellent Resume ✅")

    elif ats_score >= 60:
      st.warning("Good Resume ⚠️")

    else:
      st.error("Resume Needs Improvement ❌")

    st.subheader("🤖 AI Role Prediction")

    st.success(
        f"Predicted Role: {predicted_role}"
    )

    st.dataframe(top_roles)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🛠 Extracted Skills")
        st.write(skills)

    with col2:
        st.subheader("❌ Missing Skills")
        st.write(missing_skills)

    st.subheader("💼 Recommended Jobs")
    st.dataframe(recommended_jobs)