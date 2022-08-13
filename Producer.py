from ensurepip import bootstrap
import tweepy
import time
from kafka import KafkaProducer
from auth import *

producer= KafkaProducer(bootstrap_servers='localhost:9092')
topic_name= 'Twitter'

def getTwitterData():
    res=api.search_tweets(q="Java OR Python OR CPP",lang="en")
    for i in res:
        record=''
        record+=str(i.user.id_str)
        record+=';'
        record+=str(i.user.followers_count)
        record+=';'
        record+=str(i.user.retweet_count)
        record+=';'
        record+=str(i.user.favourite_count)
        record+=';'

        producer.send(topic_name,str.encode(record))


getTwitterData()#batch records

def PeriodicWork(interval):
    while True:
        getTwitterData()#streaming records
        time.sleep(interval)

PeriodicWork(60*0.1)