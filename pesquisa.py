favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
    }
#Pessoas que deveriam participar da lista
pessoas=['carlos','jen','roberta']
for pessoa in pessoas:
    if pessoa in favorite_languages.keys():
        print(f"{pessoa.title()} obrigado por responder!")
    else:
        print(f"{pessoa.title()}, poderia responder?")