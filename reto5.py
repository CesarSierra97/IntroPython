'''
En Supermercados Noé
'''

from ast import If
import random

print("En Supermercados Noé estamos de aniversario y te obsequiamos un descuento en el valor de tu compra, si ésta es mayor a 50.000 y dependiendo de tu suerte:")

compra=int(input("digite el valor total de su compra \n"))
bolita=random.choice(["roja","azul","amarilla","blanca"])

if compra>=50000:
    print("DIA DE SUERTE") 
    if bolita=="roja":
        total=compra-compra*0.1
        print("bolita roja GANASTE 10% DTO, el total al pagar es $",total)
    elif bolita=="azul":
        total=compra-compra*0.3
        print("bolita azul GANASTE 30% DTO, el total al pagar es $",total)
    elif bolita=="amarilla":
        total=compra-compra*0.5
        print("bolita amarilla GANASTE 50% DTO, el total al pagar es $",total)
    elif bolita=="blanca":
        total=compra*0
        print("bolita blanca GANASTE TU COMPRA GRATIS el total es $",total)
else:
    print("tu compra es inferior a $50.000, LOS SIENTO NO PUEDES PARTICIPAR, O COMPRA MÁS!")
    

