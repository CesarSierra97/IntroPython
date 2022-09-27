#JUEGO DE CARA Y SELLO

import random
print("BIENVENIDOS AL CASSINO DEL SENNA\nJuego de CARA o SELLO, Le apuestas?")
seguir="s"
total=0
ronda=0
while seguir=="s":
    apuesta=int(input("Ingrese el valor a apostar\n"))
    player=input("Que eliges CARA o SELLO\n").lower()
    pc=random.choice(["cara","sello"])
    if pc==player:
        apuesta=apuesta*2
        total=total+apuesta
        print(f"FELICIDADES GANASTE, LLEVAMOS ${total}")            
        ronda=ronda+1
    elif pc=="cara" and player=="sello" or pc=="sello" and player=="cara":
        total=total-apuesta
        print(f"Los siento perdiste :(\nTe quedan en total ${total}")
        ronda=ronda+1
    else:
        print(f"¡Los valores ingresados son incorrectos!\n***Recuerda escribir, CARA o SELLO***\nLlevas en acomulado un total de ${total}")
        ronda=ronda+1
    seguir=input("¿VOLMEMOS APOSTAR?\nSi desea volver a jugar digite S\nDe lo contrario oprecione cualquier tecla\n").lower() 
print(f"Obtuviste total ${total} en {ronda} rondas wey, echale ganas!")


