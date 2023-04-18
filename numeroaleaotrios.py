## generar una matriz que la vaya cargando con 10 numeros aleatorios
import random
num =[]

for v in range(10):
    num.insert(v,int(random.random()*100))
   

print(num)