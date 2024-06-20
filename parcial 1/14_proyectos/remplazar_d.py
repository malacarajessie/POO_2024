def reemplazar_dato(lista, valor_a_buscar):
    # Verificar si el valor existe en la lista
    if valor_a_buscar in lista:
        # Obtener el índice del valor a buscar
        indice = lista.index(valor_a_buscar)
        
        # Solicitar al usuario el nuevo valor
        nuevo_valor = input(f"Ingresa el nuevo valor para reemplazar {valor_a_buscar}: ")
        
        # Reemplazar el valor en la lista
        lista[indice] = nuevo_valor
        print("Lista actualizada:", lista)
    else:
        print(f"El valor {valor_a_buscar} no se encontró en la lista.")

# Lista de ejemplo
mi_lista = [1, 2, 3, 4, 5]

# Buscar y reemplazar el valor
valor_a_buscar = int(input("Ingresa el valor que quieres buscar y reemplazar en la lista: "))
reemplazar_dato(mi_lista, valor_a_buscar)