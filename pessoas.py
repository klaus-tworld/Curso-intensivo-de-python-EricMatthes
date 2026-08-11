#Informações pessoais
pessoa_1={'first_name':'Tom','last_name':'Cruise','age':64,'city':'Syracuse'}
pessoa_2={'first_name':'Marie','last_name':'Curie','age':66,'city':'Varsóvia'}
pessoa_3={'first_name':'Klaus','last_name':'Augusto','age':22,'city':'Campinas'}

#Criação da lista
people=[pessoa_1,pessoa_2,pessoa_3]

#Loop
for pessoa in people:
    print(f"\nNome: {pessoa_1['first_name']}")
    print(f"Sobrenome: {pessoa_1['last_name']}")
    print(f"Idade: {pessoa_1['age']}")
    print(f"Cidade: {pessoa_1['city']}")

    print(f"\nNome: {pessoa_2['first_name']}")
    print(f"Sobrenome: {pessoa_2['last_name']}")
    print(f"Idade: {pessoa_2['age']}")
    print(f"Cidade: {pessoa_2['city']}")

    print(f"\nNome: {pessoa_3['first_name']}")
    print(f"Sobrenome: {pessoa_3['last_name']}")
    print(f"Idade: {pessoa_3['age']}")
    print(f"Cidade: {pessoa_3['city']}")

    
