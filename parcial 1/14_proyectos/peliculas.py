"""
#colocar todo lo que se hara
lista_peliculas = []
#entrada
def peliculas():
    peli = input("inserte nombre de la pelicula: \n")
    lista_peliculas.append(peli)
    return lista_peliculas

print("bienvenio al sistema de peliulas")
print("\n")
print("1-añadir pelicula al repertorio")
print("2-eliminar una pelicula del repertorio")
print("3-ver repertorio")
print("4-salir")
eleccion = input("selecciona una opcion: ")



if eleccion == "1":
    print(peliculas)
"""
"""1- añadir , 2- eliminar, 3- actualizar, 4- mostrar, 5- buscar, 6- salir
en eliminar debo de dar a opcion de su quiere eliminarla.
en actualizar debere buscar el nombre de una y dar la opcion de cambiarla
buscar es para darle busqueda a una pelicula
"""
from fun import *


juanito = False
while not juanito:
    print("bienvenido al sistema de peliculas")
    print("\n")
    print("1-agregar")
    print("2-eliminar")
    print("3-remplazar titulo")
    print("4-mostrar catalogo")
    print("5-buscar")
    print("6-salir")
    eleccion = input("selecciona una opcion: ").upper()
    
    clear_screen()

    if eleccion == "1" or eleccion == "AÑADIR":
        añairPeliculas()
    elif eleccion == "2" or eleccion == "ELIMINAR":
        remover_pelicula()
    elif eleccion == "3" or eleccion == "REMPLAZAR":
        remplazar()
    elif eleccion == "4" or eleccion == "VER":
        repertorio()
    elif eleccion == "5" or eleccion == "BUSCAR":
        print("no hay nada")
    elif eleccion == "6" or eleccion == "SALIR":
        salir()
        juanito = True
    else:
        print("opcion no encontrada, por favor seleccionar una opcion valida.")
        esperar_tecla()
    clear_screen()