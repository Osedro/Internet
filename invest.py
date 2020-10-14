import time
import sys
from datetime import datetime
from invest_lib import *
#from gui import *
import threading

taquisitar = aquisitar()

taquisitar.start()


try:
    taquisitar.join()
    print("Thread aquisitar encerrada.")

    print("Encerrando...")
except:
    print("Erro")

