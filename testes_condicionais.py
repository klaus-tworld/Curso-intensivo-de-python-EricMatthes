#Testes verdadeiros
car='subaru'
print("If car=='subaru' I predict True")
print(car=='subaru')

motos=['kawasaki','honda','bmw']
print("\nIf 'kawasaki' is in motos, I predict True")
print('kawasaki' in motos)

age_0=21
age_1=15
print("\nIf age_0==21 and age_1==15, I predict True")
print(age_0==21 and age_1==15)
print("\nIf age_0==21 I predict True")
print(age_0==21 or age_1==20)

print('#################')
#Testes falsos
print("\nIf car!=='subaru' I predict False")
print(car=='toyota')

print("\nIf 'harley' is in motos, I predict False")
print('harley' in motos)

print("\nIf age_0!=21 and age_1!=15, I predict False")
print(age_0==22 and age_1==14)
print("\nIf age_0==25 I predict False")
print(age_0==25 or age_1==20)
