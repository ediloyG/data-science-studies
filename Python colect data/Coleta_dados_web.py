import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

'''
# mostra o que esta da extração
 print(extracao.text.strip())# .strip() remove os espaços em branco no inicio e no final da string

for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.strip()
    print('titulo : ',titulo)
'''
'''
# conta paragrafos e titulos
contar_titulos = 0
contrar_paragrafos = 0
for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        contar_titulos += 1 # autoincremento contar_titulos = contar_titulos + 1
    elif linha_texto.name == 'p':
        contrar_paragrafos += 1 # autoincremento contar_titulos = contar_titulos + 1
        
print('Quantidade de titulos: ', contar_titulos)
print('Quantidade de paragrafos: ', contrar_paragrafos)
'''
# exibe tags com links
for titulo in extracao.find_all('h2'):
    print('\n Titulo: ',titulo.text.strip())
    for link in titulo.find_next_siblings('p'):#next_siblings() retorna o que tem dentro das tags seguintes
        for a in link.find_all('a', href=True):#href=true retorna o link
            print('texto Link: ', a.text.strip(), '| url: ', a['href'])
