# import library xmlrpc server
from xmlrpc.server import SimpleXMLRPCServer

# Buat instance xml rpc server
server = SimpleXMLRPCServer( ("0.0.0.0", 8001) )

saldo = 1000000

# Definisikan fungsi untuk melakukan penjumlahan
def ceksaldo(total):
    global saldo
    if total < saldo :
        saldo = saldo - total
        print("Sisa saldo "+str(saldo))
        return "Sukses"
    else :
        return  "Gagal"

# Register fungsinya
server.register_function(ceksaldo, "ceksaldo")

# Jalankan servernya
server.serve_forever()