from invest_lib import *

resp = "n"

while(resp != "y"):
    acao = input("Digite o nome da ação: ")
    pid = input("Digite o pid da ação: ")
    site = input("Digite o site da ação: ")
    tenho = input("Digite a quantidade de ativos: ")

    print("\n\n")
    print("Confirme os valores:")
    print("Ação:",acao)
    print("pid:",pid)
    print("Site:",site)
    print("Quantidade de ativos:",tenho)
    print("")

    resp = input("Estes valores estão corretos?(y/n)")

    while resp != "n" and resp != "y":
        resp = input("Digite y se os dados estão corretos e digite n se estiverem incorretos.")

try:
    arq = open("acoes.csv",'a')
    arq.write("\n"+acao+","+pid+","+site+","+tenho)
    arq.close()
    print("Dados da ação gravados com sucesso.")
except:
    print("Erro ao salvar dados da ação.")
