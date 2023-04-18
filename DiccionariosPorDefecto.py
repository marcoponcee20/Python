from collections import defaultdict

def valor_defecto():
    return "Ese elemento no existe en el diccionario"
    
usuario = defaultdict(valor_defecto)
usuario["ID"]=1
usuario["NOMBRE"]="MARCO "
usuario["APELLIDOS"]="PONCE"
usuario["EDAD"]=20


print(usuario["ID"])
print(usuario["NOMBRE"])
print(usuario["APELLIDOS"])
print(usuario["EDAD"])
print(usuario["DIRECCION"])
