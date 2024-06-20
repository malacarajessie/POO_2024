"""
Crear una lista y un diccionario con el contenido de esta tabla: 

  ACCION              TERROR        DEPORTES
  MAXIMA VELOCIDAD    LA MONJA       ESPN
  ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
  RAPIDO Y FURIOSO I  LA MALDICION   ACCION
"""

# Creación de la lista con el contenido de la tabla
tabla_lista = [
    ["ACCION", "TERROR", "DEPORTES"],
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]

# Creación del diccionario con el contenido de la tabla
tabla_diccionario = {
    "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
    "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
    "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
}

# Imprimir la información de la lista
print("Contenido de la lista:")
for fila in tabla_lista:
    print(fila)

# Imprimir la información del diccionario
print("\nContenido del diccionario:")
for categoria, peliculas in tabla_diccionario.items():
    print(f"{categoria}: {peliculas}")
