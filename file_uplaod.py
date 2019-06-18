import os
from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['mp4', 'avi', 'mkv', 'srt'])

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        folder = request.form.get('folder')
        files = request.files.getlist('file')
        is_file = bool(request.files.getlist('file')[0])
        if is_file:
            for file in files:
                if allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(folder, filename))
            flash('completed file upload')
            return redirect(request.url)
    return render_template("file.html")