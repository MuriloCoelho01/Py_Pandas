import pandas as pd


def contagem_L_C(df):
  print(df.shape)




df = pd.read_excel('C:\\Users\\Danila\\Downloads\\CURSO PB BASES\\BaseCargos.xlsx')
print("BAse importada")
 
rotas = input("1 - Contagem:")
match rotas:
  case "1":
    contagem_L_C(df)
   

  case "2":
    print("ok") 
   


