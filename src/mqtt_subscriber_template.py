import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print(F"Connected with result code {str(rc)}")
    print("Waiting for messages...")
    client.subscribe("test/test_message")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    print(data)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("Your_IP", 1883, 30)
client.loop_forever()
