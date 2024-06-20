basico=0.987
intermedio=1.203

consumo=int(input("ingrese cual fue su consumo:  "))

if consumo<150:
    cobro=consumo*basico
    print(f"el cobro de su consumo fue {cobro}")
else:
    tarif1=150*basico
    tarif2=(consumo-150)*intermedio
    cobro=tarif1+tarif2
    print(f"el cobro de su consumo fue {cobro}")
IVA=0.16
subTotal=(cobro*IVA)+cobro
DAP=12.56
total=subTotal+DAP
print(F"su cobro final es:  {total}")
