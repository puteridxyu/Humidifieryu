# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
from operator import truediv
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import json
import pyrebase

# dependencies for HTTP
# Dependencies

from threading import Timer
import json
import sqlite3
#import requests

THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'enb0BsXvhFOR5q8uOML'   #Device 1
ACCESS_TOKEN2 = 'SDxFz3SIxIy1wRArznjd'   #Device 2
sensor_data  = {'temperature': 0, 'humidity': 0, 'waterLevel': 0}
sensor_data2 = {'temperature': 0, 'humidity': 0,'waterLevel': 0}

# on_connect function
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully.")
    elif rc == 1:
        print("Connection refused, incorrect protocol version")
    elif rc == 2:
        print("Connection refused, invalid client identifier")
    elif rc == 3:
        print("Connection refused, server unavailable")
    elif rc == 4:
        print("Connection refused, bad username or password")
    elif rc == 5:
        print("Connection refused, not authorised")
    else:
        print("Connection failed. rc= "+str(rc))

#on_publish if you are the publisher
def on_publish(client, userdata, mid):
    print("Message "+str(mid)+" published.")

#on_subscribe if you are the subscriber
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe with mid "+str(mid)+" received.")

#on_message if you are the broker
def on_message(client, userdata, msg):
    print("Message received on topic "+msg.topic+" with QoS "+str(msg.qos)+" and payload "+msg.payload)


MQTT_Broker = "192.168.43.67"
MQTT_Port = 1883
Keep_Alive_Interval = 10
MQTT_Topic = "fk/#"

dbName = "Humidifier.db"
conn = sqlite3.connect(dbName)
#c = conn.cursor()
dataValue =0
temp=0
hum=0
lev=0

#firebase
firebaseConfig = {"apiKey": "AIzaSyB60uZB5Y_85DJ-TxL358-YmLm49V5BLaw",
                "authDomain": "humidifieryu.firebaseapp.com",
                "databaseURL": "https://humidifieryu-default-rtdb.asia-southeast1.firebasedatabase.app",
                "projectID": "humidifieryu",
                "storageBucket": "gs://humidifieryu.appspot.com/"}
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()
database = firebase.database()

#'Suhu_Dalam' is the client name
client = mqtt.Client("Humidifier")
thingsboardClient = mqtt.Client()
thingsboardClient2 = mqtt.Client()


#provide uname and pwd
client.username_pw_set(username="ayu", password="ayu123")
thingsboardClient.username_pw_set(ACCESS_TOKEN)
thingsboardClient2.username_pw_set(ACCESS_TOKEN2)


 # Assign event callbacks
thingsboardClient.on_connect = on_connect
thingsboardClient.on_publish = on_publish
thingsboardClient.on_subscribe = on_subscribe
thingsboardClient.on_message = on_message

# Assign event callbacks
thingsboardClient2.on_connect = on_connect
thingsboardClient2.on_publish = on_publish
thingsboardClient2.on_subscribe = on_subscribe
thingsboardClient2.on_message = on_message

# create mqtt connection to broker
thingsboardClient.connect(THINGSBOARD_HOST, 1883, 60)
thingsboardClient2.connect(THINGSBOARD_HOST, 1883, 60)

# Connect
client.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

#Subscribe to all Sensors at Base Topic
def on_connect(mosq, obj,flag, rc):
    client.subscribe(MQTT_Topic, 0)

#To print the subscribed message
def on_message(mosq, obj, msg):
    print("\n")
    print("Message received on topic "+str(msg.topic)+" with QoS "+str(msg.qos)+" and payload "+str(msg.payload))
    dataValue = msg.payload.decode('UTF-8')
    c = conn.cursor()
    database.child("DB Humidifier")
    
    if msg.topic == "fk/humidifier1/temperature":
        c.execute("INSERT INTO temperature1 (DateTime, Temperature1) VALUES (?,?)", ('2', dataValue))
        sensor_data['temperature'] = dataValue
        data = {"Temperature": dataValue}

    elif msg.topic == "fk/humidifier1/humidity":
        c.execute("INSERT INTO humidity1 (DateTime, Humidity1) VALUES (?,?)", ('2', dataValue))
        sensor_data['humidity'] = dataValue
        data = {"Humidity": dataValue}

    elif msg.topic == "fk/humidifier1/waterLevel":
        c.execute("INSERT INTO waterLevel1 (DateTime, WaterLevel1) VALUES (?,?)", ('2', dataValue))
        sensor_data['waterLevel'] = dataValue
        data = {"WaterLevel": dataValue}

    elif msg.topic == "fk/humidifier2/temperature":
        c.execute("INSERT INTO temperature2 (DateTime, Temperature2) VALUES (?,?)", ('2', dataValue))
        sensor_data2['temperature'] = dataValue
        data = {"Temperature2": dataValue}

    elif msg.topic == "fk/humidifier2/humidity":
        c.execute("INSERT INTO humidity2 (DateTime, Humidity2) VALUES (?,?)", ('2', dataValue))
        sensor_data2['humidity'] = dataValue
        data = {"Humidity2": dataValue}

    elif msg.topic == "fk/humidifier2/waterLevel":
        c.execute("INSERT INTO waterLevel2 (DateTime, WaterLevel2) VALUES (?,?)", ('2', dataValue))
        sensor_data2['waterLevel'] = dataValue
        data = {"WaterLevel2": dataValue}

    #firebase
    database.set(data)
    print(data)

    conn.commit()
    thingsboardClient.publish('v1/devices/me/telemetry',json.dumps(sensor_data),1)
    thingsboardClient2.publish('v1/devices/me/telemetry',json.dumps(sensor_data2),1)
    #make_request()
    
    print ("the data value = ", dataValue)
    print("message topic=",msg.topic)
    print("message qos=",msg.qos)
    print("message retain flag=",msg.retain)

    time.sleep(10)


def on_subscribe(mosq, obj, mid, granted_qos):
    pass

def on_log(client, userdata, level, buf):
    print("log: ", buf)

# Assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_log = on_log


# Continue the network loop
client.loop_forever()
#client.loop_start()
#client.loop_stop()