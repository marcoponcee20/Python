
import re


try:
    palabra=input("Introduce la palabra que quieras buscar:\n")
    with open('C:/Users/marco/Desktop/Archivo.txt','r' , encoding="utf-8") as texto:
       for x in texto:
           buscar=re.search(palabra,x)
    if buscar:
        print("Se ha encontrado la palabra " , palabra)
    else:
        print("No  se ha encontrado la palabra " , palabra)

  
except FileNotFoundError:
    print("El archivo no existe")
