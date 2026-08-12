class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"\nO restaurante {self.restaurant_name} é bem localizado")
        print(f"{self.restaurant_name} tem uma culinária do tipo {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\nO restaurante {self.restaurant_name} está aberto!")

restaurant_1=Restaurant('Jiló na Manteiga','Buffet')
restaurant_2=Restaurant('Moccelin','Frutos do mar')
restaurant_3=Restaurant('Kazu','Comida japonesa')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()