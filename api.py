import flask
import json

f = open('sample.json')
data = json.load(f)

app = flask.Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello World"

@app.route('/books/' ,methods=['GET'])
def h():
    return data
app.run()


