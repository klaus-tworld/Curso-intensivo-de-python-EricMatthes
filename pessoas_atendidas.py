class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f"O restaurante {self.restaurant_name} é bem localizado")
        print(f"{self.restaurant_name} tem uma culinária do tipo {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\nO restaurante {self.restaurant_name} está aberto!")

    def numero_servido(self):
        print(f"Os pedidos atendidos são de {self.number_served}")

    def set_number_served(self,pedidos):
        self.number_served=pedidos

    def increment_number_served(self,clientes):
        self.number_served+=clientes

restaurant=Restaurant('Jiló na Manteiga','Buffet')

restaurant.open_restaurant()
restaurant.describe_restaurant()

restaurant.numero_servido()
restaurant.set_number_served(50) 
restaurant.numero_servido()
restaurant.increment_number_served(55)
restaurant.numero_servido()

