"""
server.py

This module sets up a Flask web application with two routes:
1. '/' - Renders the index.html template.
2. '/emotionDetector/<path:text>' - Analyzes the text and
   searches for words related to emotions.
"""

from flask import Flask, render_template
from EmotionDetection.services.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def get_index_html():
    """Render the main page"""
    return render_template('index.html')

@app.route('/emotionDetector/<path:text>')
def analyze_text(text):
    """Receives the text parameter and analyzes it to identify the emotion"""
    analysis_result = emotion_detector(text)
    return analysis_result

if __name__ == "__main__":
    app.run(debug=True)
