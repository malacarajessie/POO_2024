#Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
# y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

def es_lista(var):
    if isinstance(var, list):
        print(f"La variable {var} es una lista.")

def es_cadena(var):
    if isinstance(var, str):
        print(f"La variable '{var}' es una cadena.")

def es_entero(var):
    if isinstance(var, int):
        print(f"La variable {var} es un entero.")

def es_logico(var):
    if isinstance(var, bool):
        print(f"La variable {var} es un valor lógico (booleano).")

# Definimos las variables
mi_lista = [1, 2, 3]
mi_cadena = "Hola, mundo"
mi_entero = 42
mi_logico = True

# Llamamos a las funciones para cada variable
es_lista(mi_lista)
es_cadena(mi_cadena)
es_entero(mi_entero)
es_logico(mi_logico)