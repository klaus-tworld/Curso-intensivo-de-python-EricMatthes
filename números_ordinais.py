numbers=list(range(1,10))
for number in numbers:
    if number==1:
        x='st'
    elif number==2:
        x='nd'
    elif number==3:
        x='rd'
    else:
        x='th' 
    print(f"{number}{x}")