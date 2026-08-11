#Pizzas que eu gosto
pizzas=['mussarela','calabresa','frango']
#Cópia das pizzas
friend_pizzas=pizzas[:]
#Adicionando uma pizza nova à lista original
pizzas.append('peperoni')
#Adicionando uma pizza diferente à outra lista
friend_pizzas.append('sorvete')
#Provando que temos 2 listas distintas
print("Minhas pizzas favoritas são:")
for pizza in pizzas:
    print(f"{pizza.title()}")

print("\nAs outras pizzas favoritas são:")
for friend_pizza in friend_pizzas:
    print(f"{friend_pizza.title()}")
