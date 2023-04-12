##listas##

my_list = list()
my_other_list=[]



my_list=[35,24,62,52,30,30]
print(my_list)

my_other_list = [35,1.77,"Brais", "Moure"]
print(my_other_list)


#print(my_list+my_other_list)


# añadir al final de la lista este elemento
my_list.append("QuetesSL")
print(my_list)


#añade el elemento que queramos en la posicion que queramos 
my_list.insert(1,"Azul")
print(my_list)

my_list[1]="Rojo"
print(my_list)

# eliminar el elemento en concreto que queramos
my_list.remove(30)
print(my_list)

#no muestra  el ultimo elemento apilado , o bien si le pongo un numero en el parentesis, no muestra ese elemento

print(my_list.pop())
print(my_list)

my_pop_element= my_list.pop(2)
print(my_pop_element)
print(my_list)


#eliminar por indice
del my_list[2]
print(my_list)

# creo una nueva lista, y copio los datos de una en otra, con el clear borro los datos de esa, y lo mostramos
my_new_list= my_list.copy()
my_list.clear()
print(my_list)
print(my_new_list)

# imprime los valores justo al reves
my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

