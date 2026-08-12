#Criando a classe
class User:
    def __init__(self,first_name,last_name, height, weight):
        self.first_name=first_name
        self.last_name=last_name
        self.height=height
        self.weight=weight

    def describe_user(self):
        print(f"\nO usuário {self.first_name} {self.last_name} possui altura {self.height} e peso {self.weight}")

    def greet_uuser(self):
        print(f"Bem-vindo {self.first_name} {self.last_name}!")

#Atributos:
usuário=User('Diego','Souza','1,83m','70kg')
usuário.describe_user()
usuário.greet_uuser()