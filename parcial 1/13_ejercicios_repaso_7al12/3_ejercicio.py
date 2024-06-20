#Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
# palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir
# el contenido de la lista en mayusculas

mi_lista = []

# Comprobamos si la lista está vacía
if not mi_lista:
    print("La lista está vacía. Vamos a llenarla.")
    
    # Bucle para añadir palabras o frases a la lista
    while True:
        # Pedimos al usuario que introduzca una palabra o frase
        entrada = input("Introduce una palabra o frase (o 'fin' para terminar): ")
        
        # Si el usuario escribe 'fin', terminamos el bucle
        if entrada.lower() == 'fin':
            break
        
        # Añadimos la entrada a la lista
        mi_lista.append(entrada)

# Mostramos el contenido de la lista en mayúsculas
print("\nContenido de la lista en mayúsculas:")
for elemento in mi_lista:
    print(elemento.upper())

    