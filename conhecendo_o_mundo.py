lista=['K','A','P','C','F']
#Lista na ordem original
print(lista)

#Ordem alfabética temporária
alfabética_t=sorted(lista)
print(alfabética_t)

#A lista permanece igual
print(lista)

#Ordem alfabética reversa temporária
alfabética_t.reverse()
print(alfabética_t)

#A lista ainda está na ordem original
print(lista)

#Revertendo a ordem
lista.reverse()
print(lista)
lista.reverse()
print(lista)

#Ordem alfabética definitiva
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)