#ejercicio de Supermercados Noé

import random
print("En Supermercados Noé estamos de aniversario y te obsequiamos un descuento en el valor de tu compra,\nSi es superior a 50.000 obtendras un descuento dependiendo de tu suerte:")
total=0
seguir="s"
while seguir=="s":
    precio=int(input("Ingrese el valor del producto\n"))
    cantidad=int(input("Ingrese la cantidad productos\n"))
    subtotal=precio*cantidad
    total=total+subtotal
    print(f"Van ${subtotal} de {cantidad} productos,\nRecuerda que para participar son $50.000")
    seguir=input("para agregar otro producto\nprecione S\nDe lo contrario preciona cualquier tecla\n").lower()
    
print(f"El valor total de la compra es ${total}")
compra=total
bolita=random.choice(["roja","azul","amarilla","blanca"])

if compra>=50000:
    print("DIA DE SUERTE") 
    if bolita=="roja":
        descuento=compra-compra*0.1
        print("bolita roja GANASTE 10% DTO, el total al pagar es $",descuento)
    elif bolita=="azul":
        descuento=compra-compra*0.3
        print("bolita azul GANASTE 30% DTO, el total al pagar es $",descuento)
    elif bolita=="amarilla":
        descuento=compra-compra*0.5
        print("bolita amarilla GANASTE 50% DTO, el total al pagar es $",descuento)
    elif bolita=="blanca":
        descuento=compra*0
        print("bolita blanca GANASTE TU COMPRA GRATIS el total es $",descuento)
else:
    print("tu compra es inferior a $50.000, \nLOS SIENTO NO PUEDES PARTICIPAR, O COMPRA MÁS!")

dinero=int(input("ingrese el valor con el que va a cancelar\n"))
if dinero >= descuento:
    vueltas=dinero-descuento
    print(f"Su cambio es ${vueltas}")
else:
    print("No tienes dinero suficiente,\n¡LLAMAREMOS A LA POLICIA!")




    

