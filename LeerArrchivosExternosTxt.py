
try:
    with open('C:/Users/marco/Desktop/Archivo.txt','r' , encoding="utf-8") as texto:
        lectura = texto.readlines()


    #print(lectura)
except FileNotFoundError:
    print("El archivo no existe")



# abrir un archivo con un bucle for


try:
    with open('C:/Users/marco/Desktop/Archivo.txt','r' , encoding="utf-8") as texto:
       for linea in texto:
           print(linea)


  
except FileNotFoundError:
    print("El archivo no existe")
