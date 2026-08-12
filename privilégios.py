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

class Privileges:
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']

    def show_privileges(self):
            print(f"Os privilégio do admin são: ")
            for privilege in self.privileges:
                print(f"-{privilege}")


class Admin(User):
    """Classe-filha admin"""
    def __init__(self, first_name, last_name, height, weight):
        super().__init__(first_name,last_name,height,weight)
        self.privilege2=Privileges()
        print(f"Privilégios de {first_name} {last_name}")

admin=Admin('Klaus', 'Augusto','182cm','77kg')
admin.privilege2.show_privileges()


        