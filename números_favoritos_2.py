números_favoritos = {'Júlia': [1, 2], 'Clara': [2, 3], 'Marcia': [3, 4]}


for nome, numeros in números_favoritos.items():
    print(f"Os números favoritos de {nome} são:")


    for num in numeros:
        print(f" - {num}")
    print()  