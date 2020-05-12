import urllib.request

print('=====NACIONAL 2020=====')
content = urllib.request.urlopen("https://bajasaebrasil.online/prova.php?id=20BR_GER",).read()
content = str(content)
find = '<td>49</td>'
posicao = int(content.index(find))-14
nois = content[posicao : posicao+320]
separado = nois.split('</td>')

#for i in separado:
#    print(i)

#print(separado)
#print(nois)


nomeindex = len('<td style="text-align: left; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">')
nomefim = int(separado[2].index('<br />'))
nome = separado[2][nomeindex:nomefim]
print('Nome da escola:',nome)
print('Posição:', separado[0][0:int(separado[0].index('\\'))]+ '*')
print('Numero da equipe:', separado[1][4:len(separado[1])])
print('Região:',separado[3][4:len(separado[3])])
print('Penalidade:', separado[4][4:len(separado[4])])
print('Segurança:', separado[5][4:len(separado[5])])
print('Projeto:', separado[6][4:len(separado[6])])
print('Dinâmica:', separado[7][4:len(separado[7])])
print('Enduro:', separado[8][4:len(separado[8])])
print('Total:', separado[9][7:int(separado[9].index('</b>'))])

print('\n\n=====NACIONAL 2019=====')
content = urllib.request.urlopen("https://bajasaebrasil.online/19BR/prova.php?id=19BR_GER",).read()
content = str(content)
find = '<td>67</td>'
posicao = int(content.index(find))-15
nois = content[posicao : posicao+320]
separado = nois.split('</td>')

#for i in separado:
#    print(i)

nomeindex = len('<td style="text-align: left; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">')
nomefim = int(separado[2].index('<br />'))
nome = separado[2][nomeindex:nomefim]
print('Nome da escola:',nome)
print('Posição:', separado[0][0:int(separado[0].index('\\'))]+ '*')
print('Numero da equipe:', separado[1][4:len(separado[1])])
print('Região:',separado[3][4:len(separado[3])])
print('Penalidade:', separado[4][4:len(separado[4])])
print('Segurança:', separado[5][4:len(separado[5])])
print('Projeto:', separado[6][4:len(separado[6])])
print('Dinâmica:', separado[7][4:len(separado[7])])
print('Enduro:', separado[8][4:len(separado[8])])
print('Total:', separado[9][4:len(separado[9])])
