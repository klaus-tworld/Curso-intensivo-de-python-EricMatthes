ingredientes="Diga os ingredientes que deseja"
ingredientes+=", digite 'quit' para sair "  
mensagem=""

while mensagem!='quit':
    mensagem=input(ingredientes)
    if mensagem!='quit':
        print(f"\nO ingrediente {mensagem} será adicionado")
    else:
        print("\nPrograma encerrado")