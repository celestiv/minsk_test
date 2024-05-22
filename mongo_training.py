import os
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

env = load_dotenv(find_dotenv())  # подгружаем переменные из файла .env
password = os.environ.get("MONGODB_PWD")
host = os.environ.get("MONGODB_HOST")
port = os.environ.get("MONGODB_PORT")

connection_string = f"{host}:{port}"
client = MongoClient(connection_string)  # установка соединения с сервером
# dbs = client.list_database_names()  # получаем список баз данных на сервере
# print("databases:", dbs)

local_db = client.local
# collections = local_db.list_collection_names()
# print("collections: ", collections)


def insert_test_doc():
    collection = local_db.test  # mongo автоматически создает коллекцию, если ее нет
    test_document = {
        "name": "Alex",
        "age": "21"
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    # добавляем данные для теста в коллекцию и сохраняем id
    print("inserted id: ", inserted_id)


def find_key():
    collection = local_db.test
    people = collection.find_one({"name": "Alex"})
    print(people)


if __name__ == "__main__":
    # insert_test_doc()
    find_key()