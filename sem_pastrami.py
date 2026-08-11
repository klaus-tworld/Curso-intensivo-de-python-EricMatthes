sandwich_orders=['pastrami','x-tudo','big mac','carne oss','bistecão','pastrami','pastrami']
finished_sandwiches=[]

print("Estamos sem pastrami no momento\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:    
    current_sandwich=sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)

for finished_sandwich in finished_sandwiches:

    print(f"\nSeu sanduíche de {finished_sandwich} está pronto")

