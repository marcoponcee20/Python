## sets ##

my_set= set()
my_other_set={}
print(type(my_set))
print(type(my_other_set))#nos dice que inicialmente es un diccionario, porque está vacio


my_other_set={"Marco","Ponce",35} # si rellenamos el set, ya nos muestra como que es un set
print(type(my_other_set))


print(len(my_other_set))
my_other_set.add("SRMLK")# un set no admite repetidos
my_other_set.add("SRMLK")# un set no admite repetidos, lo pone en otro orden distinto cada vez
print("Marco" in my_other_set)# comprueba si existe o no ese elemento en el set
print("Pepe" in my_other_set)
#elimino
my_other_set.remove("Ponce")
print(my_other_set)

#borrar todo
my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

my_set={"Brais","Moure",35}


#transformamos el set en una list
my_list=list(my_set)
print(my_list[0])
my_other_set={"Marco","Ponce",35}
#juntamos con el union los dos sets
my_new_set= my_set.union(my_other_set)
print(my_new_set)


print (my_new_set.difference(my_set))
