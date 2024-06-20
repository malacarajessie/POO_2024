"""

una funcion es un conjunto de instrucciones agrupadas bajo
un nombre en particular como un origrama mas peque
que cumple una funcion especifica. la funcion se puede reutilizar 
con el simple hecho de invocarla es decir mandarla llamar

sintaxis: def nombredeMifuncion(parametros):
bloque o conjunto de instrucciones

sintaxis: def nombredeMifuncion(parametros):

las funciones pueden ser de 4 tipos 
1. funcion que no recibe parametros y no regresa valor
2. funcion que no recibe parametros y regresa valor
3. funcion que recibe parametreos y se regresa el valor
4. funcion que recibe parametros y regresa valor
"""

# 1. funcion que no recibe parametros y no regresa valor

def sumaNumeros():
    n1=int(input("numero #1:"))
    n2=int(input("numero #2:"))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")
    sumaNumeros()

#2. funcion que no recibe parametros y regresa valor
def sumaNumeros2():
     n1=int(input("numero #1:"))
     n2=int(input("numero #2:"))
     suma=n1+n2
     return f"{n1}+{n2}={suma}"
    
print(sumaNumeros2())

#3. funcion que recibe parametreos y se regresa el valor

def sumaNumeros3(n1,n2):
     suma=n1+n2
     print(f"{n1}+{n2}={suma}")
    
    



#crear un programa que solicita a traves de una funcion la siguiente info
#nombre del\paciente, edad, estatura, tipo de sangre 
#utilizar los 4 tipos de funciones