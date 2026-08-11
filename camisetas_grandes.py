def make_shirt(estampa, tamanho='grande'):
    """Mostra o tamanho e o que deve ser colocado na estampa"""
    print(f'\nQuero a camisa tamanho {tamanho}')
    print(f"A estampa será '{estampa}'")

make_shirt('Eu amo Python')
make_shirt(tamanho='médio', estampa='Eu amo Python')
make_shirt(tamanho='pequeno',estampa='Apenas viva')
