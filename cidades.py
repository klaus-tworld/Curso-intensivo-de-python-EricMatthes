def describe_city(cidade,país='Brasil'):
    """Descreve uma cidade e país"""
    print(f"\n{cidade.title()} fica em {país.title()}")

describe_city('rio de janeiro')
describe_city(cidade='miami',país='estados unidos')
describe_city(país='canadá',cidade='toronto')