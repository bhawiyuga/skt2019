import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://127.0.0.1:8080")
hasil = client.belipulsa(100000)
print(hasil)