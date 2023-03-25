import paho.mqtt.client as mqtt
import random
import time

broker_address = "mqtt.eclipseprojects.io"
broker_port = 1883
client = mqtt.Client()
client.connect(broker_address, broker_port)

def simulate_data():
    temperature = random.uniform(18.0, 32.0)
    luminosity = random.uniform(0, 100)
    return temperature, luminosity

while True:
    temperature, luminosity = simulate_data()
    client.publish("jardim/temperatura", temperature)
    client.publish("jardim/luminosidade", luminosity)
    print("Just published " + str(temperature) + " to topic temperatura")
    print("Just published " + str(luminosity) + " to topic luminosidade")
    time.sleep(5)
