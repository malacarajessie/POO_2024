# ciclo for estructura interactiva que se ejecuta x veces
#     sintaxis
# for variable in elemento_iterable (lista, rango, etc.):
# bloqie de instrucciones

#ejemplo 1 crear un programa que se imprima en pantalla 5 veces el @


for contador in range(1,6):
    print("@")
    print("hola")

#ejemplo 2 crear un programa que imorima los numeros del 1 al 5 y los sume y al final immprima la suma


suma=0
for contador in range(1,6):
    print(contador)
    suma+=contador


print("la suma es: {suma}")

#ejercicio 3 crear un programa que imprima la tabla de multiplicar que el usuario desee

tabla=int(input("ingresa un numeri para calcular se tabla de multiplicar: "))


multi=0

for i in range(1,11):
    multi=tabla
    print(f"{tabla}X {i}={multi}")