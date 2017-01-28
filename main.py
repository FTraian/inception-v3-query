import os
import inception.classify_image as classifier

from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename


# webapp
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp'
app.secret_key = 'some_dirty_secret'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filename)
            classifier_response = classifier.run_inference_on_image(filename)
            os.remove(filename)
            return render_template('index.html', response=classifier_response)
    return render_template('index.html')
