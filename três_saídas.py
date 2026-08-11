while True:
    entrada=input("Qual sua idade?\nDigite 'quit' para sair: ")

    if entrada=='quit':
        print("Você saiu da tela")
        break

    idade=int(entrada)

    if idade<3:
        price='Grátis'
    elif idade<12:
        price='US$10'
    else:
        price='US$15'
    print(f"O custo foi: {price}\n")
    