#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_script import Manager
import os, string, random

app = Flask(__name__)

ALLOWED_EXTENSIONS = ['jpg','jpeg','gif', 'png']
UPLOAD_PATH = os.path.join(os.getcwd(), 'static/upload')

# upload size
app.config['MAX_CONTENT_LENGTH'] = 1024*1024*64
manager = Manager(app)

def random_name(suffix, length=32):
    str = string.ascii_letters+string.digits
    return "".join(random.choice(str) for i in range(length))+'.' + suffix

# add route
@app.route('/upload/', methods=['GET','POST'])
def upload():
    if request.method == 'POST' and request.files.get('file'):
        file = request.files.get('file')
        filename = file.filename
        suffix = filename.split('.')[-1]
        if suffix in ALLOWED_EXTENSIONS:
            filename = random_name(suffix)
            print(UPLOAD_PATH)
            file.save(os.path.join(UPLOAD_PATH, filename))
    return render_template('template.html')

if __name__== '__main__':
    manager.run()
