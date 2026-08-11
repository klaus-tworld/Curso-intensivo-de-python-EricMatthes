pessoas=['minha avó', 'minha mãe','meu pai']
#minha avó não irá jantar
pessoas_popped=pessoas.pop(0)
print(pessoas)

#adicionando minha madrinha
pessoas.append('minha madrinha')

#nova mensagem
message=f'Vamos jantar juntos, {pessoas[0]}?'
print(message)
message=f'Vamos jantar juntos, {pessoas[1]}?'
print(message)
message=f'Vamos jantar juntos, {pessoas[2]}?'
print(message)

print(f"{pessoas_popped} não irá jantar")




