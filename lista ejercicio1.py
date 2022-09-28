from re import A, X


baul=["Balon","Sombrero"]
seguir="s"
while seguir=="s":
    print("LISTA DE ARTICULOS MODIFICABLE\nSeleccione una opción.\n \n1.Ingresar un articulo\n2.Ver lista de articulos\n3.Eliminar el ultimo articulo\n4.Verificar lista y seleccionar un articulo para eliminar\n ")
    opcion=int(input("¡Que opcion deseas realizar?\n"))

    if opcion==1:
        baul.append(input("ingresa el nombre de tu artiluco\n"))
    elif opcion==2:
        print("Estos son los articulos de tu baul")
        baul.sort()
        print(baul)
    elif opcion==3:
        print("Vas a eliminar el articulo",baul[-1])
        baul.pop()
        print(baul)
    elif opcion==4:
        for index, b in enumerate(baul):
            print(index,b)
        op=input("Si requiere eliminar alguno presione s\nDelo contrario oprima cualquier tecla")
        if op=="s":
            #PREGUNTAR POR QUE SE OBSTRUYE EL ESPACIO O NO FUNCIONA EL OTRO????
            a=int(input("ingrese el index que desea borrar\n"))
            del baul[a]
            #baul.remove(int(input("indique numero del articulo que desea retirar\n")))
            print("El baul quedo asi ",baul)
            
    else:
        print("opsion incorrecta")

    seguir=input("si desea continuar digite S,\nDe lo contrario oprima cualquier tecla\n").lower()
