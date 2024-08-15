from flask import Flask, render_template
from .services.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def get_index_html():
    return render_template('index.html')

@app.route('/analyze/<path:text>')
def analyze_text(text):
    analysis_result = emotion_detector(text)
    return analysis_result

if __name__ == "__main__":
    app.run(debug=True)
