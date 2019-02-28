from xmlrpc.server import SimpleXMLRPCServer

saldo = 100000

# Inisiasi xml rpc server dengan port 8080
server = SimpleXMLRPCServer( ("0.0.0.0", 8081) )

# Definisikan fungsi yang akan dipanggil di server
def ceksaldo(jumlah):
    global saldo
    if jumlah < saldo :
        saldo = saldo - jumlah
        print("Sisa saldo "+str(saldo))
        return "Sukses"
    else :
        return "Gagal"

# Register fungsi
server.register_function(ceksaldo, "ceksaldo")
# Running server
server.serve_forever()