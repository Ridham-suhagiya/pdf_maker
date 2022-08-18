from re import L
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>hello world</h1>"

@app.route('/home')
def first():

    if request.form.get('submit') == 'submit':
        f = request.file('img')
        f.save('','screenshot.png')
        return render_template('templates/success.html')

    return render_template('templates/image_input.html')