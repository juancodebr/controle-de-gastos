gastos = []

while True:
    print("\n ===========CONTROLE DE GASTOS==========")
    print("1 - Adicionar gastos")
    print("2 - Listar gastos")
    print("3 - Ver total de gastos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        descricao = input("Descricao: ")
        valor = float(input("Valor: R$ "))

        gasto = {
            "descricao": descricao,
            "valor": valor
        }
        gastos.append(gasto)

        print("Gastos Adicionado!")

    elif opcao == "2":
        for gasto in gastos:
            print(f"{gasto["descricao"]} - R$ {gasto['valor']:.2f}")

    elif opcao == "3":
        total = 0
        for gasto in gastos:
            total += gasto["valor"]
        print(f"Total de gastos: R$ {total:.2f}")

    elif opcao == "0":
        print("Até a proxima compra!")
        break
    else:
        print("Opção Invalida!")