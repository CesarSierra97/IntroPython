#definir una lista 

lista=[] # lista bacia 
lista2=[1,2,3,4]
lista3=[5,6,8]

print(lista2)
#muestra posicion especifica
print(lista2[2])
#Remplazar la posision
lista2[0]=4
print(lista2)

#Imprime la lista de forma vertical de 0 a x
for l in lista2:
    print(l)

#muestra la lista vertical con la pocicion index
for index, l in enumerate(lista3):
    print(index, l)

#Iteracion de dos listas
numeros=[1,2,3]
nombres=["amarillo","azul","rojo"]
for l1, l2 in zip(numeros, nombres):
    print(l1, l2)

#Dice la cantidad n que comnone la lista
print(len(nombres))
#Imprime horizonral normal
nombres.sort()
print(nombres)
#Imprime en orden contrario
numeros.sort(reverse=True)
print(numeros)
#Impirme la pocicion del elemtno de la lista
print(nombres.index("azul"))


