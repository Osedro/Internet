import urllib.request
import urllib.error
import time, glob
import matplotlib.pyplot as plt
from datetime import datetime
import threading
import matplotlib.animation as animation

acoes = ['B3SA3','BBFI11b','BRDT3','GNDI3','ITSA3','ITSA4','KNRI11','MGLU3','XPML11','YDUQ3','TRPL4','BOVA11','HGRU11','RBRR11']
pids = {'B3SA3':'18628','BBFI11b':'986549','BRDT3':'1056489','MGLU3':'18729','GNDI3':'1073664',
        'ITSA3':'18705','ITSA4':'18706','KNRI11':'940958','XPML11':'1057399','YDUQ3':'18673',
        'TRPL4':'18805','BOVA11':'39004','HGRU11':'1097720','RBRR11':'1091188'}
sites = {'B3SA3':"https://br.investing.com/equities/bmfbovespa-on-nm",
        'YDUQ3':"https://br.investing.com/equities/estacio-part-on-nm",
        'XPML11':"https://br.investing.com/etfs/xp-malls-fdo-inv-imob-fii",
        'KNRI11':"https://br.investing.com/equities/fii-kinea",
        'ITSA4':"https://br.investing.com/equities/itausa-pn-ej-n1",
        'ITSA3':"https://br.investing.com/equities/itausa-on-ej-n1",
        'GNDI3':"https://br.investing.com/equities/notre-dame-intermedica-participacoe",
        'BRDT3':"https://br.investing.com/equities/petrobras-distribuidora",
        'BBFI11b':"https://br.investing.com/equities/progressivo",
        'MGLU3':"https://br.investing.com/equities/magaz-luiza-on-nm",
        'TRPL4':"https://br.investing.com/equities/tran-paulist-pn",
        'BOVA11':"https://br.investing.com/etfs/ishares-ibovespa",
        'HGRU11':"https://br.investing.com/equities/cshg-renda-urbana-fii",
        'RBRR11':"https://br.investing.com/equities/fii-rbr-rendimento-high-grade"}

def get_valor(acao):
    site = sites[acao]
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        
        valorindex = int(content.index('<span class="arial_26 inlineblock pid-' + pids[acao] +'-last" id="last_last" dir="ltr">')) + len('<span class="arial_26 inlineblock pid-' + pids[acao] +'-last" id="last_last" dir="ltr">')
        
        i = valorindex
        valorstr = ''
        while content[i] != '<' :
            if content[i] != '.':
                valorstr += content[i]
            i = i + 1
        
        virgulaindex = int(valorstr.index(','))
        valorstr = valorstr.replace(valorstr[virgulaindex], '.')
        valor = float(valorstr)
        
        return valor

    except:
        print('ERRO')

