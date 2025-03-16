import pandas as pd
df = pd.read_excel('C:\\Users\\Danila\\Downloads\\CURSO PB BASES\\BaseCargos.xlsx')

print("Base importada com sucesso:")
print(df)


#contagem de linhas e colunas
count_df = df.shape
print("Contagem de linhas e colunas")
print(count_df)

#descrição da base de dados,contagem de informações filtradas
description_df = df.describe()
print("Descrição da base")
print(description_df)

#excluir coluna
df.drop('Quadro', axis= 1, inplace= True)
print(df)

export = df.to_excel('base_nova.xlsx', index= False)
if export:
    print("ok")



