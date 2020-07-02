import time
import sys
from datetime import datetime
from invest_lib import *
from gui import *
import threading


taquisitar = aquisitar()
tplot_paralelo = tcplotar_paralelo()
#tgui = tcgui()

taquisitar.start()
tplot_paralelo.start()
#tgui.start()

taquisitar.join()
print("Thread aquisitar encerrada.")
tplot_paralelo.join()
print("Thread plot paralelo encerrada.")
print("Encerrando...")

exit()
