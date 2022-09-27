'''
JUEGO DE PIEDRA, PAPEL O TIJERA
'''

import random

print("Juego de Piedra, Papel o Tijera")

pc=random.choice(["piedra","papel","tijera"])
player=input("Elige una opcion \n")

if player=="piedra":
    if pc=="piedra":
        print("pc elige piedra, EMPATE")
    elif pc=="tijera":
        print("pc elige tijera, piedra rompe tijera, GANAS")
    else:
        print("pc elige papel, papel envuelbe piedra, PIERDES")
elif player=="tijera":
    if pc=="piedra":
        print("pc elige piedra, PIERDES")
    elif pc=="tijera":
        print("pc elige tijera, EMPATE")
    else:
        print("pc elige papel, tijera corata papel, GANAS")
elif player=="papel":
    if pc=="piedra":
        print("pc elige piedra, PIERDES")
    elif pc=="tijera":
        print("pc elige tijera, tijera corta papel, PIERDES")
    else:
        print("pc elige papel, EMPATE")
else:
    print("debes escribir en minusculas, sin espacios o numeros")
    