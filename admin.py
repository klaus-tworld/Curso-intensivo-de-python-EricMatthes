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

class Admin(User):
    """Classe-filha admin"""
    def __init__(self, first_name, last_name, height, weight):
        super().__init__(first_name,last_name,height,weight)
        
        self.privileges=['can add post','can delete post','can ban user']

    def show_privileges(self):
        print(f"Os privilégio de {self.first_name} {self.last_name} são: ")
        for privilege in self.privileges:
            print(f"-{privilege}")

admin=Admin('Klaus', 'Augusto','182cm','77kg')
admin.describe_user()
admin.show_privileges()
        

    



