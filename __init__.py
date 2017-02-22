from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from se.settings import *
from se.Routes.Lead.routes import lead 

app = Flask(__name__)
CORS(app)

app.register_blueprint(lead)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run(port=5001,debug=True)
