# import library paho mqtt
import paho.mqtt.client as mqtt

# inisiasi client mqtt
client = mqtt.Client(client_id="sub1", clean_session=True)

# Koneksikan ke broker
client.connect("127.0.0.1", port=1883)

# Subscribe ke salah satu topik
client.subscribe("/suhu/1", qos=1)

# Buat fungsi untuk menghandle message yang masuk
def handle_message(client, obj, msg):
    print(msg.payload)

# Daftarkan fungsi handle message
client.on_message = handle_message

# Buat infinite loop supaya subscriber tidak mati
client.loop_forever()