from webchat import app
from flask import render_template


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

