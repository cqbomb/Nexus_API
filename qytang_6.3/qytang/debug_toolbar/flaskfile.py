from flask import Flask, make_response
from flask import request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = '1231231esdfsdfsdfsdfsdfsdf234234234'
toolbar = DebugToolbarExtension(app)

@app.route('/', methods=['GET'])
def index():
    return "<body>welcome to qytang</body>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)