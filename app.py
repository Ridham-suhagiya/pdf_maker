from pdf_maker.lambdaMaker import lambda_maker
from urllib import request
from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return {'message':'hello world'}

@app.route('/home')
def first():
    lambda_maker()
    if request.form.get('submit') == 'submit':
        f = request.file('img')
        f.save('','screenshot.png')
        return render_template('success.html')

    return render_template('image_input.html')

if __name__ == '__main__':
    app.run()