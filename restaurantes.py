class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"O restaurante {self.restaurant_name} é bem localizado")
        print(f"{self.restaurant_name} tem uma culinária do tipo {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\nO restaurante {self.restaurant_name} está aberto!")

# Final do arquivo restaurantes.py
if __name__ == '__main__':
    restaurant = Restaurant('Jiló na Manteiga', 'Buffet')
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
