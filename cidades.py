cities={'rio de janeiro':{'country':'brasil','population':'+6M','fact':'perigosa'},
        'são paulo':{'country':'brasil','population':'+46M','fact':'feia'},
        'fortaleza': {'country':'brasil','population':'+2M','fact':'deserta'}
        }

for cidade,informação in cities.items():
    print(f"\n{cidade.title()}")
    país=f"{informação['country']}"
    população=f"{informação['population']}"
    fato=f"{informação['fact']}"

    print(f"-{país.title()}")
    print(f"-{população.title()}")
    print(f"-{fato.title()}")