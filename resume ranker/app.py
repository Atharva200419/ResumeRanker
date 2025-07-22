from flask import Flask, render_template, request
from utils import rank_resumes
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'resumes'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    jd = request.form['jd']
    files = request.files.getlist('resumes')

    resume_paths = []
    for file in files:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        resume_paths.append(path)

    results = rank_resumes(jd, resume_paths)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
