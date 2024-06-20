#escribir un programa que muestre los cuadrados
#un numero multiplicando por si mismo de los 60 primeros
#numeros naturales. resolverlo con while y for

i=1
while i <= 60:
    cuadrado= i*i
    print(f"el cuadrado del numero {i} es {cuadrado}")
    i += 1

i=1
for cuadrado in range(1,61):
    cuadrado= i*i
    print(f"el cuadrado de {i} es { cuadrado}")
    cuadrado+=1