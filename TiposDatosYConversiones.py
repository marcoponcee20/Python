
# ver si una variable booleana es verdadera o falsa

a = False
if a is True:
    print("True")
else:
    print("False")
# conversion de str a int
    b="10"
    b= int (b)
    print(type(b))

    # de int a str
    b=10
    b= str(b)
    print(type(b))

    # de float a int
    b=10.65
    b= int(b)
    print(type(b))
    print(b)

    # conversion con listas y tuplas y set, se hacen las tres iguales

    a = "Programacion facil"
    b = tuple(a)
    print (type(b),b)