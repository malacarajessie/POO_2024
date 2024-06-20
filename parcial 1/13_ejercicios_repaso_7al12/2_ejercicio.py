#Escribir un programa  que añada valores a una lista mientras que su longitud 
#sea menor a 120, y luego mostrar la lista: Usar un while y for

# Inicializamos una lista vacía
mi_lista = []

# Usamos un bucle while para añadir valores hasta que la longitud sea menor a 120
while len(mi_lista) < 120:
    # Añadimos un valor a la lista (por ejemplo, un número secuencial)
    mi_lista.append(len(mi_lista) + 1)

# Mostramos la lista utilizando un bucle for
for valor in mi_lista:
    print(valor)
