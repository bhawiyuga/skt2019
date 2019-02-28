# import library xmlrpc server
from xmlrpc.server import SimpleXMLRPCServer

# Buat instance xml rpc server
server = SimpleXMLRPCServer( ("0.0.0.0", 8888) )

# Definisikan fungsi untuk melakukan penjumlahan
def handle_add(a, b):
    return (a+b)

# Register fungsinya
server.register_function(handle_add, "tambah")

# Jalankan servernya
server.serve_forever()