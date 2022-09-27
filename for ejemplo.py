#capturar 10 datos y preguntar si es hombre o mujer determinar cuantos hombre y mujeres ahi 

h=0
m=0
for i in range(0,10,1):   
    genero=input("Escribe H si eres hombre \nEscribe M si eres mujer \n").lower()
    if genero=="h":
        h=h+1
        print(f"Van {h} hombres ")
    elif genero=="m":
        m=m+1
        print(f"van {m} mujeres ")
    else:
        print("mal digitado solo debes escoger M o H")
print(f"En total hay {h} hombre y {m} mujeres")






   
