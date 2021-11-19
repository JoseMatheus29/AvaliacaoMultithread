import pickle
import socket
import threading
import time

def imc (cliente,addr):
    """Função que recebe o cliente e o addr para calcular o  imc de cada cliente"""
    receblista = cliente.recv(1024)
    lista = pickle.loads(receblista)
    peso = lista[0]
    altura = lista[1]
    imc = int(peso) / pow(float(altura), 2)
    envia = pickle.dumps(imc)
    clientsocket.send(envia)
    lista.clear()
    clientsocket.close()


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9987
serversocket.bind((host, port))
serversocket.listen()
print(f"Serve listening on port {port}")
while True:
    clientsocket, addr = serversocket.accept()
    print(f"Go to conect from {addr} às {time.ctime()}")
    t = threading.Thread(target=imc, args=(clientsocket, addr))
    t.start()
