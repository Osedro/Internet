import time
import sys
from datetime import datetime
from invest_lib import *
#from gui import *
import threading

fig, subgrafs = plt.subplots(4,3)

ani = animation.FuncAnimation(fig, plotar_paralelo,fargs=(fig,subgrafs), interval=120000)
plt.show()