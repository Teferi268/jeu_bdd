import os 
from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri) 
db = client["heroes"]
collection_heroes = db["heroes"]
collection_monster = db["monstres"]


