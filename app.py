from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def get_index_html():
    return render_template('index.html')