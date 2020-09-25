import requests
from lxml import html
"""
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)
games = tree.xpath('//div[@class="css-1r3zsoc-StatusBar__root"]/text()')

print(games)"""

"""
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')
print ('Buyers: ', buyers)
print ('Prices: ', prices)
"""
#link = input("Digite o link: ")
page = requests.get('https://www.epicgames.com/store/pt-BR/product/into-the-breach/home')
tree = html.fromstring(page.content)
caminho = '//*[@id="dieselReactWrapper"]/div/div[4]/main/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[2]/span'
lista = tree.xpath(f'{caminho}')
print(*lista)
