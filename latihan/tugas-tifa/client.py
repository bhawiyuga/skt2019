# import library xml rpc client
import xmlrpc.client

# Inisiasi client
client = xmlrpc.client.ServerProxy("http://127.0.0.1:8000")

# Eksekusi RPC
hasil = client.beli(5,1000)

# Cetak hasil
print(hasil)
