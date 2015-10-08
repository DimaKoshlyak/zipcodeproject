from flask import Flask
from flask import render_template
from pymongo import MongoClient
import pymongo
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'zipcode'
COLLECTION_NAME = 'code'
MAX_CITIES=20
FIELDS = {"city" : True, "pop" : True, "_id" : False}

@app.route("/")
def index():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    cities = collection.find(projection=FIELDS).sort('pop', direction=pymongo.DESCENDING).limit(MAX_CITIES)

    output = open('static/export.json','w')

    list_cities = []
   
    for city in cities:
      list_cities.append(city)
   
    output.write(dumps(list_cities))    

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
