#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

num1=int(input("ingrese un numero: "))
num2=int(input("ingrese un numero: "))

if num1 > num2:
        num1, num2 = num2, num1
    
for numero in range(num1, num2 + 1):
        if numero % 2 != 0:
            print(numero)