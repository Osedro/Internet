from socket import *

# IP do servidor
serverHost = '192.168.0.111'
serverPort = 8080

#mensagem = [b'Salve salve, rapaziada do windows']
entrada = "OIE"
mensagem = []
mensagem.append(entrada.encode())

objsocket = socket(AF_INET, SOCK_STREAM)
objsocket.connect((serverHost, serverPort))

for linha in mensagem:
    objsocket.send(linha)

    data = objsocket.recv(1024)
    print('Cliente recebeu: ', data)