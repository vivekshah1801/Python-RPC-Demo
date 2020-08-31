import rpyc
import os
from flask import Flask

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
    t = ThreadedServer(MyService,port=os.environ.get("port",5000))
    print(f'Server listening on {t.port}:{t.host}')
    
    t.start()

    print("RPC Server Started")

if __name__=="__main__":
    app = Flask(__name__)

@app.route('/')
def hello():
    return "Hi vivek, flask is on."
