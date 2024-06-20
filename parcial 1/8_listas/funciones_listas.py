paises=["mexico", "USA", "brasil", "china"]
numeros=[100,80, 3.1416, 75]
varios=["UTD", True, 100, 0.100]

#ordenar las listas 
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

#agregar elementis a las listas
print(numeros)
numeros.append(100)
print(numeros)
numeros.insert(len(numeros),200)
print(numeros)

#remover elementos
print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(2)
print(numeros)

#dar la buelta a los eelmentos de una lista

print(varios)
varios.reverse()

#buscra un valor dentro de una lista

encontro="brasil" in paises
print(encontro)

#vaciar una lista

print(paises)
paises.clear
print(paises)

#unir listas

print(varios)
varios.extend(numeros)
print(varios)