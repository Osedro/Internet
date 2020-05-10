from socket import *

meuHost = ''

minhaPort = 50007

# AF_INET => Protocolo de endereço de IP
# SOCK_STREAM => Protocolo de transferência TCP
objsocket = socket(AF_INET, SOCK_STREAM)

objsocket.bind((meuHost, minhaPort))

objsocket.listen(4)

print('SERVIDOR INICIALIZADO')
print('AGUARDANDO CLIENTES')

while True:
    # Aceita uma conexão quando encontrada e devolve a um novo socket conexão e o endereço do cliente conectado
    conexao, endereco = objsocket.accept()

    print('Servidor conectado a ', endereco)

    while True:
        # Recebe dados enviados pelo cliente
        # 1024 é o tamanho da informação em bytes
        data = conexao.recv(1024)

        # Se não receber nada, paramos o loop
        if not data:
            break
        
        resp = int(data.decode('utf-8'))
        sresp = str(resp) + ' ao quadrado é ' + str(resp*resp)

        #print(sresp)

        # Servidor devolve data
        #conexao.send(b'Eco=> ' + data)
        conexao.send(sresp.encode())
    
    conexao.close()

