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

def on_publish(client, userdata, mid):
	print("Message "+str(mid)+" published.")

#def on_subscribe(client, userdata, mid, granted_qos):
#	print("Subscribe with mid "+str(mid)+" received.")

def on_message(client, userdata, msg):
	print("Message received on topic "+msg.topic+" with QoS "+str(msg.qos)+" and payload "+msg.payload)

mqttclient = mqtt.Client()

# Assign event callbacks
mqttclient.on_connect = on_connect
mqttclient.on_publish = on_publish
#mqttclient.on_subscribe = on_subscribe
mqttclient.on_message = on_message

# Connect
mqttclient.username_pw_set("prashantkrishnan99@gmail.com", "d10e68f5")
mqttclient.connect("mqtt.dioty.co", 1883)
#mqtt.dioty.co -> 104.198.201.218

# Start subscription
#mqttclient.subscribe(yourRootTopic)

# Publish a message
def getJsonData():
    for i in range(1,1000):
	voltage = random.uniform(0.70,0.75)
	Celsius = random.uniform(20.0,25.0)
	Fahrenheit = 9.0/5.0 * Celsius + 32
		
        _data_js = {}
	temp = {}

	_data_js["id"] = i
	_data_js["voltage"] = voltage
	temp["Celsius"] = Celsius
	temp["Farhenheit"] = Fahrenheit
	_data_js["temp"] = temp

	now = datetime.datetime.now()
        print "Published at : " + now.strftime("%H:%M:%S")
        millis = int(round(time.time() * 1000))
        _data_js["millis"] = millis
		
	data = json.dumps(_data_js,indent=2)
	pprint(data)
	
        mqttclient.publish("/prashantkrishnan99@gmail.com/temp", str(data)) 
        time.sleep(1)

while True:
    getJsonData()

