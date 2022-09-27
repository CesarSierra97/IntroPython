

total=0
for i in range(0,3,1):
    precio=int(input("Digite el precio \n"))
    cantidad=int(input("Digite la cantidad \n"))
    subtotal=precio*cantidad
    total=subtotal+total
    print(f"subtotal: ${total}")

print(f"El precio de su desayuno fue {total}")

