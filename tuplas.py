## tuplas##

# no se puede modificar, una vez que metes los valores no puedes cambiarlos por otros, es decir, inmutable


my_other_tuple= (35,60,30) # si escrimos solo parentesis es una tuple si no es una lista

my_tuple =(35,1.77,"Brais","Moure")
print(type(my_tuple))


print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Brais"))# nos dice cuantos con ese nombre existen

print(my_tuple.index("Moure"))# nos dice el indice donde se encuentra Moure

print(my_tuple + my_other_tuple) # mostramos las dos tuplas al mismo tiempo

my_sum_tuple = my_other_tuple+my_tuple # creo una variable donde esten las dos tuplas juntas y la muestro
print(my_sum_tuple)

my_tuple=list(my_tuple) # cambio mi tupla a una lista, y ya puedo hacer todas las operaciones que hace una lista
print(type(my_tuple))
