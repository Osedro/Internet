import urllib.request
import urllib.error
import time
from datetime import datetime

def get_valor_mglu3():
    site = "https://br.investing.com/equities/magaz-luiza-on-nm"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        

    except urllib.error.HTTPError as e:
        print('ERRO',e.code)

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

def write_mglu3(mglu3):
    dia_atual = str(datetime.now().strftime('%d-%m-%Y'))
    arquivo_path = 'MGLU3/' + dia_atual + '.txt'
    arquivo = open(arquivo_path,'a')
    arquivo.write(datetime.now().strftime('%H:%M')+','+str(mglu3)+'\n')
    arquivo.close()

def get_valor_itsa4():
    site = "https://br.investing.com/equities/itausa-pn-ej-n1"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        

    except urllib.error.HTTPError as e:
        print('ERRO',e.code)

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

def get_valor_knri11():
    site = "https://br.investing.com/equities/fii-kinea"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        

    except urllib.error.HTTPError as e:
        print('ERRO',e.code)

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

def get_valor_bbfi11b():
    site = "https://br.investing.com/equities/progressivo"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        

    except urllib.error.HTTPError as e:
        print('ERRO',e.code)

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

def get_valor_xpml11():
    site = "https://br.investing.com/etfs/xp-malls-fdo-inv-imob-fii"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        

    except urllib.error.HTTPError as e:
        print('ERRO',e.code)

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

def get_valor_gndi3():
    site = "https://br.investing.com/equities/notre-dame-intermedica-participacoe"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        

    except urllib.error.HTTPError as e:
        print('ERRO',e.code)

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

def get_valor_b3sa3():
    site = "https://br.investing.com/equities/bmfbovespa-on-nm"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        

    except urllib.error.HTTPError as e:
        print('ERRO',e.code)

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

def get_valor_brdt3():
    site = "https://br.investing.com/equities/petrobras-distribuidora"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        

    except urllib.error.HTTPError as e:
        print('ERRO',e.code)

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

def get_valor_itsa3():
    site = "https://br.investing.com/equities/itausa-on-ej-n1"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        

    except urllib.error.HTTPError as e:
        print('ERRO',e.code)

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

def get_valor_yduq3():
    site = "https://br.investing.com/equities/estacio-part-on-nm"
    headers = {}
    headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        req = urllib.request.Request(site, headers=headers)
        content = str(urllib.request.urlopen(req).read())
        

    except urllib.error.HTTPError as e:
        print('ERRO',e.code)

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