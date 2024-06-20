#1. Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

 #a.- Recorrer la lista y mostrarla
 #b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 #c.- ordenarla y mostrarla
 #d.- mostrar su longitud
 #d.- mostrar su longitud

print("\nt..::LISTAS::..\n a.- Recorrer la lista y mostrarla \n b.- hacer una funcion que recorra la lista de numeros y devuelva un string \n c.- ordenarla y mostrarla \n d.- mostrar su longitud \n d.- mostrar su longitud")
opcion=input("\t Elije una opcion :") .upper()

nums=[10,20,30,40,50,60,70,80]

def mostrar(lista):  #a
    for numero in lista:
        print(nums)

print("a. recorrer y mostrar lista:")
mostrar(nums)

def recorrer_lista(lista):  #b
    return ",".join(map(str,lista))

recorrer_lista(nums)
print("\n la lista convertida a string: ")
print(recorrer_lista)
       
numeros_ordenados = sorted(nums)
print("\nc. Lista ordenada:")
mostrar(numeros_ordenados)

# d. Mostrar su longitud
print("\nd. Longitud de la lista:")
print(len(nums))

def buscar(lista,elemento):
    if elemento in lista:
        return f"el elemento{elemento}se encuentra en la lista"
    else:
        return f"el elemento {elemento} NO se encuentra en la lista"
elemento_a_buscar = int(input("\ne. Introduce un número para buscar en la lista: "))
resultado_busqueda = buscar(nums, elemento_a_buscar)
print(resultado_busqueda)