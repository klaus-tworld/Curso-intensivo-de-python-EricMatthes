palavras={'del':'deletar algo',
          'sort':'colocar em ordem alfabética',
          'append':'adicionar algo no final',
          'for':'percorrer um loop',
          'if':'condicional'}

#Loop para percorrer as chaves-valor
for k,v in palavras.items():
    print(f"O valor da chave é {k.title()}, enquanto o da palavra é: {v.title()}")
