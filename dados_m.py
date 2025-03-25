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


nova_base[1] = nova_base[1].astype(str) 
db_vendas['SKU'] = db_vendas['SKU'].astype(str)


with pd.ExcelWriter('C:\\Users\\Danila\\Downloads\\CURSO PB BASES\\nova_base.xlsx') as writer:
    nova_base.to_excel(writer, sheet_name='novabase', index=False)
    