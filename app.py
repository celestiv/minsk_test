import os
from bson.objectid import ObjectId
from flask import Flask, request
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import memory_test

env = load_dotenv(find_dotenv())  # подгружаем переменные из файла .env
password = os.environ.get("MONGODB_PWD")
host = os.environ.get("MONGODB_HOST")
port = os.environ.get("MONGODB_PORT")

connection_string = f"{host}:{port}"
client = MongoClient(connection_string)
local_db = client.local
collection = local_db.minsk_collection

app = Flask(__name__)


@app.route('/name', methods=['POST'])
def create_object():
    data = request.json
    inserted_object = collection.insert_one(data)
    if inserted_object:
        return str(inserted_object.inserted_id), 201
    else:
        return "Creation failed", 400


@app.route('/name', methods=['GET'])
def read_object():
    key = request.json.get("name")
    result = collection.find_one({"name": key})
    if result:
        return str(result), 200
    else:
        return "Object not found", 404


@app.route('/name', methods=['PUT'])
def update_object():
    data = request.json
    key = data.get("name")
    value = collection.find_one({"name": key})
    result = collection.update_one({"_id": value["_id"]}, {"$set": data})
    if result.modified_count == 1:
        return "Object updated successfully", 200
    else:
        return "Object not found", 404


@app.route('/name', methods=['DELETE'])
def delete_by_name():
    data = request.json
    name = data.get("name")
    result = collection.delete_one({"name": name})
    if result:
        return str(result), 200
    else:
        return "Object not found", 404


@app.route('/names', methods=['GET'])
def read_all():
    result = collection.find()
    if result:
        return list(str(res) for res in result), 200
    else:
        return "Object not found", 404


@app.route('/alarm', methods=['GET'])
def handle_alarm():
    message = memory_test.send_alarm()
    return message, 200


if __name__ == '__main__':
    app.run()
