##funciones##

def my_function():
    print("Esto es una función")


my_function()


def sum_two_values(first_number: int , second_number: int ):
    print(first_number+second_number)



sum_two_values(20,30)


def sum_two_values_with_return(fv, sv):
   my_sum=fv+sv
   return my_sum

my_result= sum_two_values_with_return(10,5)
print(my_result)

def print_name(n,s):
    print(f"{n} {s}")


print_name(n="Marco", s= "Ponce")


def print_name_with_default(n,s,a = "Sin alias"):
    print(f"{n} {s} {a}")


print_name_with_default("Marco", "Ponce")


def print_texts(*text):
    print(text)


print_texts("Hola","Marco","Ponce","Gomez")
