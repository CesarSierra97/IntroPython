#definir una lista 

lista=[] # lista bacia 
lista2=[1,2,3,4]

print(lista2)
print(lista2[2])
lista2[0]=4

for l in lista2:
    print(l*2)

for index, l in enumerate(lista2):
    print(index, l)


numeros=[1,2,3]
nombres=["amarillo","azul","rojo"]
for l1, l2 in zip(numeros, nombres):
    print(l1, l2)

print(len(nombres))
nombres.sort()
print(nombres)

#al contrario
numeros.sort(reverse=True)
print(numeros)

print(nombres.index("azul"))


