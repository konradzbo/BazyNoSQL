import uuid

import pymongo
import redis as redis
from bson import ObjectId
from ecart.ecart.ecart import Cart
from elasticsearch import Elasticsearch
from cassandra.cluster import Cluster



connection = pymongo.MongoClient("localhost", 27017)

database = connection['Sklep_muzyczny']

collection = database['Pracownik']
collection1 = database['Klient']
collection2 = database['Produkt']
print("Database connected")

#collection2.insert_one({"_id": 1,"Nazwa": 'Klasyczna gitara',"Model": 'C40',"Marka": 'Yamaha',"Cena": 554,"Ilość": 100 })

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

r = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

cluster = Cluster()
session = cluster.connect('historia')


#print ("%s, %s, %s, %s, %s" %(user.numer_zakupu, user.klient, user.produkt, user.cena, user.ilosc))
#cluster = Cluster()
#session = cluster.connect('mykeyspace')
#session.set_keyspace('historia')

#session.execute("""INSERT INTO users (name, credits, user_id)VALUES (%s, %s, %s)""",("John O'Reilly", 42, uuid.uuid1()))

#rows = session.execute('SELECT name, age, email FROM users')


def insert_data(data):
    document = collection.insert_one(data)
    return document.inserted_id


def update_or_create(document_id, data):
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data}, upsert=True)
    return document.acknowledged


def get_single_data(document_id):
    data = collection.find_one({'_id': ObjectId(document_id)})
    return data

def get_multiple_data():
    data = collection.find()
    return list(data)

def update_existing(document_id, data):
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data})
    return document.acknowledged


def remove_data(document_id):
    document = collection.delete_one({'_id': ObjectId(document_id)})
    return document.acknowledged



def get_multiple_data1():
    data = collection1.find()
    return list(data)

def get_multiple_data2():
    data = collection2.find()
    return list(data)


connection.close()