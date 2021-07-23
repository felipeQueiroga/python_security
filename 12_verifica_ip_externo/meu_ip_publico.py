import re
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json/'

resposta = urlopen(url)

dados = json.load(resposta)

print(dados)
print(dados['ip'])
print(dados['org']) #...