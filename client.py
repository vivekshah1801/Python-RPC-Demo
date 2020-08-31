import rpyc

r = rpyc.connect("https://rocky-dawn-55347.herokuapp.com/",80).root

print(r)