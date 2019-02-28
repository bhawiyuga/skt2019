from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

# Inisiasi xml rpc server dengan port 8080
server = SimpleXMLRPCServer( ("0.0.0.0", 8080) )

# Definisikan fungsi yang akan dipanggil di server
def belipulsa(jumlah):
    client_bank = xmlrpc.client.ServerProxy("http://127.0.0.1:8081")
    hasil = client_bank.ceksaldo(jumlah)
    if hasil == "Sukses":
        client_op = xmlrpc.client.ServerProxy("http://127.0.0.1:8082")
        hasil = client_op.belipulsa(jumlah)
        return "Beli Pulsa Sukses"
    else :
        return "Beli Pulsa Gagal"

# Register fungsi
server.register_function(belipulsa, "belipulsa")
# Running server
server.serve_forever()