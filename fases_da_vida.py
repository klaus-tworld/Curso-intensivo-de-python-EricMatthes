#Definindo o valor da variável:
age=22
#Condições
if age<2:
    x='neném'
elif age<4:
    x='criança'
elif age<13:
    x='garoto'
elif age<20:
    x='adolescente'
elif age<65:
    x='adulto'
else:
    x='idoso'

print(f"A pessoa é um/uma {x}")
