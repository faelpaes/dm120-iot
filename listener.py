import paho.mqtt.client as mqtt

broker_address = "mqtt.eclipseprojects.io"
broker_port = 1883
client = mqtt.Client()
client.connect(broker_address, broker_port)

def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker com sucesso!")
    client.subscribe("jardim/temperatura")
    client.subscribe("jardim/luminosidade")

def on_message_temperature(client, userdata, msg):
    temperature = float(msg.payload.decode())
    print("Temperatura:", temperature)

def on_message_luminosity(client, userdata, msg):
    luminosity = float(msg.payload.decode())
    print("Luminosidade:", luminosity)

client.on_connect = on_connect
client.on_message = on_message_temperature
client.message_callback_add("jardim/temperatura", on_message_temperature)

client.on_connect = on_connect
client.on_message = on_message_luminosity
client.message_callback_add("jardim/luminosidade", on_message_luminosity)

client.loop_forever()
