#Lista de sanduíches no menu:
sandwich_orders=['x-tudo','big mac','carne oss','bistecão']
#Lista de sanduíches finalizados:
finished_sandwiches=[]

#Adicionando os pedidos nos sanduíches finalizados:
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()

    print(f"Sanduíche em preparo: {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

    print(f"\nOs seguintes sanduíches foram preparados:")
    for sandwich_ordered in sandwich_orders:
        print(sandwich_ordered.title())