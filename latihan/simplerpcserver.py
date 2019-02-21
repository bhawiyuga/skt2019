from xmlrpc.server import SimpleXMLRPCServer

# Inisiasi xml rpc server dengan port 8080
server = SimpleXMLRPCServer( ("0.0.0.0", 8080) )

# Definisikan fungsi yang akan dipanggil di server
def add_function(a,b):
    return (a+b)

# Register fungsi
server.register_function(add_function, "add")
# Running server
server.serve_forever()