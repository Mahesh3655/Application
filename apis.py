from flask import Flask,make_response,abort,request,jsonify
import json

from pymongo import MongoClient

app = Flask(__name__)

def database():
    client = MongoClient('mongodb://3.86.159.183:27017/company')
    db = client.company
    e = db.Employees
    lst =[]
    for i in e.find():
        lst.append(i)
    return lst
@app.route("/",methods=['GET'])
def all_Employees():
    lst = database()
    return jsonify(lst)

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
    return make_response("Bad Request",400)

@app.route("/update/<int:id>",methods=['PUT'])
def update_employee(id):
    client = MongoClient('mongodb://3.86.159.183:27017/company')
    db = client.company
    e = db.Employees
    data = json.loads(request.get_data())

    e.update_one({"_id":id},{"$set":{"name":data["name"]}})
    return data["name"]

@app.route("/insert",methods=["POST"])
def insert_Employee():
    lst = database()
    data = json.loads(request.get_data())
    employee = {}
    employee["_id"] = lst[-1]["_id"] +1
    employee["name"] = data["name"]
    employee["role"] = data["role"]
    employee["age"] = data["age"]
    employee["salary"] = data["salary"]
    client = MongoClient('mongodb://3.86.159.183:27017/company')
    db = client.company
    e = db.Employees
    e.insert_one(employee)
    return "done"

@app.route("/delete/<int:id>",methods=['DELETE'])
def delete_Employee(id):
    lst = database()
    employee = []
    for emp in lst:
        if emp["_id"] == id:
            employee.append(emp)
    if len(employee) == 0:
        abort(404)

    client = MongoClient('mongodb://3.86.159.183:27017/company')
    db = client.company
    e = db.Employees
    e.delete_one({"_id" : id})
    return "done"



app.run()
