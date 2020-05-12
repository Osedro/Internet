import urllib.request
import urllib.error

site = "https://br.investing.com/equities/magaz-luiza-on-nm"
headers = {}
headers['User-Agent'] = "Mozzilla/5.0 (X11; Linux i686) AppWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
try:
    req = urllib.request.Request(site, headers=headers)
    content = str(urllib.request.urlopen(req).read())
    valorindex = int(content.index('<strong class="value">')) + len('<strong class="value">')
    valor = content[valorindex : valorindex+5]
    print(valor)

except urllib.error.HTTPError as e:
    print('ERRO',e.code)
