import pandas as pd

db_produtos = pd.read_excel('C:\\Users\\Danila\\Downloads\\CURSO PB BASES\\Tabela Produtos.xlsx')
db_vendas = pd.read_excel('C:\\Users\\Danila\\Downloads\\CURSO PB BASES\\Tabela Vendas.xlsx')
db_vendedores = pd.read_excel('C:\\Users\\Danila\\Downloads\\CURSO PB BASES\\Vendedor e seus IDs.xlsx')

print(db_vendas)
print(db_produtos)
print(db_vendedores)


cont_db = db_produtos.shape
print(cont_db)


nova_base = pd.concat([db_vendedores, db_produtos], axis=1, ignore_index = True)
print(nova_base)


