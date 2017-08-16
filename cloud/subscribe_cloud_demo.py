import paho.mqtt.client as mqtt
import time
from pprint import pprint
import random
import json
import datetime

def on_connect(client, userdata, rc):
	if rc == 0:
		print("Connected successfully.")
	else:
		print("Connection failed. rc= "+str(rc))

def on_subscribe(client, userdata, mid, granted_qos):
	print("Subscribe with mid "+str(mid)+" received.")

def on_message(client, userdata, msg):
	now = datetime.datetime.now()
	print("Message received on topic "+msg.topic+" with QoS "+str(msg.qos))
	print("Data : " + str(msg.payload))
        millis_subscribe = int(round(time.time() * 1000))

	str_data = str(msg.payload)
    	json_data = json.loads(str(msg.payload))

	millis_publish = json_data['millis']
    	str_latency = millis_subscribe - millis_publish
   	latency = int(str_latency)

   	print "LATENCY in (ms) : ", abs(latency)
   	print "SIZE in (bytes) : ", len(str_data.encode('utf-8'))


mqttclient = mqtt.Client()

# Assign event callbacks
mqttclient.on_connect = on_connect
mqttclient.on_subscribe = on_subscribe
mqttclient.on_message = on_message

# Connect
mqttclient.username_pw_set("prashantkrishnan99@gmail.com", "d10e68f5")
mqttclient.connect("mqtt.dioty.co", 1883)

# Start subscription
mqttclient.subscribe("/prashantkrishnan99@gmail.com/temp")

mqttclient.loop_forever()
