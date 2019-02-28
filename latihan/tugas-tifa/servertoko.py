# import library xmlrpc server
from xmlrpc.server import SimpleXMLRPCServer

# Buat instance xml rpc server
server = SimpleXMLRPCServer( ("0.0.0.0", 8002) )

stok = 20

# Definisikan fungsi untuk melakukan penjumlahan
def beli(jumlah):
    global stok
    if jumlah < stok :
        stok = stok - jumlah
        print("Sisa stok "+ str(stok))
        return "Sukses"
    else :
        return  "Gagal"

# Register fungsinya
server.register_function(beli, "beli")

# Jalankan servernya
server.serve_forever()