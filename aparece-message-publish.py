import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect

client.connect("mqtt.eclipse.org", 1883, 60)

time.sleep(1)
message = ""
while True:
    client.loop()
    client.publish("harvey/message", message)
    time.sleep(1)
    message = input("Enter a message: ")
