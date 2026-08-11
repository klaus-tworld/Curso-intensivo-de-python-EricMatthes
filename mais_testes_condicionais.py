idade_1=25
idade_2=34
print(idade_1 == 25)
print(idade_2 != 34)

print('########')

nome='CARLOS'
nome_2='Alfredo'
print(nome.lower()=='carlos')
print(nome_2.lower()=='carlos')

print('########')

print(idade_1>idade_2)
print(idade_1>=14)
print(idade_2<=34)
print(idade_2<=14)
print(idade_2!=idade_1)

print('########')

print(nome=='CARLOS' or nome_2=='José')
print(nome=='Nelson' and nome_2=='João')

print('########')

lista=[1,2,6,9,14,11]
print(1 in lista)
if 2 not in lista:
    print(False)
