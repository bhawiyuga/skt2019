# import library xmlrpc server
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


# Buat instance xml rpc server
server = SimpleXMLRPCServer( ("0.0.0.0", 8000) )

# Definisikan fungsi untuk melakukan penjumlahan
def beli(jumlah, harga):
    total = jumlah * harga
    client_bank = xmlrpc.client.ServerProxy("http://127.0.0.1:8001")
    status = client_bank.ceksaldo(total)
    if status == "Sukses" :
        client_toko = xmlrpc.client.ServerProxy("http://127.0.0.1:8002")
        client_toko.beli(jumlah)
        return("Pembelian sukses")
    else :
        return("Saldo tidak cukup")

# Register fungsinya
server.register_function(beli, "beli")

# Jalankan servernya
server.serve_forever()