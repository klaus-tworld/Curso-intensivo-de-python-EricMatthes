def make_car(fabricante,modelo,**informação):
    carro={}
    carro["Fabricante"]=fabricante
    carro['Modelo']=modelo
    for key,value in informação.items():
        carro[key]=value

    return(carro)
    i
car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)

    