#alcancia

repetir=input("Escriba S para iniciar el programa \n").lower()

alcancia=0
while repetir=="s":
    
    plata=int(input("Ingrese el valor a horrar \n"))
    alcancia=alcancia+plata

    if alcancia<=100000:
        repetir=input("Si desea continuar ahorrando presiones S, \ndelo contrario preciones N \n").lower()
    else:
        break
print(f"El total ahorrado fue de {alcancia} ")
