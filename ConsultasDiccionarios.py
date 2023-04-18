from operator import itemgetter


usuario=[{'id':1,'Nombre':'Marco','Apellidos':'Ponce ','Edad':20},
         {'id':2,'Nombre':'Fernando','Apellidos':'Perez','Edad':21},
         {'id':3,'Nombre':'Pedro','Apellidos':'Gomez','Edad':22},
         {'id':4,'Nombre':'Lucas','Apellidos':'López','Edad':23}]

# ordenamos de ascendente a descendente
ordena_id= itemgetter('id')
ordena_nombre= itemgetter('Nombre')
ordena_apellidos= itemgetter('Apellidos')
ordena_edad= itemgetter('Edad')
usuario.sort(key=ordena_edad)


# ordenamos de descendente a ascendente
usuario.reverse()

for y in usuario:
    print(y)
