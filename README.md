# 🤖 LLM-Powered Resume Analyzer

An AI-powered resume analyzer that reads your resume, matches it with job descriptions, and provides detailed feedback using LLaMA 3.

## 🌐 Live Demo
👉 https://ai-resume-analyzer.onrender.com

## 🚀 Features
- Upload resume in PDF or TXT format
- Match resume with any job description
- Get a match score percentage
- See matched and missing keywords
- Get detailed AI-powered feedback and suggestions

## 🛠️ Tech Stack
- Python
- Flask
- Groq API (LLaMA 3)
- PyPDF2
- python-dotenv
- Gunicorn

## ⚙️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/AshmitKohli01MB/ai-resume-analyzer.git
cd ai-resume-analyzer

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate.bat

### 3. Install dependencies
pip install -r requirements.txt

### 4. Add API Key
Create a .env file:
GROQ_API_KEY=your-groq-api-key-here

### 5. Run the project
python app.py

### 6. Open in browser
http://127.0.0.1:5000

## 📁 Project Structure
- app.py — Flask backend and API routes
- resume_parser.py — Extracts text from PDF/TXT resumes
- job_matcher.py — Matches resume keywords with job description
- ai_feedback.py — Generates AI feedback using Groq LLaMA 3
- templates/index.html — Frontend UI
- requirements.txt — Project dependencies

## 🔄 How It Works
1. Upload your resume (PDF or TXT)
2. Paste a job description (optional)
3. Click Analyze Resume
4. Get match score and AI feedback instantly

## 📊 Example Output
- Match Score: 75%
- Matched Keywords: python, flask, git, api
- Missing Keywords: docker, aws
- AI Feedback: Detailed suggestions to improve your resume

## 👨‍💻 Author
Ashmit Kohli
- GitHub: https://github.com/AshmitKohli01MB
- Email: kohliashmit94@gmail.com
- Project 1: https://github.com/AshmitKohli01MB/ai-email-automation
