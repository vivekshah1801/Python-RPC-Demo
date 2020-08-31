import rpyc

host = "localhost"
port = 9876

r = rpyc.connect(host, port).root

print(r)

print(r.helloworld())
print("Done")