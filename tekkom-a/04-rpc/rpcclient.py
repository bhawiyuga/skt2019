# import library xml rpc client
import xmlrpc.client

# Inisiasi client
client = xmlrpc.client.ServerProxy("http://127.0.0.1:8888")

# Eksekusi RPC
hasil = client.tambah(20,10)

# Cetak hasil
print(hasil)
