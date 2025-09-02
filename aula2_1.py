#exercicio1 da aula2

lista_compras = []

while True :

    print("\n## Lista de compras! ##")
    print("1. Para adicionar um item, digite 1")
    print("2. Para remover um item, digite 2")
    print("3. Para ver a lista, digite 3")
    print("4. Para sair, digite 4")
    
    opcao = input("Escolha a opcao: ")

    if opcao == "1" :
        novo_item = input("Qual item vc deseja adicionar: ")
        if novo_item in lista_compras :
            print("\nEsse item já está na lista")
        else :
            lista_compras.append(novo_item)

    elif opcao == "2" :
        tira_item = input("Qual item vc deseja remover: ")
        if tira_item in lista_compras :
            lista_compras.remove(tira_item)
        else :
            print("\nEsse item não está na lista")

    elif opcao == "3" :
        print("\nLista de compras:", lista_compras)
    
    elif opcao == "4" :
        break

    else :
        print("\nEscolha uma opção válida")

