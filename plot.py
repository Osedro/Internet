from invest_lib import *
import urllib.request
import urllib.error
import time, glob
import matplotlib.pyplot as plt
from datetime import datetime
import threading
import matplotlib.animation as animation

plot_all_today()
#plot_all_n(3)

'''

fig, subgrafs = plt.subplots(4,3)
contx = 0
conty = 0
n = 5
for acao in acoes:
    last = ultimas_n(acao,n)
    acaovet = []
    acaovetlast = []
    acaovetinit = []
    flaginit = 0

    for l in last:
        arquivo = open(l,'r')
        texto = arquivo.readlines()
        for i in texto:
            linha = i.split(',')
            try:
                acaovet.append(float(linha[1][0:linha[1].index('\n')]))
            except:
                print(l)
        
        if flaginit == 0:
            acaoinit = acaovet[len(acaovet)-1]
            flaginit=1
        
        acaovetinit.append(acaoinit)
        acaovetlast.append(acaovet[len(acaovet)-1])

        arquivo.close()

    aumento = (acaovetlast[len(acaovetlast)-1]-acaovetlast[0])*100/acaovetlast[0]
    
    subgrafs[contx][conty%3].plot(acaovetlast)
    subgrafs[contx][conty%3].plot(acaovetinit)


    if aumento >= 0:
        subgrafs[contx][conty%3].set_title(acao+': +'+format(aumento,'.2f')+'%', color='green')
    else:
        subgrafs[contx][conty%3].set_title(acao+': '+format(aumento,'.2f')+'%', color='red')
    

    conty = conty+1
    if conty%3 == 0:
        contx = contx+1

fig.subplots_adjust(left=0.06,bottom=0.05,top=0.95,right=0.99,wspace=0.15,hspace=0.4)
plt.show()
'''