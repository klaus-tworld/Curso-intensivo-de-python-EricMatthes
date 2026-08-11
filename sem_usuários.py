usuários=['charles','julio','lucas','marcos','admin']
for usuário in usuários:
    if usuário=='admin':
        print("Olá, administrador, gostaria de ver um relatório de status?")
    else:
        print(f"Olá {usuário.title()}, obrigado por fazer login novamente")
else:
    print("É necessário encontrar alguns usuários")