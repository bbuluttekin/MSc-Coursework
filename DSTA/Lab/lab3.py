import pymongo as pm
import json

with open("DSTA/Lab/mongo.json") as f:
    url = json.load(f)


c = pm.MongoClient(url["url"])

print(c.admin)
