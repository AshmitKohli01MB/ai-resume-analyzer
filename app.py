from flask import Flask, render_template, request, jsonify
from resume_parser import parse_resume
from job_matcher import match_resume_with_job
from ai_feedback import get_ai_feedback, get_general_feedback
import os
import traceback

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create uploads folder if not exists
os.makedirs('uploads', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Get uploaded resume file
        resume_file = request.files.get('resume')
        job_description = request.form.get('job_description', '')

        if not resume_file:
            return jsonify({'error': 'No resume uploaded'}), 400

        # Save uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
        resume_file.save(file_path)

        print(f"File saved: {file_path}")

        # Parse resume
        resume_text = parse_resume(file_path)
        print(f"Resume text extracted: {len(resume_text)} chars")

        if job_description.strip():
            # Match with job description
            match_result = match_resume_with_job(resume_text, job_description)
            print(f"Match score: {match_result['score']}")
            # Get AI feedback
            feedback = get_ai_feedback(resume_text, job_description, match_result)
        else:
            match_result = {
                'score': 'N/A',
                'matched_keywords': [],
                'missing_keywords': [],
                'resume_keywords': []
            }
            feedback = get_general_feedback(resume_text)

        print(f"Feedback generated successfully")

        # Clean up uploaded file
        if os.path.exists(file_path):
            os.remove(file_path)

        return jsonify({
            'success': True,
            'match_score': match_result['score'],
            'matched_keywords': match_result['matched_keywords'],
            'missing_keywords': match_result['missing_keywords'],
            'feedback': feedback
        })

    except Exception as e:
        print(f"ERROR: {traceback.format_exc()}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)