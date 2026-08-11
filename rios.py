rios={'nilo':'egito','amazonas':'brasil','gandhi':'índia'}
for rio,país in rios.items():
    print(f"O rio {rio.title()} atravessa o país {país.title()}\n")
for rio in rios.keys():
    print(f"Um dos rios é {rio.title()}\n")
for país in rios.values():
    print(f"Um dos países é {país.title()}\n")
        

