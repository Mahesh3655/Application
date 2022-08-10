from flask import Flask,make_response,abort
import json

from pymongo import MongoClient

app = Flask(__name__)

@app.route("/",methods=['GET'])
def gcff():
    client = MongoClient()
    db = client.company
    e = db.Employees
    lst =[]
    for i in e.find():
        lst.append(i)
    return json.dumps(lst)

@app.route("/getid/<int:id>",methods=['GET'])
def get_emp_id(id):
    client = MongoClient()
    db = client.company
    e = db.Employees
    lst =[]
    for i in e.find():
        lst.append(i)
    employee = []

    for emp in lst:
        if emp["_id"] == id:
            employee.append(emp)
    if len(employee) == 0:
        abort(404)
    return json.dumps(employee)

@app.errorhandler(404)
def notfound(error):
    return make_response("Not Found",404)



app.run(port=5050)
