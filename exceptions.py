##exceptions##
numberOne = 5
numberTwo = 1
numberTwo="1"
# try except else finally

try:
        print(numberOne+numberTwo)
        print("No se ha producido un error")
except:
      # el error que salta
      print("Se ha producido un error")
else: 
       # se ejecuta si no se produce una excepción
       print("La ejecución continúa correctamente")
finally: 
       # se ejecuta siempre pase lo que pase
       print("La ejecución continúa")


#captura de exepciones por tipo
try:
        print(numberOne+numberTwo)
        print("No se ha producido un error")
except ValueError:
      #captura el error de tipo valor, es decir, un valor mal inapropiado
      print("Se ha producido un error por el valor de dato")
except TypeError as error :
      #captura el error de tipo, es decir has metido un string en una suma de numeros
      print(error)

except Exception as my_random_error_name:
       print(my_random_error_name)
