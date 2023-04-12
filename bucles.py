##bucles##

#while
my_condition=0
while my_condition < 20:
        my_condition+=1
        if my_condition == 15:
             print("Se detiene la ejecución")
             break
        print(my_condition)

print("la ejecucion continua")



# for
my_list= [10,20,30,40,50,60,70,80,90,100]
print("Se van a mostrar los elementos de la lista:")
for element in my_list:
       print(element)
else: 
       print("El bucle for ha finalizado")




my_dict = {"Nombre":"Marco", "Apellido": "Ponce", "Edad":20, 1:"Python"}
for element in my_dict.values():
       print(element)
       if element == 20:
              continue