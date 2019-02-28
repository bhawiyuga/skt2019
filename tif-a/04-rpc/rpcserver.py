# Import server rpc
from xmlrpc.server import SimpleXMLRPCServer

# Inisiasi server rpc
server = SimpleXMLRPCServer( ("0.0.0.0", 8888) )

# Buat fungsi yang akan dipanggil
def handle_add(a, b):
    return (a+b)

# Daftarkan fungsinya
server.register_function( handle_add, "tambah" )

# Jalankan servernya
server.serve_forever()


