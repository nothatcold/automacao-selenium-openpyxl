from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# acessar o site https://www.kabum.com.br/computadores/pc/pc-gamer
driver = webdriver.Chrome()
driver.get('https://www.kabum.com.br/computadores/pc/pc-gamer')

# extrair todos os títulos
titulos = driver.find_elements(By.XPATH,"//div[@class='sc-93fa31de-15 dCsZrx']")

# extrair todos os preços
precos = driver.find_elements(By.XPATH,"//div[@class='sc-6889e656-0 bggLyN availablePricesCard']")

# Criando a planilha
workbook = openpyxl.Workbook()
# Criando a página 'produtos'
workbook.create_sheet('produtos')
# Seleciono a página produtos
sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'


# inserir os títulos e preços na planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text,preco.text])

workbook.save('produtos.xlsx')