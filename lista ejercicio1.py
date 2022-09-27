baul=[]
seguir="s"
while seguir=="s":
    print()
    opcion=int(input("Que opcion deseas realizar\n"))

    if opcion==1:
        baul.append(input("ingresa el nombre de tu artiluco\n"))
    elif opcion==2:
        print("Estos son sus articulos")
    elif opcion==3:
        baul.pop()
        print(baul)
    elif opcion==4:
        
        print("Estos son sus articulos")
        baul.remove(input("indique el articulo que desea retirar\n"))
        print(baul)
    else:
        print("opsion incorrecta")

    seguir=input("si desea continuar digite S,\nDe lo contrario oprima cualquier tecla")
