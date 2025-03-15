
nomes = ["Murilo,João,Julio,Gabriel,Pedro,Antonio"]


condicion = input("Deseja adicionar um nome na lista? (S/N)")

if condicion.upper == "S":
    new_name = input("Adicione o nome: ")
    nomes.append(new_name)
    print("Adicionado com sucesso!")
    print("\nLista de nomes atualizada:")
    for nome in nomes:
        print(nome)
 
elif condicion.upper == "N":
     print("\nLista de nomes atualizada:")
     for nome in nomes:
        print(nome)

