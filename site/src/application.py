from flask import (Flask, render_template)
app = Flask(__name__, template_folder="templates")

APPLICATION_NAME = "Sentiment Analysis"


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/development')
def development():
    return render_template('development.html')


@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

