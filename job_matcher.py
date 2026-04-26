def extract_keywords(text):
    # Common tech keywords to look for
    keywords = [
        "python", "java", "sql", "machine learning", "deep learning",
        "flask", "django", "api", "git", "docker", "aws", "azure",
        "data analysis", "nlp", "tensorflow", "pytorch", "llm",
        "automation", "rest api", "javascript", "html", "css",
        "communication", "teamwork", "leadership", "problem solving"
    ]
    
    text_lower = text.lower()
    found = [kw for kw in keywords if kw in text_lower]
    return found

def match_resume_with_job(resume_text, job_description):
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)
    
    # Find matching keywords
    matched = [kw for kw in job_keywords if kw in resume_keywords]
    missing = [kw for kw in job_keywords if kw not in resume_keywords]
    
    # Calculate match score
    if len(job_keywords) == 0:
        score = 0
    else:
        score = round((len(matched) / len(job_keywords)) * 100, 2)
    
    return {
        'score': score,
        'matched_keywords': matched,
        'missing_keywords': missing,
        'resume_keywords': resume_keywords
    }