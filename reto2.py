'''
DEFINIR LA DOSIS PARA EL BEBE
'''

meses=int(input("Por favor ingrese la edad de su bebe, en meses \n"))
peso=int(input("Por favor ingrese el peso en Kg \n"))
formula=(peso+10/meses*10)*8
print("La dosis correcta que debe aplicar es de",formula,"ml")
