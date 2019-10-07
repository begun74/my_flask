import sys
import subprocess
from flask import Flask , jsonify , request

persons =  [
   {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
   },
   {
    "firstName": "Micky",
    "lastName": "Mouse",
    "hobbies": ["running", "sky diving"],
    "age": 25,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        }
    ]
   }

]

app = Flask(__name__)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route("/")
def home():
    return "<h2>Hello!</h2> <p><font color='red'>This is  11.Docker.Lading! </font> </p>"

@app.route("/get")
def get():
    return "<h2>Get request</h2>"

@app.route("/person/<int:id>" , methods=['GET'])
def getPerson(id):
    person = {}
    try:
     person = persons[id]
    except:
     person = {}
    return person

@app.route("/persons")
def getPersons():
    return jsonify({'persons': persons})

@app.route("/quit")
def goodBye():
    shutdown_server()


if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=80, debug=False)
