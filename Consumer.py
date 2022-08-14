from asynchat import simple_producer
from ensurepip import bootstrap
from auth import *
from kafka import *
from Producer import *
import pandas as pd
import seaborn as snb
import json
from pymongo import *

consumer = KafkaConsumer('values',bootstrap_servers=['localhost:9092'])

client = MongoClient('localhost:27017')
collection = client.values.values

for message in consumer:
    message = message.value
    collection.insert_one(message)