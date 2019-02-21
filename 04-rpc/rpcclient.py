import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://127.0.0.1:8888")

hasil = client.tambah(20, 10)

print(hasil)