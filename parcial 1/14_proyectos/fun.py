lista_peliculas = ["juan", "pedro"]

import os

def clear_screen():
    os.system('cls')

def añairPeliculas(): #1
    pelicula = input("inserte nombre de la pelicula: \n")
    if pelicula == lista_peliculas:
        print("la pelicula ya esta dentro del sistema")
    else:
        lista_peliculas.append(pelicula)
        print("pelicula añadida con exito")
    esperar_tecla()
   
def remover_pelicula():#2
    pelicula = input("pelicula a remover: ")
    seguro = input("desea remover la pelicula? SI/NO\n").upper()
    if seguro == "SI":
        if pelicula in lista_peliculas:
            lista_peliculas.remove(pelicula)
            print(f"¡{pelicula} ha sido removida de la lista de películas!")
        else:
            print(f"{pelicula} no se encuentra en la lista de películas.")
    esperar_tecla()

def repertorio():#4
    print("Peliculas en el repertorio:")
    for pelicula in lista_peliculas:
        print(pelicula)
    esperar_tecla()

def salir():#6
    print("saliendo del sistema")
    esperar_tecla()

def remplazar():#3
    peli = input("inserte pelicula a remplazar: ")
    if peli in lista_peliculas:
        indice = lista_peliculas.index(peli)
        remplazo = input(f"añadir el reemplazo de {peli}: ")
        desicion = input(f"estas seguro de reemplazar {peli} por {remplazo}? (S/N)").upper()
        if desicion == "S" or desicion == "SI":
         lista_peliculas[indice] = remplazo
         print("lista actualizada")
        else:
            print("cambio no hecho \n volviendo al menu")
            input("presione enter para continuar. ")
    else:
        print(f"{peli} no fue encontrada en el sistema")

def esperar_tecla():
    input("Presiona cualquier tecla para continuar...")