import socket
import pickle


def envia(lista):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 9987
    clientsocket.connect((host, port))
    receblista = lista
    lista = pickle.dumps(receblista)
    clientsocket.send(lista)
    recebeimc = clientsocket.recv(1024)
    imc = pickle.loads(recebeimc)
    clientsocket.close()
    classificacao = ''
    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif 18.5 < imc < 24.9:
        classificacao = 'Peso normal'
    elif 25 <= imc <= 29.9:
        classificacao = 'Sobrepeso'
    elif 30 <= imc <= 34.9:
        classificacao = 'Obesidade grau 1'
    elif 35 <= imc <= 39.9:
        classificacao = 'Obesisdade grau 2'
    elif imc > 40:
        classificacao = 'Obesidade grau Morbita '
    return f"O seu imc é {round(imc,2)}" \
           f"\n {classificacao}"
