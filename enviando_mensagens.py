#Definindo a função
def show_messages(msgs):
    """Exibe a mensagem de texto"""
    for mensagem in msgs:
        print(mensagem)

def send_messsages(message_to_send, sent_messages):
    """Envia a mensagem para uma lista vazia"""
    while mensagens:
        current_message=mensagens.pop()
        print(f"\nEnviando '{current_message}'")
        sent_messages.append(current_message)

#Criando uma lista
mensagens=['vc','pprt','tbm','lol']
sent_messages=[]

#Função para transferir
send_messsages(mensagens, sent_messages)

print("\nEstado final das listas: ")
print(f"mensagens: {mensagens}")
print(f"sent_messages: {sent_messages}")
