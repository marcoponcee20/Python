##condicionales##

my_condition = False


if my_condition == False:
    print("Se ejecuta la condicion del if")## dentro del if

my_condition=1

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")


if my_condition > 10 and my_condition<20:
    print("Es mayor que diez y menor que 20")
elif my_condition == 1:
        print("Es 1")

else:
    print("Es menor o igual que 10 o mayor o igual que 20")

my_condition=""
if not my_condition:
     print("Mi cadena de texto es vacia")