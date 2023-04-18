a=10

while a<10:
    print(a)
    if a ==5:
        print("Saliendo del bucle antes de tiempo")
        break
    a+=1



for a in range(0,9):
    print(a)
    if a ==5:
        print("Saliendo del bucle antes de tiempo")
        break


for indice, elemento in enumerate(['rojo','azul','verde','amarillo']):
    print(indice,'-',elemento)