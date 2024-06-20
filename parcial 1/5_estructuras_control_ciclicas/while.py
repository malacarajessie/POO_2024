# ciclo while estructura interactiva que se ejecuta x veces siempre y cuando la condicion se cumpla y se ejecutara tantas veces como sea
#tru la cindicion
#     sintaxis
#ehile condition:
# for variable in elemento_iterable (lista, rango, etc.)
# bloqie de instrucciones

#ejemplo 1 crear un programa que se imprima en pantalla 5 veces el @

contador=1
while contador <=5:
    print("@")
    contador+=1

#ejemplo 2 crear un programa que imorima los numeros del 1 al 5 y los sume y al final immprima la suma

contador=1
suma=0

while contador<=5:
     print(contador)
     suma+=contador
     contador+=1



# print("la suma es: {suma}")

# #ejercicio 3 crear un programa que imprima la tabla de multiplicar que el usuario desee
tabla=int(input("ingresa un numeri para calcular se tabla de multiplicar: "))
i=1 
multi=0

while i<=10:
     multi=i*tabla
     i+=1
     print(f"{tabla}X {i}={multi}")