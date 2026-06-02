# AI Resume Screening & Job Recommendation System

## Overview

An AI-powered Resume Screening and Job Recommendation System that helps candidates analyze resumes, calculate ATS scores, identify missing skills, predict suitable job roles, and receive job recommendations using Machine Learning and NLP techniques.

## Features

* Resume PDF Upload
* Resume Text Extraction
* Skill Extraction
* ATS Score Calculation
* Missing Skills Detection
* Resume vs Job Description Matching
* Job Recommendation Engine
* Resume Role Classification
* Top 3 Role Predictions
* Interactive Streamlit Dashboard

## Machine Learning Techniques

* TF-IDF Vectorization
* Logistic Regression
* Cosine Similarity
* Text Classification
* Natural Language Processing (NLP)

## Tech Stack

### Frontend

* Streamlit

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorizer
* Logistic Regression

### Data Processing

* Pandas
* NumPy
* PyPDF2

## Project Structure

AI-Resume-Screening-System/
│
├── data/
├── models/
├── utils/
├── app.py
├── requirements.txt
└── README.md

## Installation

```bash
git clone <repository-url>
cd AI-Resume-Screening-System

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python models/train_model.py

python -m streamlit run app.py
```

## Future Improvements

* Deep Learning Based Resume Classification
* Resume Ranking System
* Candidate Recommendation Engine
* LLM-based Resume Feedback
* Cloud Deployment
