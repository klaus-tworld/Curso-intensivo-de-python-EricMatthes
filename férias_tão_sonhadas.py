respostas = {}
sistema = True

while sistema:
    nome = input("Qual seu nome? ")
    lugar = input(f"{nome.title()}, se pudesse visitar qualquer lugar do mundo, para onde iria? ")
    respostas[nome] = lugar

    message = input("Deseja adicionar mais uma pessoa? (yes/no) ")

    if message == 'no':
        sistema = False


print("\n---Respostas---")
for nome, lugar in respostas.items():
    print(f"{nome.title()} gostaria de ir para {lugar.title()}")