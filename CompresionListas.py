
# x va cambiando según el valor que le metamos en la lista

potencias=[x*x for x in(1,2,5,10,50)]
print(potencias)



#otra forma mas larga de hacerlo 
potencias2=[]


for x in(1,2,5,10,50):
    x=x*x
    potencias2.append(x)


print(potencias2)

colores =["rojo","azul","verde","amarillo"]

colores_mayuscula=[x.upper() for x in colores]

print(colores_mayuscula)

# eliminar los puntos
l1=[x.strip(".")for x in ["hola.","me.","llamo.","Marco."]]
print(l1)

#

l2=[x if x in 'pny'else ' caracter no encontrado' for x in 'python']

print(l2)