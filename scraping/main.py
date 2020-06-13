import requests
from bs4 import BeautifulSoup


url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')# analisa meu html

for pergunta in html.select('.question-summary'): #estri tudo que estva dentro dessas divs
    titulo=pergunta.select_one('.question-hyperlink')# estrai tudos os titulos
    data =pergunta.select_one(".relativetime")
    votos =pergunta.select_one(".vote-count-post")

    print(data.text, titulo.text, votos.text, sep='\t')


# o que est aentre parenteses é que esta em html na pagina
# print(titulo) vem tudo em html
# print(titulo.text) vem so os textos que estao dentro dos titulos




time.sleep(10)


driver.quit()