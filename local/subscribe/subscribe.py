import paho.mqtt.client as paho
import time
from pprint import pprint
import datetime
import json

now = datetime.datetime.now()

#Defining variables
MQTT_BROKER = "192.168.0.37"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 10

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to : " +str(mid))
    print("Granted QoS : " +str(granted_qos))      

def on_message(client, userdata, msg):
    now = datetime.datetime.now()
    print "Subscribed at : " + now.strftime("%H:%M:%S")
    millis_subscribe = int(round(time.time() * 1000))
    
    print("You have subscribed for : " + msg.topic)
    print("Data : " + str(msg.payload))

    str_data = str(msg.payload)
    json_data = json.loads(str(msg.payload))
    
    millis_publish = json_data['millis']
    str_latency = millis_subscribe - millis_publish
    latency = int(str_latency)

    print "LATENCY in (ms) : ", abs(latency)
    print abs(latency)
    print "SIZE in (bytes) : ", len(str_data.encode('utf-8'))

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
try:
	client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
except:
	print "Hello"
client.subscribe("environment/#",qos=1)


#Loop till the end of publish
client.loop_forever()
