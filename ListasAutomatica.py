a=[1,2,3]
b=[7,8,9]
c=a+[4,5,6]+ b
a.extend(range(1,10))# una lista con el rango pasado por parentesis
#a.extend(range(4,10)) #una lista con el rango de inicio y fin
indice=a.index(3,2)
print(a)
print(indice)