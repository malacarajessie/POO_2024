#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

def mostrar_numeros_entre():
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    if num1 <= num2:
        for numero in range(num1, num2 + 1):
            print(numero)
    else:
        for numero in range(num1, num2 - 1, -1):
            print(numero)
mostrar_numeros_entre()
