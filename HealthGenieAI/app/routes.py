from flask import render_template, request, current_app as app
from .main import analyze_input

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form['user_input']
    results = analyze_input(user_input)
    return render_template('result.html', results=results)