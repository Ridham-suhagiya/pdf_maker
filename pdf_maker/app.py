from lambdaMaker import lambda_maker
from urllib import request
from flask import Flask,render_template, request,url_for
import logging
from templates import *
import os
from helper import checker


app = Flask(__name__)




app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/')
def hello():
    return render_template('success.html')

@app.route('/home', methods=['GET', 'POST'])
def first():
    

    if request.method == 'POST':
        images = request.files.getlist('img')
        checker('images')
        for image in images:
            name = image.filename
            
            image.save(os.path.join('images', f'{name}'))
        response = lambda_maker()
        if response == True:
            return render_template('pdf_done.html')
        else:
            print(response)
            return '<h1> Something went wrong </h1>'

    return render_template('image_input.html')

if __name__ == '__main__':
    app.run()
    
    logging.basicConfig(filename='record.log', level=logging.DEBUG)