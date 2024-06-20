nombre=input("nombre del paciente: ")
sangre=input("ingrese el tipo de sangre del paciente: ")

presion=1
presis=0
predia=0
for presion in range(1,4):
    presis = int(input(f"Ingresa el valor {presion} de la presion SIStolica:  "))
    presis+=1
    predia=int(input(f"ingresa el valor {presion} de la presion diastolica:  "))
    predia+=1

mFinal=int(input("ingresa la medicion final obtenida al final del dia"))   

promsis=presis/3
print(f"el promedio de su presion sistolica es {promsis}")
promdia=predia/3
print(f"el primedio de su presion diastolica es {promdia}")

Final=(promsis+promdia+mFinal)/3
print(f"Su presion arterial final es: {Final}")

