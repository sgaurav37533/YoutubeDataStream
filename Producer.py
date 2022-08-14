from asynchat import simple_producer
from ensurepip import bootstrap
import googleapiclient.discovery
import time
from auth import *
from kafka import *
import pandas as pd
import seaborn as snb
import json

producer= KafkaProducer(bootstrap_servers='localhost:9092')
topic_name= 'Twitter'
channel_id='UCBJycsmduvYEL83R_U4JriQ'

def getChannelStatus():
    
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_id)
    record = request.execute()
    rec=json.dumps(record).encode('utf-8')
    producer.send('values', rec)

getChannelStatus()#batch records

def PeriodicWork(interval):
    while True:
        getChannelStatus()#streaming records
        time.sleep(interval)

PeriodicWork(60*0.1)