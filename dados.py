from random import randint
class Die:
    def __init__(self, sides):
        self.sides=sides

    def roll_die(self,lançamentos):
        resultados=[]

        for i in range(lançamentos):
            numero=randint(1,self.sides)
            resultados.append(numero)

        return resultados
a=int(input(f"Quantas faces tem o dado?: "))
if a in (6,10,20):
    dado=Die(a)
    resultados=dado.roll_die(10)
    print(resultados)

else:
    print("Numéro inválido. Tente 6,10 ou 20")