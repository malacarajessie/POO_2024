#manejo de errores es la forma en la que tienen los lenguajes de programacion
#para evitar que sucedan errores en tiempo de ejecucion

#EJEMPLO 1 error cuando una variable no se genera

try:
 nombre=input("dame el nombre:  ")

 if len(nombre)>1:
    nombre_usuaro="el nombre es: "+nombre

 print(nombre_usuaro)
except:
 print("es necesario introducir un nombre de ususario...")

#EJEMPLO 2 cuando se solicita un numero y se introduce una letra   #VALUeEROOR

try:
 numero=int(input("dame un numero:  "))

 if numero>0:
   print("soy un numero entero positivo")
 elif numero:
  print("soy un numero entero negativo")
except:
  print("no se puede convertir un caracter no numerico a numerico ") #excep se utiliza solo cuando hay errores (puedo hacer dentro lo que quiera)
else:
  print("toso se ejecuto sin errores")

  #EJEMPLO 3 cyando se generan multiples excepciones

try:
  numero=int(input('dame un numero:  '))

  print("el cuadrado es: "+str(numero*numero))
except ValueError:
  print("un numero no se puede convertir un  caracter que no sea numerico")
except TypeError:
  print("no es posible convertir el numero a entero")
else:
  print("finalizo correctamente")
finally:
  print("listo se termino")