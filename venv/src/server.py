from flask import Flask, Response, render_template, send_file
import os
import sys

app = Flask(__name__)

@app.route('/')
def index():
    # return send_file('\\views\index.html')
    return render_template('index.html')

