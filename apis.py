import flask
import json

from pymongo import MongoClient

app = flask.Flask(__name__)

@app.route("/",methods=['GET'])
def gcff():
    client = MongoClient()
    db = client.company
    e = db.Employees
    lst =[]
    for i in e.find():
        lst.append(i)
    return json.dumps(lst)
        

app.run(port=5050)
