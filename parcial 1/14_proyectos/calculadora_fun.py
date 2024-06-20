#calculadora con funciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."
def potencia(a,b):
    return pow(a,b)

def raiz(a,b):
    return  


def calculadora():
    while True:
        print("Calculadora básica \n")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. potencia")
        print("6. raiz")
        print("7. Salir \n")
opc = input("Elige la operación que quieres realizar: ")
if opc in ["1", "2", "3", "4"]:
            n1 = float(input("Introduce el primer número: "))
            n2 = float(input("Introduce el segundo número: "))

if opc == "1":
                print(f"{n1} + {n2} = {sumar(n1, n2)}")
elif opc == "2":
                print(f"{n1} - {n2} = {restar(n1, n2)}")
elif opc == "3":
                print(f"{n1} * {n2} = {multiplicar(n1, n2)}")
elif opc == "4":
                print(f"{n1} / {n2} = {dividir(n1, n2)}")
elif opc == "5":
                print(f"{n1} ** {n2} = {potencia(n1, n2)}")
elif opc == "6":
                print(f"{n1} ^ {n2} =")
elif opc == "7":
            print("programa finalizado")

else:
 print("Opción no válida. Por favor, elige una opción válida.")

calculadora()