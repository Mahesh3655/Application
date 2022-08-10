from pymongo import MongoClient
import json
import random
client = MongoClient()
db=client.company
emp=db.Employees
for k in emp.find():
    print(type(k))

