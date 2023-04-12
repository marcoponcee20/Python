##clases##


class MyEmptyPerson: 
    pass 







class Person:
    def __init__(self,name,surname):# constructor de la clase
        self.full_name= f"{name} {surname}"
        self._name = name # privado

    def get_name(self):
            return self._name
    
    def walk(self):
        print(f"{self.full_name} está caminando")
    pass

my_person = Person("Marco","Ponce")
print(my_person.full_name)
print(my_person._name)
print(my_person.get_name())
my_person.walk()