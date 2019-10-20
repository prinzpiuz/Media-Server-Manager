import os
from pathlib import *
from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
import configparser
import shutil
from hurry.filesize import size, alternative

config = configparser.ConfigParser()
config.read('config.ini')

ALLOWED_EXTENSIONS = set(['mp4', 'avi', 'mkv', 'srt'])

file_path = config['DEFAULT']['MOVIES']

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


def contextUpdate():
    path_obj = Path(file_path)
    file_list = [x.name for x in path_obj.iterdir() if x.is_file()]
    context = {'file_list': file_list}
    return context


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def system_statics():
    usage = shutil.disk_usage(config['DEFAULT']['MOVIES'])
    return {'total':size(usage[0], system=alternative),
        'used':size(usage[1], system=alternative),
        'free':size(usage[2], system=alternative)}
    


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
                    flash('completed uploading {0}'.format(file.filename))
                else:
                    flash("{0}'s format not supported".format(file.filename))
            return redirect(request.url)
    disk_usage = system_statics()
    context = {'tv': config['DEFAULT']['TV'], 'movies': config['DEFAULT']['MOVIES'],'disk':disk_usage }
    return render_template("file.html", **context)


@app.route('/files', methods=['GET', 'POST'])
def files():
    if request.method == 'GET':
        context = contextUpdate()
        return render_template("listfile.html", **context)
    if request.method == 'POST':
        context = contextUpdate()
        file_list = request.form.getlist('file_list')
        for file in file_list:
            path = PurePosixPath(file_path).joinpath(file)
            rem_file = Path(path)
            rem_file.unlink()
            flash("sucessfully deleted {0}".format(file))
        return render_template("listfile.html", **context)




if __name__ == "__main__":
    app.run(host='0.0.0.0')