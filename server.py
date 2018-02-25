from clarifai import rest
from clarifai.rest import ClarifaiApp
from secrets import CLARIFAI_KEY

from flask import Flask
import pymongo
import json


app = Flask(__name__)

@app.route('/')
def hello():
    clarifai = ClarifaiApp(api_key=CLARIFAI_KEY)
    model = clarifai.models.get('color')
    response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

    if 'Red' not in response:
        return json.dumps({'inventory_status': 'poor'})
    else:
        return json.dumps({'inventory_status': 'ok'})

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
