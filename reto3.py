'''
JUEGO DE TIRA LOS DADOS
'''

import random

print("Juego de los dados")

dado1=random.randint(1,6)
dado2=random.randint(1,6)

if dado1==1 and dado2==1:
    print("Un par de unos en los dados. GANASTE")
elif dado1==1 and dado2==2 or dado1==2 and dado2==1:
    print("Pateperro. GANASTE")
elif dado1+dado2==11:
    print("Sacaste 11. GANASTE")
elif dado1+dado2==12:
    print("Sacaste 12. GANASTE")
elif dado1+dado2==7:
    print("un total de 7. GANASTE")
else:
    print("PERDISTE CAYO",dado1,"y",dado2)
    