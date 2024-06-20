"""
list(array)
son colecciones o conjuntos de datos/valores bajo
un mismo nombre para acceder a los valores se hgace con un indice numerico 
nota: sus  alores so son modificados
la lista es una coleccion ordenada y modificable.
permite miembros duplicados 


#ejemplo 1 crear una lista con valores numericos enteros e imprimir la lista

numeros=(23,34)
print(numeros)
#recorrer la lista con un for
for i in numeros:
 print(i)

#recorrer la lista con un while
i=0
while i<len(numeros):
 print(numeros[i])
 i+=1

 #ejemplo 2 crea una lista de palabras psteriormente intgresar una palabra para buscar
 #la coicidencia en lista e indicar si aparece la palabra y en que posicion en el caso
 #contrario indicar una sola ves si no la encontro

 palabras=["hola","2024","10.23","true"]

 palabra_buscar=input("ingresa la palabra a buscar")

noencontro=True
for i in palabras:
  if palabra_buscar==i:
   print(f"encontre la palabra {palabra_buscar}, en la posicion {palabras.index (i)}")
   noencontro=False

if noencontro:
 print(f"no se encontro la palabradentro de la lista")


#i=0
#while i<len(palabras):
 #if palabra_buscar



#ejemplo 3 la lista multilinea o multidimensional (matriz) para  crear una agenda telefonica 

agenda= [
 ["cralos", 6181234567],
 ["fernando", 6182334567],
 ["matias", 6691112344],
 ["juan polainas", 6181342399]
]

print(agenda)

for i in agenda:
 print(f"{agenda.idex(i)+1}")
"""

 #ejemplo 4 crear un programa que permita gestionar peliculas, colkocar un menu de opciones para agragar, remover, consultar paliculas
 #notas
 #1. utilizar funciones y mandar a llamar desde otro archivo
 #2. utilizar listas para almacemar los nombres de las peliculas
def solicitarPeliculas():
    pelicula=input("ingrese la pelicula: ")
    peliculas.append(pelicula)
    #espereTecla()

def eliminarpelis():
    eliminar=input("ingrese la palicula a eliminar: ")
    eliminar.remove(peliculas)
   

    
    
peliculas=[]

print("\n\t..::: CINEEE :::... \n 1.- agregar \n 2.- eliminar \n 3.-consultar \n 4.- buscar \n 5.- salir ")
opcion=input("\t Elige una opción: ").upper()

if opcion=="1" or "AGREGAR":
    solicitarPeliculas()
elif opcion=="2" or "ELIMINAR":
    eliminarpelis()
#elif opcion=="3" or "CONSULTAR":