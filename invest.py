import time
import sys
from datetime import datetime
from invest_lib import *
import threading

buscar_e_escrever()
'''
hora_atual = datetime.now().strftime('%H:%M')
hora_int = int(hora_atual[0:2])

while hora_int < 17 and hora_int >  9:
#for t in range(10):
    buscar_e_escrever()
    hora_atual = datetime.now().strftime('%H:%M')
    hora_int = int(hora_atual[0:2])
    print(hora_atual,'\n')
    #print(t,'\n\n')
    time.sleep(30)

print('TERMINOU')
'''