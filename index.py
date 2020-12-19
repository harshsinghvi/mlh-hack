import flask 
import json 
import os
from flask_pymongo import PyMongo
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from flask import render_template
import creds

def get_stack_from_db():
    stackdb=mongo.db.stack.find({"name" :"stack0"})[0]
    stack._stack['data'] = stackdb['data']
    stack._data_validate()
    return "OK",200

def dbupdate():
    temp={
        "$set":{
        "data":stack.stack(),
        "size":stack.size()
        }
    }
    try :
        mongo.db.stack.update_one({"name":"stack0"},temp)
    except: 
        return "Internal Server Error With DB", 500
    return "DB UPDATE OK",200

#  APP CONFIG 
app = flask.Flask(__name__)
CORS(app, support_credentials=True)
app.config["DEBUG"] = False
MONGO_DB_URI = os.environ['MONGO_DB_URI']
app.config['MONGO_URI'] = MONGO_DB_URI
mongo = PyMongo(app)
db=mongo.db.hackathon

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/stack',methods=['GET'])
def view_stack():
    get_stack_from_db()
    return json.dumps(stack.raw_stack()),200

@app.route('/pop',methods=['GET'])
def pop():
    stack.pop()
    try :
        dbupdate()
    except: 
        return "Internal Server Error With DB", 500
    return {"POP":"OK"},200

@app.route('/push',methods=['GET'])
def push():
    if 'data' not in request.args:
        return "Bad Request Please Pass the data in the Quary Parameters",400
    stack.push(request.args['data'])
    try :
        dbupdate()
    except: 
        return "Internal Server Error With DB", 500
    return {"PUSH":" OK"},200

@app.route("/dispatch-top-5", methods=['GET'])
def dispatch_top_five():
    data=[]
    d= db.consignments.find()
    try:
        for i in range(6):
            data[i]=d[i]
    except:
        pass
    return data


@app.route("/delivered-top-5", methods=['GET'])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
