import rpyc

r = rpyc.connect("rocky-dawn-55347.herokuapp.com",5000).root

print(r)