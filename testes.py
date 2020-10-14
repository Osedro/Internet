from invest_lib import *

arq = open("acoes.csv",'a')
tenho = "0"
for acao in acoes:
    try:
        pid = pids[acao]
        site = sites[acao]
        arq.write("\n"+acao+","+pid+","+site+","+tenho)
        print("Acao",acao," incluida com sucesso.")
    except:
        print("Erro na acao",acao)


arq.close()
