a={'Nombre' : 'Javier'}
b={**a}
c={**a,**b}
# pegar un diccionario con otro, ahora mismo el diccionario c tiene lo mismo que el b, y el b lo mismo que el a
#print(c)


d={"Nombre": "Enrique", "Apellido":"Ponce"}
for x,y in d.items():
    print(x,':', y)



print(a['Nombre'])