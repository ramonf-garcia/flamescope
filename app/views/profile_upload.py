from flask import Blueprint, request 

from app.controllers.profile_upload import upload
from app import config

MOD_PROFILE_UPLOAD = Blueprint(
    'upload', __name__, url_prefix='/upload'
)


@MOD_PROFILE_UPLOAD.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        return upload(request)
    return f'''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name={config.FILE_FIELD}>
      <input type=submit value=Upload>
    </form>
    '''