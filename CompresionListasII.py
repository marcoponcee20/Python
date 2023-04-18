a = [[50,34],[500,2,65],[76,80],[13],[55]]

b = sum(a,[])
c=sorted(b)
#print(c)



# 15 numeros aleatorios entre el 1 y el 10000
from random import randrange

a=[randrange(1,10000) for x in range(15)]

#print(a)


a= [x for x in range(91) if x % 9==0]
#print(a)



b =[x if x % 2 == 0 else "Descartado" for x in range(10)]

print(b)