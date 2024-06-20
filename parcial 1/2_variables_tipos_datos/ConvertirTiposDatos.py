"""
comentario de varias lineas
nota: a la hora concatenar no es posible incliur en algunas 
ocaciones contenido de variables que no sean el tipo str
"""

#comentario de una linea

#cancatenae un str con str

texto="soy unba cadena de texto"
numero=23

print(texto+" y soy otra cadena")

#cancatenae un int con str

numero=23
numero_str=str(numero)
print("el numero: "+ numero_str)


print("el numero: "+str(numero))

#concatenar en str con int

n1='23'
n2=33

suma=int(n1)+n2
print("el numero: "+str(suma))

#concatenar en float y int con str

n1='23'
n2=33.0

suma=int(n1)+n2
print("el numero: "+str(suma))
print(f"el numero: {suma}")

#concatenar in float y float con float

n1='23.34'
n2='23.99'

suma= float(n1)+float(n2)

print(f"el numero: {suma}")