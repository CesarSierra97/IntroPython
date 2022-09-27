
#contador
total=0
#acomulador
minutos=0

for i in range(1,5,1):
    precio=int(input("Digite el precio \n"))
    cantidad=int(input("Digite la cantidad \n"))
    subtotal=precio*cantidad

    total=subtotal+total
    print(f"subtotal: ${total}")

    minutos=minutos+1

print(f"El precio de su desayuno fue {total}")
print(f"por esta compra obtuviste {minutos} minutos de obsequio")