class aquisitar(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
                
        hora_atual = datetime.now().strftime('%H:%M')
        hora_int = int(hora_atual[0:2])
        while hora_int<10:
            time.sleep(30)
            hora_atual = datetime.now().strftime('%H:%M')
            print(hora_atual)
            hora_int = int(hora_atual[0:2])

        while hora_int < 17 and hora_int >  9:
            buscar_e_escrever()
            hora_atual = datetime.now().strftime('%H:%M')
            hora_int = int(hora_atual[0:2])
            print('\n',hora_atual)
            #print(t,'\n\n')
            time.sleep(60)

def plotar_paralelo(i, fig, subgrafs):
    data = str(datetime.now().strftime('%d-%m-%Y'))
    contx = 0
    conty = 0
    hora_atual = datetime.now().strftime('%H:%M')
    hora_int = int(hora_atual[0:2])

    if hora_int > 17:
        plt.close(fig)

    for acao in acoes:
        try:
            arquivo = open(acao+'/'+data+'.txt','r')
            
            texto = arquivo.readlines()
            acaovet = []
            acaovetinit = []
            linha = texto[0].split(',')
            acaoinit = float(linha[1][0:linha[1].index('\n')])
            for i in texto:
                linha = i.split(',')
                acaovet.append(float(linha[1][0:linha[1].index('\n')]))
                acaovetinit.append(acaoinit)
            arquivo.close()

            

            aumento = (acaovet[len(acaovet)-1]-acaovet[0])*100/acaovet[0]
            
            subgrafs[contx][conty%4].clear()
            subgrafs[contx][conty%4].plot(acaovet)
            subgrafs[contx][conty%4].plot(acaovetinit)
            
            if aumento >= 0:
                subgrafs[contx][conty%4].set_title(acao+': +'+format(aumento,'.2f')+'%', color='green')
            else:
                subgrafs[contx][conty%4].set_title(acao+': '+format(aumento,'.2f')+'%', color='red')

        except:
            print(acao+' ainda está vazia para o dia '+data)
        #subgrafs[contx][conty%3].set_title(acao)
        
        

        conty = conty+1
        if conty%4 == 0:
            contx = contx+1
    
    #fig.tight_layout(pad=0.01)
    fig.subplots_adjust(left=0.06,bottom=0.05,top=0.95,right=0.99,wspace=0.15,hspace=0.4)
    #plt.show()

class tcplotar_paralelo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        fig, subgrafs = plt.subplots(4,3)

        ani = animation.FuncAnimation(fig, plotar_paralelo,fargs=(fig,subgrafs), interval=120000)
        plt.show()

class tc_mglu3(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        mglu3 = get_valor_mglu3()
        print('MGLU3: R$', mglu3)
        if mglu3 != None:
            #write_mglu3(mglu3)
            write(mglu3, 'MGLU3')

class tc_b3sa3(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        b3sa3 = get_valor_b3sa3()
        print('B3SA3: R$', b3sa3)
        if b3sa3 != None:
            #write_b3sa3(b3sa3)
            write(b3sa3, 'B3SA3')

class tc_bbfi11b(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        bbfi11b = get_valor_bbfi11b()
        print('BBFI11b: R$', bbfi11b)
        if bbfi11b != None:
            #write_bbfi11b(bbfi11b)
            write(bbfi11b, 'BBFI11b')

class tc_brdt3(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        brdt3 = get_valor_brdt3()
        print('BRDT3: R$', brdt3)
        if brdt3 != None:
            #write_brdt3(brdt3)
            write(brdt3, 'BRDT3')

class tc_gndi3(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        gndi3 = get_valor_gndi3()
        print('GNDI3: R$', gndi3)
        if gndi3 != None:
            #write_gndi3(gndi3)
            write(gndi3, 'GNDI3')

class tc_itsa3(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        itsa3 = get_valor_itsa3()
        print('ITSA3: R$', itsa3)
        if itsa3 != None:
            #write_itsa3(itsa3)
            write(itsa3, 'ITSA3')  

class tc_itsa4(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        itsa4 = get_valor_itsa4()
        print('ITSA4: R$', itsa4)
        if itsa4 != None:
            #write_itsa4(itsa4)
            write(itsa4, 'ITSA4')

class tc_knri11(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        knri11 = get_valor_knri11()
        print('KNRI11: R$', knri11)
        if knri11 != None:
            #write_knri11(knri11)
            write(knri11, 'KNRI11')

class tc_xpml11(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        xpml11 = get_valor_xpml11()
        print('XPML11: R$', xpml11)
        if xpml11 != None:
            #write_xpml11(xpml11)
            write(xpml11, 'XPML11')

class tc_yduq3(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        yduq3 = get_valor_yduq3()
        print('YDUQ3: R$', yduq3)
        if yduq3 != None:
            #write_yduq3(yduq3)
            write(yduq3, 'YDUQ3')

class tc_trpl4(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        trpl4 = get_valor('TRPL4')
        print('TRPL4: R$', trpl4)
        if trpl4 != None:
            #write_trpl4(trpl4)
            write(trpl4, 'TRPL4')

class tc_bova11(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        bova11 = get_valor('BOVA11')
        print('BOVA11: R$', bova11)
        if bova11 != None:
            #write_bova11(bova11)
            write(bova11, 'BOVA11')

class tc_rbrr11(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        rbrr11 = get_valor('RBRR11')
        print('RBRR11: R$', rbrr11)
        if rbrr11 != None:
            write(rbrr11, 'RBRR11')

class tc_hgru11(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        hgru11 = get_valor('HGRU11')
        print('HGRU11: R$', hgru11)
        if hgru11 != None:
            write(hgru11, 'HGRU11')

def plot_all_today():
    #fig = plt.figure(len(acoes))
    #fig, subgrafs = plt.subplots(len(acoes))
    data = str(datetime.now().strftime('%d-%m-%Y'))
    fig, subgrafs = plt.subplots(4,3)
    contx = 0
    conty = 0
    for acao in acoes:
        arquivo = open(acao+'/'+data+'.txt','r')
        texto = arquivo.readlines()
        acaovet = []
        acaovetinit = []
        linha = texto[0].split(',')
        acaoinit = float(linha[1][0:linha[1].index('\n')])
        for i in texto:
            linha = i.split(',')
            acaovet.append(float(linha[1][0:linha[1].index('\n')]))
            acaovetinit.append(acaoinit)
        arquivo.close()

        aumento = (acaovet[len(acaovet)-1]-acaovet[0])*100/acaovet[0]
        
        subgrafs[contx][conty%3].plot(acaovet)
        subgrafs[contx][conty%3].plot(acaovetinit)
        if aumento >= 0:
            subgrafs[contx][conty%3].set_title(acao+': +'+format(aumento,'.2f')+'%', color='green')
        else:
            subgrafs[contx][conty%3].set_title(acao+': '+format(aumento,'.2f')+'%', color='red')
        

        conty = conty+1
        if conty%3 == 0:
            contx = contx+1
    
    #fig.tight_layout(pad=0.01)
    fig.subplots_adjust(left=0.06,bottom=0.05,top=0.95,right=0.99,wspace=0.15,hspace=0.4)
    plt.show()

def plot_all(data):
    #fig = plt.figure(len(acoes))
    #fig, subgrafs = plt.subplots(len(acoes))
    #dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    fig, subgrafs = plt.subplots(4,3)
    contx = 0
    conty = 0
    for acao in acoes:
        arquivo = open(acao+'/'+data+'.txt','r')
        texto = arquivo.readlines()
        acaovet = []
        acaovetinit = []
        linha = texto[0].split(',')
        acaoinit = float(linha[1][0:linha[1].index('\n')])
        for i in texto:
            linha = i.split(',')
            acaovet.append(float(linha[1][0:linha[1].index('\n')]))
            acaovetinit.append(acaoinit)
        arquivo.close()

        aumento = (acaovet[len(acaovet)-1]-acaovet[0])*100/acaovet[0]
        
        subgrafs[contx][conty%3].plot(acaovet)
        subgrafs[contx][conty%3].plot(acaovetinit)
        if aumento >= 0:
            subgrafs[contx][conty%3].set_title(acao+': +'+format(aumento,'.2f')+'%', color='green')
        else:
            subgrafs[contx][conty%3].set_title(acao+': '+format(aumento,'.2f')+'%', color='red')
        

        conty = conty+1
        if conty%3 == 0:
            contx = contx+1
    
    #fig.tight_layout(pad=0.01)
    fig.subplots_adjust(left=0.06,bottom=0.05,top=0.95,right=0.99,wspace=0.15,hspace=0.4)
    plt.show()

def plot(acao,data):
    arquivo = open(acao+'/'+data+'.txt','r')
    texto = arquivo.readlines()
    horas = []
    precos = []
    preco = []
    aux = texto[0].split(',')
    preco_inicial = float(aux[1][0:aux[1].index('\n')])
    for i in texto:
        aux = i.split(',')
        horas.append(aux[0])
        precos.append(float(aux[1][0:aux[1].index('\n')]))
        preco.append(preco_inicial)

    arquivo.close()
    
    plt.figure()
    plt.plot(horas,precos)
    plt.plot(horas,preco)
    plt.title('Ações de '+ acao + ' no dia' + data)
    plt.show()

def buscar_e_escrever():
    tmglu3 = tc_mglu3()
    tb3sa3 = tc_b3sa3()
    tbbfi11b = tc_bbfi11b()
    tbrdt3 = tc_brdt3()
    tgndi3 = tc_gndi3()
    titsa3 = tc_itsa3()
    titsa4 = tc_itsa4()
    tknri11 = tc_knri11()
    txpml11 = tc_xpml11()
    tyduq3 = tc_yduq3()
    ttrpl4 = tc_trpl4()
    tbova11 = tc_bova11()
    thgru11 = tc_hgru11()
    trbrr11 = tc_rbrr11()

    tmglu3.start()
    tb3sa3.start()
    tbbfi11b.start()
    tbrdt3.start()
    tgndi3.start()
    titsa3.start()
    titsa4.start()
    tknri11.start()
    txpml11.start()
    tyduq3.start()
    ttrpl4.start()
    tbova11.start()
    thgru11.start()
    trbrr11.start()


def get_valor_mglu3():
    site = "https://br.investing.com/equities/magaz-luiza-on-nm"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        valorindex = int(content.index('<span class="arial_26 inlineblock pid-18729-last" id="last_last" dir="ltr">')) + len('<span class="arial_26 inlineblock pid-18729-last" id="last_last" dir="ltr">')
        i = valorindex
        valorstr = ''
        while content[i] != '<' :
            valorstr += content[i]
            i = i + 1

        virgulaindex = int(valorstr.index(','))
        valorstr = valorstr.replace(valorstr[virgulaindex], '.')
        valor = float(valorstr)
        #print(valorstr[virgulaindex])
        return valor

        
    except:
        print('ERRO')

def write(valor, acao):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = '/home/leonardo/Documents/Internet/' + acao + '/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(valor)+'\n')
    arquivo.close()


def write_mglu3(valor):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = 'MGLU3/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(valor)+'\n')
    arquivo.close()

def get_valor_itsa4():
    site = "https://br.investing.com/equities/itausa-pn-ej-n1"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        valorindex = int(content.index('<span class="arial_26 inlineblock pid-18706-last" id="last_last" dir="ltr">')) + len('<span class="arial_26 inlineblock pid-18706-last" id="last_last" dir="ltr">')
        i = valorindex
        valorstr = ''
        while content[i] != '<' :
            valorstr += content[i]
            i = i + 1
        virgulaindex = int(valorstr.index(','))
        valorstr = valorstr.replace(valorstr[virgulaindex], '.')
        valor = float(valorstr)
        #print(valorstr[virgulaindex])
        return valor

        

    except:
        print('ERRO')   

def write_itsa4(valor):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = 'ITSA4/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(valor)+'\n')
    arquivo.close()

def get_valor_knri11():
    site = "https://br.investing.com/equities/fii-kinea"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        valorindex = int(content.index('<span class="arial_26 inlineblock pid-940958-last" id="last_last" dir="ltr">')) + len('<span class="arial_26 inlineblock pid-940958-last" id="last_last" dir="ltr">')
        i = valorindex
        valorstr = ''
        while content[i] != '<' :
            valorstr += content[i]
            i = i + 1

        virgulaindex = int(valorstr.index(','))
        valorstr = valorstr.replace(valorstr[virgulaindex], '.')
        valor = float(valorstr)
        #print(valorstr[virgulaindex])
        return valor
    except:
        print('ERRO')

def write_knri11(valor):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = 'KNRI11/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(valor)+'\n')
    arquivo.close()

def get_valor_bbfi11b():
    site = "https://br.investing.com/equities/progressivo"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        
        content = str(urllib.request.urlopen(req).read())
        
        valorindex = int(content.index('<span class="arial_26 inlineblock pid-986549-last" id="last_last" dir="ltr">')) + len('<span class="arial_26 inlineblock pid-986549-last" id="last_last" dir="ltr">')
        i = valorindex
        valorstr = ''
        while content[i] != '<' :
            if content[i] != '.':
                valorstr += content[i]
            i = i + 1

        virgulaindex = int(valorstr.index(','))
        valorstr = valorstr.replace(valorstr[virgulaindex], '.')
        valor = float(valorstr)
        #print(valorstr[virgulaindex])
        return valor

    except:
        print('ERRO')

def write_bbfi11b(valor):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = 'BBFI11b/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(valor)+'\n')
    arquivo.close()

def get_valor_xpml11():
    site = "https://br.investing.com/etfs/xp-malls-fdo-inv-imob-fii"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
    
        content = str(urllib.request.urlopen(req).read())
        valorindex = int(content.index('<span class="arial_26 inlineblock pid-1057399-last" id="last_last" dir="ltr">')) + len('<span class="arial_26 inlineblock pid-1057399-last" id="last_last" dir="ltr">')
        i = valorindex
        valorstr = ''
        while content[i] != '<' :
            if content[i] != '.':
                valorstr += content[i]
            i = i + 1

        virgulaindex = int(valorstr.index(','))
        valorstr = valorstr.replace(valorstr[virgulaindex], '.')
        valor = float(valorstr)
        #print(valorstr[virgulaindex])
        return valor

    except:
        print('ERRO')

def write_xpml11(valor):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = 'XPML11/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(valor)+'\n')
    arquivo.close()

def get_valor_gndi3():
    site = "https://br.investing.com/equities/notre-dame-intermedica-participacoe"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        valorindex = int(content.index('<span class="arial_26 inlineblock pid-1073664-last" id="last_last" dir="ltr">')) + len('<span class="arial_26 inlineblock pid-1073664-last" id="last_last" dir="ltr">')
        i = valorindex
        valorstr = ''
        while content[i] != '<' :
            if content[i] != '.':
                valorstr += content[i]
            i = i + 1

        virgulaindex = int(valorstr.index(','))
        valorstr = valorstr.replace(valorstr[virgulaindex], '.')
        valor = float(valorstr)
        #print(valorstr[virgulaindex])
        return valor

    except:
        print('ERRO')

def write_gndi3(valor):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = 'GNDI3/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(valor)+'\n')
    arquivo.close()

def get_valor_b3sa3():
    site = "https://br.investing.com/equities/bmfbovespa-on-nm"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        valorindex = int(content.index('<span class="arial_26 inlineblock pid-18628-last" id="last_last" dir="ltr">')) + len('<span class="arial_26 inlineblock pid-18628-last" id="last_last" dir="ltr">')
        i = valorindex
        valorstr = ''
        while content[i] != '<' :
            if content[i] != '.':
                valorstr += content[i]
            i = i + 1

        virgulaindex = int(valorstr.index(','))
        valorstr = valorstr.replace(valorstr[virgulaindex], '.')
        valor = float(valorstr)
        #print(valorstr[virgulaindex])
        return valor

    except:
        print('ERRO')

def write_b3sa3(valor):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = 'B3SA3/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(valor)+'\n')
    arquivo.close()

def get_valor_brdt3():
    site = "https://br.investing.com/equities/petrobras-distribuidora"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        valorindex = int(content.index('<span class="arial_26 inlineblock pid-1056489-last" id="last_last" dir="ltr">')) + len('<span class="arial_26 inlineblock pid-1056489-last" id="last_last" dir="ltr">')
        i = valorindex
        valorstr = ''
        while content[i] != '<' :
            if content[i] != '.':
                valorstr += content[i]
            i = i + 1

        virgulaindex = int(valorstr.index(','))
        valorstr = valorstr.replace(valorstr[virgulaindex], '.')
        valor = float(valorstr)
        #print(valorstr[virgulaindex])
        return valor

    except:
        print('ERRO')

def write_brdt3(valor):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = 'BRDT3/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(valor)+'\n')
    arquivo.close()

def get_valor_itsa3():
    site = "https://br.investing.com/equities/itausa-on-ej-n1"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        valorindex = int(content.index('<span class="arial_26 inlineblock pid-18705-last" id="last_last" dir="ltr">')) + len('<span class="arial_26 inlineblock pid-18705-last" id="last_last" dir="ltr">')
        i = valorindex
        valorstr = ''
        while content[i] != '<' :
            if content[i] != '.':
                valorstr += content[i]
            i = i + 1

        virgulaindex = int(valorstr.index(','))
        valorstr = valorstr.replace(valorstr[virgulaindex], '.')
        valor = float(valorstr)
        #print(valorstr[virgulaindex])
        return valor

    except:
        print('ERRO')

def write_itsa3(valor):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = 'ITSA3/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(valor)+'\n')
    arquivo.close()

def get_valor_yduq3():
    site = "https://br.investing.com/equities/estacio-part-on-nm"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        valorindex = int(content.index('<span class="arial_26 inlineblock pid-18673-last" id="last_last" dir="ltr">')) + len('<span class="arial_26 inlineblock pid-18673-last" id="last_last" dir="ltr">')
        i = valorindex
        valorstr = ''
        while content[i] != '<' :
            if content[i] != '.':
                valorstr += content[i]
            i = i + 1

        virgulaindex = int(valorstr.index(','))
        valorstr = valorstr.replace(valorstr[virgulaindex], '.')
        valor = float(valorstr)
        #print(valorstr[virgulaindex])
        return valor

    except:
        print('ERRO')

def write_yduq3(valor):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = 'YDUQ3/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(valor)+'\n')
    arquivo.close()

def write_trpl4(valor):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = 'TRPL4/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(valor)+'\n')
    arquivo.close()

def write_bova11(valor):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = 'BOVA11/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(valor)+'\n')
    arquivo.close()

def ultimas_n(acao,n):

    ultimas = []*n

    data = str(datetime.now().strftime('%d-%m-%Y'))
    data_sep = data.split('-')
    mes_atual = int(data_sep[1])

    arquivos = glob.glob(acao+'/*.*')
    meses = []

    for i in range(12):
        # cria a linha i
        linha = [] # lista vazia
        # coloque linha na matriz
        meses.append(linha)

    for f in arquivos:
        #arquivos.append(f)
        aux = f.split('-')
        mes = int(aux[1])
        meses[mes-1].append(f)

    for i in range(12):
        meses[i] = sorted(meses[i])


    cont = 0

    while cont < n:
        if len(meses[mes_atual-1]) != 0:
            ultimas.append(meses[mes_atual-1].pop())
            cont = cont + 1
        elif mes_atual == 0:
            break
        else:
            mes_atual=mes_atual-1
        
    ultimas.reverse()

    return ultimas


def plot_all_n(n):
    fig, subgrafs = plt.subplots(4,3)
    contx = 0
    conty = 0
    for acao in acoes:
        last = ultimas_n(acao,n)
        acaovet = []
        acaovetinit = []
        flaginit = 0
        for l in last:
            arquivo = open('/home/leonardo/Documents/Internet/' +l,'r')
            texto = arquivo.readlines()
            if flaginit == 0:
                linha = texto[0].split(',')
                acaoinit = float(linha[1][0:linha[1].index('\n')])
                flaginit=1
            for i in texto:
                linha = i.split(',')
                acaovet.append(float(linha[1][0:linha[1].index('\n')]))
                acaovetinit.append(acaoinit)
            arquivo.close()

        aumento = (acaovet[len(acaovet)-1]-acaovet[0])*100/acaovet[0]
        
        subgrafs[contx][conty%3].plot(acaovet)
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



