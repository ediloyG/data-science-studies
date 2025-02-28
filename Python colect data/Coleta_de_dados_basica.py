import requests
from bs4 import BeautifulSoup
import pandas as pd

# https://br.financas.yahoo.com/quote/%5EBVSP/history


print('Requests:')
response = requests.get(
    'https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/')
print(response.text[:600])  # informa os 600 primeiros caracteres da página

print('\n\nBeautifulSoup:')
soup = BeautifulSoup(response.text, 'html.parser')
# prettify() formata o código HTML para melhor visualização
print(soup.prettify()[:600])

print('\n\nPandas:')
url_dados = pd.read_html(
    'https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/')
# informa a primeiratabela do site, head(10) informa as 10 primeiras linhas
print(url_dados[0].head(10))
