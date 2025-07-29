# 
# Rejeshkm.709@gmail.com
# ** AI-Powered Resume Screening Tool
A smart and simple web application to automatically match resumes against a job description using transformer-based sentence embeddings. Built using Streamlit and SentenceTransformers.

🚀 Features
📌 Upload and process multiple .txt resumes.

📌 Match resumes with job description using semantic similarity.

📌 View ranked results based on AI-calculated similarity scores.

📌 Fast, lightweight, and easy to run locally.

# 🧠 Tech Stack
Frontend/UI: Streamlit

Backend: Python

ML Model: all-MiniLM-L6-v2 from HuggingFace's SentenceTransformers

Libraries: streamlit, sentence-transformers, torch

# ***🗂️ Project Structure ****
python
Copy
Edit
HR-Resume-Matching-Tool-with-Hugging-face/
│
├── app.py                      # Streamlit web interface
├── match.py                    # Resume matching logic
├── job_description.txt         # Example job description
├── resumes/                    # Folder with sample resumes (.txt format)
├── requirements.txt            # All dependencies
└── README.md                   # You're here!

⚙️ Setup Instructions
# ✅ 1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/HR-Resume-Matching-Tool-with-Hugging-face.git
cd HR-Resume-Matching-Tool-with-Hugging-face
# ✅ 2. Create and Activate a Virtual Environment (Optional)
bash
Copy
Edit
python3 -m venv myenv
source myenv/bin/activate   # On Windows: myenv\Scripts\activate
# ✅ 3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt not available, manually install:

bash
Copy
Edit
pip install streamlit sentence-transformers
# ✅ 4. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
Open the browser at: http://localhost:8501

📂 How to Use
Edit job_description.txt with your job description.

Place all resume files (in .txt format) inside the resumes/ folder.

Click the "Match Resumes" button on the app.

View ranked list of top matching candidates.


