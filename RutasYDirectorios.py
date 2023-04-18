


# copiar un arbol de directorio entero con su arhcivos y carpetas
import  shutil

origen="C:/Users/marco/Desktop/HelloGit"

destino="D:/copia"# no tiene que exisitir, si no dará error

shutil.copytree(origen,destino)
