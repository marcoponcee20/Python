a={1,2,3}
#a.remove(3)#eliminar, si lo hacemos dos veces da error
#a.discard(3)#eliminar, discard ignora el fallo, no me da error
#a.add(4)# añadir solo un elemento
a.update({3,4})

# todos los numeros sin repetir
set1={1,2,3,4,4}.union({1,2,3,4,5,6,6,6})
set2= set1.union({7,8,9})
#print("Set1:", set1)
#print("Set2:",set2)


# un set con valores comunes en ambos sets
set1={1,2,3,4,4}.intersection({1,2,3,4,5,6,6,6})
set2= set1&({7,8,9})
print("Set1:", set1)
print("Set2:",set2)


# obtener los valores diferentes y excluir los repetidos
a = {'a','b','c','d'}
b={'d','e','f','g'}
print(a-b)
print(b.difference(a)) 

print(a^b)
print(b.symmetric_difference(a))

print(b.issuperset(a))#comprueba si todos los valores de b estan en a
print(b.isdisjoint(a))# si se repite un elemento de las dos comparaciones da false