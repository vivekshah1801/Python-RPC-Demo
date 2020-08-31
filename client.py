import rpyc

r = rpyc.connect("localhost",9876).root

print(r)