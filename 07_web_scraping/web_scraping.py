import requests
from bs4 import BeautifulSoup

site = requests.get("https://www.climatempo.com.br/").content #conteudo da requisição http

soup = BeautifulSoup(site, 'html.parser')                     #converte para o HTML   

temperatura = soup.find("span", class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5") #busca algum elemento
print(temperatura.string)

print(soup.title.string)
print(soup.a.string)
print(soup.p.string)
print(soup.find('Temperatura'))

arquivo = open("07_web_scraping/site.html", 'w')
arquivo.write(soup.prettify())                                #convete string
arquivo.close()