"""
print("\nt..::CALCULADORA BASICA::..\n 1. suma \n 2. resta \n 3. mjultiplicacion \n 4. division")
opcion=input("\t Elije una opcion :") .upper()

n1=int(input("numero #1:"))
n2=int(input("numero #2:"))

if opcion=="1" or opcion=="+" or opcion=="suma":
    print(f"{n1}+{n2}={n1+n2}")
elif opcion=="2" or opcion=="-" or opcion=="resta":
    print(f"{n1}-{n2}={n1-n2}")
elif opcion=="3" or opcion=="*" or opcion=="multiplicacion":
    print(f"{n1}*{n2}={n1*n2}")
elif opcion=="4" or opcion=="/" or opcion=="divicion":
    print(f"{n1}/{n2}={n1/n2}")
else:
    print(f"gracias por utilizar el sistema...")
"""

import os

def solicitarNumeros():
    global n1,n2
    n1=int(input("Numero # 1:"))
    n2=int(input("Numero # 2:"))

def calculadora(n1,n2,opcion):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        
        return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
        return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
       
        return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
        return f"{n1}*{n2}={n1/n2}"

os.system("cls") #Limpiar pantalla 

opcion=True
while opcion:
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()
    if opcion!="5":
     solicitarNumeros()
     print(calculadora(n1,n2,opcion))
    else:
     opcion=False
     print ("Gracias por utilizar el sistema ...")