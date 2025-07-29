
import streamlit as st
from main import read_texts, load_job_description, match_resumes

st.title("🔍 HR Resume Matching Tool")

jd = load_job_description()
resumes = read_texts("resumes")

st.subheader("📄 Job Description")
st.text_area("Job Description", jd, height=200)

if st.button("Match Resumes"):
    st.write("Matching resumes...")
    results = match_resumes(jd, resumes)

    st.subheader("📋 Top Matching Resumes")
    for i, (name, score) in enumerate(results):
        st.write(f"{i+1}. **{name}** — Similarity Score: `{score:.2f}`")
