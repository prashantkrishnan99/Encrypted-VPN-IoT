import paho.mqtt.client as paho
import time
from pprint import pprint
import random
import json
import datetime

#Define variables
MQTT_BROKER = "192.168.0.37"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 10
voltage = 0.0
Celsius = 0.0
Fahrenheit = 0.0

def on_publish(client, userdata, mid):
    print ("message_id : " +str(mid))

client = paho.Client()
client.on_publish = on_publish

try:
    client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
    client.loop_start()
except:
    print "Connection error !!!"

def getJsonData():
    #vary in a scale of 1000	
    number_of_requests = 1000;
    for i in range(1,number_of_requests):
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
        #print millis
		
	data = json.dumps(_data_js,indent=2)
	
        (rc,mid) = client.publish("environment/temperature",str(data),qos=1)
        
        time.sleep(0.001)

while True:
    getJsonData()
