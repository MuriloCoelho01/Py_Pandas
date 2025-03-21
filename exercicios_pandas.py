import pandas as pd
df_Cargos = pd.read_excel('C:\\Users\\Danila\\Downloads\\CURSO PB BASES\\BaseCargos.xlsx')
df_Clientes = pd.read_excel('C:\\Users\\Danila\\Downloads\\CURSO PB BASES\\BaseCLientes.xlsx')

df_Clientes = df_Clientes.loc[df_Clientes['Nivel de Importancia'] == 3]




print("Base importada com sucesso:")
print(df_Cargos)
print(df_Clientes)


#contagem de linhas e colunas
count_df = df_Cargos.shape
print("Contagem de linhas e colunas")
print(count_df)

#descrição da base de dados,contagem de informações filtradas
description_df = df_Cargos.describe()
print("Descrição da base")
print(description_df)

#excluir coluna
df_Cargos.drop('Quadro', axis= 1, inplace= True)
print(df_Cargos)

df_Cargos = (df_Cargos.loc[df_Cargos['Contratacao'] == 'Diretoria'])

export = df_Cargos.to_excel('base_nova.xlsx', index= False)





