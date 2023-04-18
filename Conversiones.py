def convierte():
    numero=input("Introduce un numero:\n")
    sistema=int(input('Introduce un sistema de conversión\n'))
    print(int(numero,sistema))


#convierte()



def binario_decimal():
     numero=int(input("Introduce un numero:\n"))
     convertido=bin(numero)
     print(convertido)


#binario_decimal()


def octal_decimal():
     numero=int(input("Introduce un numero:\n"))
     convertido=oct(numero)[2:]
     print(convertido)

#octal_decimal()

def hexadecimal_binario():
     numero=int(input("Introduce un numero:\n"))
     convertido=hex(numero)[2:]
     print(convertido)

hexadecimal_binario()


