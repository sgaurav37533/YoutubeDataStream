from asynchat import simple_producer
from ensurepip import bootstrap
from auth import *
from kafka import *
from Producer import *
import pandas as pd
import seaborn as snb
import json
from pymongo import *

client = MongoClient('localhost:27017')
collection = client.db.customers

consumer = KafkaConsumer('values',bootstrap_servers=['localhost:9092'])

for message in consumer:
    message = message.values
    collection.insert_one(message)