from flask import Flask,render_template
from flask_restful import Api
from api.admin import Admin
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)
api = Api(app)
@app.route('/')
def hello():
    return render_template('index.html')
api.add_resource(Admin,'/userid')
app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
     app.run()