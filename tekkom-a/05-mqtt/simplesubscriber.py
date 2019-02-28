# import library paho mqtt client
import paho.mqtt.client as mqtt

# Inisiasi client
client = mqtt.Client(client_id="sub1", clean_session=False)

# Koneksi ke broker
client.connect("127.0.0.1", port=1883)

# Subscribe ke topik tertentu
client.subscribe("/suhu/1", qos=1)

# Definisikan callback function untk menerima message dari broker
def on_message(client, obj, msg):
    print(msg.payload)
    
#Daftarkan callback function nya
client.on_message = on_message

# Loop supaya tidak berhenti
client.loop_forever()