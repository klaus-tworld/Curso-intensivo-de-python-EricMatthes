class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"O restaurante {self.restaurant_name} é bem localizado")
        print(f"{self.restaurant_name} tem uma culinária do tipo {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\nO restaurante {self.restaurant_name} está aberto!")

#Classe-filha
class IceCreamStand(Restaurant):
    """Tentativa de representar uma sorveteria"""
    def __init__(self,restaurant_name, cuisine_type, flavors=" "):
        """Armazena os sabores da sorveteria"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=flavors

#Sabores da sorveteria        
    def mostrar_sabores(self):
        """Sabores que tem a sorveteria"""
        self.mostrar_sabores=self.flavors
        sabores=['maracujá','manga','pistache']

        for sabor in sabores:
            print(f"Temos o sabor: {sabor} ")

#Teste
sorvete=IceCreamStand('Sergel','Sorveteria')
sorvete.mostrar_sabores()