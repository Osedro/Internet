from invest_lib import *
import urllib.request
import urllib.error
import time, glob
import matplotlib.pyplot as plt
from datetime import datetime
import threading
import matplotlib.animation as animation

n = int(input("Digite o numero de dias: "))

#plot_all_today()
plot_all_n(n)

