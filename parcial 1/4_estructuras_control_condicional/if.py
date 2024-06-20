# #existe una estructura de condicion llama "if" la cual evalua una cindicion para encintrar el vLOOR "TRUE"
# #Y SI SE CUMPLE LA CONDICIOn se ejcuta la linea o lineas

# #ejemplo 1. if simple

# color=input("ingresa un color: ")

# if color=="rojo":
#     print('soy el color rojo')

#     #ejemplo 2 if compuesto
# color=input("ingresa un color: ")

# if color=="rojo":
#     print('soy el color rojo')
# else:
#     print("no soy el color rojo soy otra cosa")


# #ejemplo 3 if anidado
# color=input("ingresa un color: ")

# if color=="rojo":
#     print('soy el color rojo')
# elif color=="amarillo":
#        print("soy el color amarillo")
# elif color=="azul":
#      print('soy el color azul')       
# elif color=="morado":
#      print('soy el color morado')
# else:
#      print("no soy ninguno de los anteriores")   

   
    #ejemplo 4 crear un programa que solcicite el num de la semana e imprima en pantalla el dia uq ele corresponde

dia=int(input("ingresa un dia de la semana (1-7)"))
if dia==1:
     print("lunes")
elif dia==2:
     print('martes')
elif dia==3:
     print('miercoles')
elif dia==4:
     print('jueves')
elif dia==5:
     print('viernes') 
elif dia==6:
     print("sabado")
elif dia==7:
     print('domingo')  
else:
     print("no soy ninguno de los anteriores")
     