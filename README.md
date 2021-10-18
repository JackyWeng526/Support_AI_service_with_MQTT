# Support_AI_service_with_MQTT
MQTT is a lightweight, publish-subscribe network protocol that transports messages between devices. 

By using MQTT, the AI service requiring additional sensors can easily integrate into the existing building automation system.

## MQTT Installation
Make sure you have already installed Mosquito on your server.

Here are some resources help you to finish the installation.

- [MQTT on Windows](https://delightnet.nl/index.php/mqtt/12-mqtt-broker-installation)
 
- [MQTT on Synology NAS](https://www.youtube.com/watch?v=b3A1RJdDf-w&ab_channel=ediy)

## Start a MQTT broker
Quickly build a test channel on your server and subscribe it.
```bash
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
client.connect("XX.XX.XX.XX", 1883, 30) # XX.XX.XX.XX is the IP address of your MQTT server
client.loop_forever()
```
Then, you can hear the response when messages are sent to the channel.

![subscriber_waiting](https://github.com/JackyWeng526/Support_AI_service_with_MQTT/blob/main/docs/subscriber_waiting.PNG)

## Publish message
Connect to the test channel and publish a test message on it.

```bash
import paho.mqtt.client as mqtt
import json  
import time

client = mqtt.Client()
client.connect("XX.XX.XX.XX", 1883, 30) # XX.XX.XX.XX is the IP address of your MQTT server
time.sleep(1)

payload = {"Time" : "2021-10-16T16:38:02", "Temperature" : 30.2 , "Humid": 58.0}
msg = json.dumps(payload)
print(msg)
client.publish("test/test_message", msg)
```
![publisher_send_test_msg](https://github.com/JackyWeng526/Support_AI_service_with_MQTT/blob/main/docs/publisher_send_test_msg.PNG)

## Receive and save messages
When there are messages uploaded to the channel, the subscriber will receive the response in the string type.

![subscriber_receiving](https://github.com/JackyWeng526/Support_AI_service_with_MQTT/blob/main/docs/subscriber_receiving.PNG)

Use json and pandas libraries to transfer the data ytpe, and then you can save the data or messages easily. 
```bash
data = json.loads(msg.payload)
data_df = pd.DataFrame(data, index=[0])
```
![data_example](https://github.com/JackyWeng526/Support_AI_service_with_MQTT/blob/main/docs/data_example.PNG)

With an edge data logger, like Raspberry Pi, the monitored data can be updated to your server or data center constantly through MQTT.

It will be an alternative to transmit data from additional sensors and submeters for your AI project.

## Authors
- [@Jacky Weng](https://github.com/JackyWeng526)

