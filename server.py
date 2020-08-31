import rpyc

class MyService(rpyc.Service):

    # necessary service
    def on_connect(self,conn):
        print("Connected to client")
    
    def on_disconnect(self,conn):
        print("Disconnected from client")
    
    


    def exposed_helloworld(self):
        print("on server")
        return "hello client"


if __name__=="__main__":
    from rpyc.utils.server import ThreadedServer
    print("RPC Server Starting")
    t = ThreadedServer(MyService,port=9876)
    t.start()

    print("RPC Server Started")