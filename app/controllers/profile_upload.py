from os.path import join
from flask import request, abort, redirect, url_for
from werkzeug.utils import secure_filename
from app import config

def valid_file(filename):
    extension = filename.split('.')[-1]
    return extension in config.ALLOWED_EXTENSIONS

def upload(request):
    uploaded_profile = request.files.get(config.FILE_FIELD)
    if uploaded_profile:
        try:
            filename = uploaded_profile.filename
            if valid_file(filename):
                uploaded_profile.save(join(config.PROFILE_DIR, filename))
                return redirect(url_for('root'))
            else:
                print('Invalid filename received')
        except IOError:
            print('Failed to save file locally')
            abort(500)
    abort(400)

