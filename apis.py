from flask import Flask,make_response,abort,request,jsonify
import json

from pymongo import MongoClient

app = Flask(__name__)

def database():
    client = MongoClient()
    db = client.company
    e = db.Employees
    lst =[]
    for i in e.find():
        lst.append(i)
    return lst
@app.route("/",methods=['GET'])
def gcff():
    lst = database()
    return json.dumps(lst)

@app.route("/getid/<int:id>",methods=['GET'])
def get_emp_id(id):
    lst = database()
    employee = []

    for emp in lst:
        if emp["_id"] == id:
            employee.append(emp)
    if len(employee) == 0:
        abort(404)
    return jsonify(employee)

@app.errorhandler(404)
def notfound(error):
    return make_response("Not Found",404)
@app.errorhandler(400)
def badrequest(error):
    return make_response("bad Request",400)

@app.route("/update/<int:id>",methods=['PUT'])
def update_employee(id):
    client = MongoClient()
    db = client.company
    e = db.Employees
    data = json.loads(request.get_data())

    e.update_one({"_id":id},{"$set":{"name":data["name"]}})
    return data["name"]

@app.route("/insert",methods=["POST"])
def insert_Employee():
    client = MongoClient()

app.run()
