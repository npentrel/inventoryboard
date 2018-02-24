from flask import Flask
from secrets import DB_USER, DB_PASSWORD, DB_URL, DB_PORT
import pymongo

connection = pymongo.MongoClient(DB_URL, DB_PORT)
db = connection["inventory-dashboard"]
db.authenticate(DB_USER, DB_PASSWORD)

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/insert/<name>')
def hello_name(name):
    resp = db.organizations.insert({"name": name, "chain_segments": [{"suppliers": [{"name": "Apple"}]}, {"factories": [{}]}, {"stores": [{"name": "{}'s store".format(name)}]}]})
    return "Onject: {}!".format(resp)


if __name__ == '__main__':
    app.run()
