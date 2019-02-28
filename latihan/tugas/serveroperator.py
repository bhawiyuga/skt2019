from xmlrpc.server import SimpleXMLRPCServer

daftar_pembelian = []

# Inisiasi xml rpc server dengan port 8080
server = SimpleXMLRPCServer( ("0.0.0.0", 8082) )

# Definisikan fungsi yang akan dipanggil di server
def belipulsa(jumlah):
    daftar_pembelian.append(jumlah)
    print("Transaksi berhasil")
    return ""

# Register fungsi
server.register_function(belipulsa, "belipulsa")
# Running server
server.serve_forever()