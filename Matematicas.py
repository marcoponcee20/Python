import operator, math
a,b=10,15
print(operator.add(a,b))
print(operator.iadd(a,b))

print(operator.sub(a,b))
print(operator.isub(a,b))

print(operator.mul(a,b))
print(operator.imul(a,b))

print(operator.truediv(a,b))
print(operator.itruediv(a,b))

print(10%2)
a =cociente, resto = divmod(10,2)
print(a)

a,b,d = 2,10,20
c=pow(a,b,d)
print(type(c),c)

a = math.sqrt(10)
print(a)