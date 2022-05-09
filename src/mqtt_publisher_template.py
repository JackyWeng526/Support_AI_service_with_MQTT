import paho.mqtt.client as mqtt
import json  
import time

# MQTT Client
client = mqtt.Client()

# connect(IP, Port, connectionTime)
client.connect("Your_IP", 1883, 30)

time.sleep(1)

# make a test data
payload = {"Time" : "2021-10-16T16:38:02", "Temperature" : 30.2 , "Humid": 58.0}

msg = json.dumps(payload)
print(msg)

client.publish("test/test_message", msg)
