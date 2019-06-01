# from pymongo import MongoClient

# client = MongoClient()

# db = client.cw_database

# collection = db.test_collection

# doc = {
#     "name": "test name"
# }

# # doc_id = collection.insert_one(doc).inserted_id
# # print(doc_id)

# print(collection.find_one({"name": "test name"}))

import pymongo
import time
import pprint
from pymongo import ReadPreference

# connect to replicaset servers ([host:port] (list), replicaSetName)
# connection = pymongo.MongoClient([
#     'localhost:27017',
#     'localhost:27018',
#     'localhost:27019'
# ],replicaset='replica1')

connection = pymongo.MongoClient("localhost:27010")

db = connection.get_database('cw', read_preference=ReadPreference.SECONDARY)
# connection.drop_database('cw')
# res = db.get_collection('guitars').insert_one({
#     "manufacturer": "Fender",
#     "model": "Strat12",
#     "price": 2550
# })

for i in range(100, 3000, 100):
    db.guitars.insert_one({
        "manufacturer": f"manufactirer Fender${i}",
        "model": f"telecaster {i}",
        "price": i
    })

# print(res)

for item in db.guitars.find():
    print(item)

# time.sleep(0.5)
# print(connection.nodes)
# collection = db.collection
# print(collection.read_preference)

# connection.drop_database('test')

# collection.insert_one(data)
# collection.find_one_and_delete({
#     'name': 'test2'
# })
counter = 0
# for item in db.guitars.find({"source": "thomann"}):
#     print(item)
#     counter+=1
# print(counter)
# for guitar in db.guitars.find().sort('price', 1):
#     print(guitar)