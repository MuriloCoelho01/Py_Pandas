import pandas as pd

db_produtos = pd.read_excel('C:\\Users\\Danila\\Downloads\\CURSO PB BASES\\Tabela Produtos.xlsx')
db_vendas = pd.read_excel('C:\\Users\\Danila\\Downloads\\CURSO PB BASES\\Tabela Vendas.xlsx')

print(db_vendas)
print(db_produtos)

#Manipulação da primeira base de dados
cont_db = db_produtos.shape
print(cont_db)