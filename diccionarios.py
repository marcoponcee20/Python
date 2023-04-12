## dicionarios##

my_dict = dict()
my_other_dict={}


my_other_dict = {"Nombre":"Marco", "Apellido": "Ponce", "Edad":20, 1:"Python"}
my_dict = {"Nombre":"Marco",
            "Apellido": "Ponce",
            "Edad":20,
            "Lenguajes":{"Python","Swift","Kotlin"}
            }
print(my_dict)
print(my_dict["Nombre"])
#añadimos un elemento
my_dict["Calle"] ="Calle marco"
print(my_dict)


#borramos el elemento 
del my_dict["Calle"]
print(my_dict)


print("Nombre" in my_other_dict)

print(my_dict.items())# nos da  los items
print(my_dict.values()) # nos da los valores
print(my_dict.keys()) # nos da un listado con nombre apellido etc etc
my_new_dict = dict.fromkeys(("Anios","Piso"))
print(my_new_dict)

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))