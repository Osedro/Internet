from tkinter import *
from invest_lib import *
import threading


class interface(object):
    
    labels_acoes = []


    def __init__(self,toplevel):

        self.mainframe = Frame(bg = 'white')
        self.mainframe.pack()
        self.mainframe.place(x = 10, y = 10, width = 400, height = 400)
        

        self.primeira_coluna = Frame(bg = 'gray')
        self.primeira_coluna.pack(side = LEFT)
        self.primeira_coluna.place(x = 10, y = 10, width = 60)

        self.cabecalho_label_acoes = Label(self.primeira_coluna, text = "Ações", bg = 'red')
        self.cabecalho_label_acoes.pack()
        #self.cabecalho_label_acoes.place(width = 75, height = 25)

        for acao in acoes:
            self.labels_acoes.append(Label(self.primeira_coluna, text = acao, bg = 'white'))
        
        cont = 26

        for label in self.labels_acoes:
            label.pack()
            #label.place(width = 75, height = 25, x = 20, y = cont)
            cont = cont + 26



class tcgui(threading.Thread):
    
    def __init__(self):
        
        threading.Thread.__init__(self)

    def run(self):

        i = Tk()

        i.geometry("500x500")

        i.configure(bg = 'white')

        i.title("Invest Visualizer (Alpha)")
        
        interface(i)

        i.mainloop()
