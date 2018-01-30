from flask import Flask, render_template, request, redirect, url_for, flash
from flask_restful import Api
from api.admin import Admin

from werkzeug.contrib.fixers import ProxyFix
from upload import upload
app = Flask(__name__)
api = Api(app)


# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def hello():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')



api.add_resource(Admin, '/userid')
app.wsgi_app = ProxyFix(app.wsgi_app)


app.register_blueprint(upload, url_prefix='/upload')

if __name__ == '__main__':
    app.run(debug=True)
