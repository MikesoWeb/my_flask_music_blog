
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():

    return render_template('index.html')

@app.route('/audio')
def hello_audio():

    return render_template('audio.html', l=l)

import os
path = '/music'
l = os.listdir(path)


@app.route('/blog')
def hello():
    return render_template('blog.html')




