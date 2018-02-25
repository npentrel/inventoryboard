from clarifai import rest
from clarifai.rest import ClarifaiApp
from secrets import CLARIFAI_KEY
from werkzeug.utils import secure_filename
from flask import Flask, request, redirect, url_for

import pymongo
import json
import os

UPLOAD_FOLDER = '/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# clarifai = ClarifaiApp(api_key=CLARIFAI_KEY)
# model = clarifai.models.get('color')
# file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# image = ClImage(file_obj=open('/home/user/image.jpeg', 'rb'))
# response = model.predict([image])
# if 'Crimson' in response:
#     return json.dumps({'inventory_status': 'poor'})
# if 'Olive' in response:
#     return json.dumps({'inventory_status': 'ok'})
# else:
#     return json.dumps({'inventory_status': 'good'})

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
