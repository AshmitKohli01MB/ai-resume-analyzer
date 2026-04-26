from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_feedback(resume_text, job_description, match_result):
    prompt = f"""
    You are a professional resume reviewer and career coach.
    
    Analyze this resume against the job description and provide detailed feedback.
    
    RESUME:
    {resume_text[:2000]}
    
    JOB DESCRIPTION:
    {job_description[:1000]}
    
    MATCH SCORE: {match_result['score']}%
    MATCHED KEYWORDS: {', '.join(match_result['matched_keywords'])}
    MISSING KEYWORDS: {', '.join(match_result['missing_keywords'])}
    
    Please provide:
    1. Overall Assessment (2-3 sentences)
    2. Top 3 Strengths of this resume
    3. Top 3 Areas for Improvement
    4. Missing keywords to add
    5. One specific tip to improve chances of getting this job
    
    Keep the feedback clear, specific and actionable.
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()

def get_general_feedback(resume_text):
    prompt = f"""
    You are a professional resume reviewer.
    
    Analyze this resume and provide detailed feedback:
    
    RESUME:
    {resume_text[:2000]}
    
    Please provide:
    1. Overall Assessment (2-3 sentences)
    2. Top 3 Strengths
    3. Top 3 Areas for Improvement
    4. Suggested skills to add
    5. Formatting and structure tips
    
    Keep feedback clear, specific and actionable.
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()