from socket import *

# IP do servidor
#serverHost = '192.168.56.1'    #Windows
serverHost = '192.168.1.159'    #Linux
serverPort = 50007

#mensagem = [b'Salve salve, rapaziada do windows']
#entrada = input()
mensagem = []
mensagem.append(input().encode())

objsocket = socket(AF_INET, SOCK_STREAM)
objsocket.connect((serverHost, serverPort))

for linha in mensagem:
    objsocket.send(linha)

    data = objsocket.recv(1024)
    print('Cliente recebeu: ', data.decode('utf-8'))