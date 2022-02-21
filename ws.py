from bs4 import BeautifulSoup
# Importando a biblioteca BeautifulSoup
import requests
# Importando a biblioteca requests
site = requests.get("https://www.climatempo.com.br/").content
# objeto site recebendo o conteudo da requisição http do site
soup = BeautifulSoup(site, 'html.parser')
#objeto soup está baixando do site html
print(soup.prettify())
#o prettify transforma o html em string e o print exibe o html do site

#temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
# o find vai procurar esse elemento dentro do html
#print(temperatura.string)
