import time
import sys
from datetime import datetime
from invest_lib import *

mglu3 = get_valor_mglu3()
write_mglu3(mglu3)
print('MGLU3: R$', mglu3)

#print('ITSA4: R$', get_valor_itsa4())
#print('KNRI11: R$', get_valor_knri11())
#print('BBFI11b: R$', get_valor_bbfi11b())
#print('XPML11: R$', get_valor_xpml11())
#print('GNDI3: R$', get_valor_gndi3())
#print('B3SA3: R$', get_valor_b3sa3())
#print('BRDT3: R$', get_valor_brdt3())
#print('ITSA3: R$', get_valor_itsa3())
#print('YDUQ3: R$', get_valor_yduq3())

'''
hora_atual = datetime.now()
hora_em_texto = hora_atual.strftime('%H:%M')
hora_int = int(hora_em_texto[0:2])

while hora_int < 17 and hora_int >  10:
    hora_atual = datetime.now()
    hora_em_texto = hora_atual.strftime('%H:%M')
    hora_int = int(hora_em_texto[0:2])
    print('Hora:',hora_em_texto,'Preço MGLU3: R$',busca_valor())
    time.sleep(60)
'''