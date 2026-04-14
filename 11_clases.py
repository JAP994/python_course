# Clases #

class Person:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.full_name = f"{name} {surname}"

    def get_name (self):
        return self.__name
    
    def get_surname (self):
        return self.__surname
    
    def walk(self):
        print(f"{self.full_name} Esta caminando")

my_person = Person("Jona", "Sanchez")
print(my_person.get_name())
print(my_person.get_surname())
print(my_person.full_name)
my_person.walk()