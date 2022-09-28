'''
Construya un programa que solicite las notas a evaluar (libre) en un
la materia de Programación con Python, el valor de cada una de
dichas notas debe ser de 0.0 a 5.0. Calcule el promedio de dichas de
notas para obtener la nota final y agregue las siguientes anotaciones
según corresponda:

✓ Si la nota es menor que 3.0 Reprobaste
✓ Si la nota está entre 3.0 y 4.0 Pasaste Raspando
✓ Si la nota es mayor que 4.0 Aprobaste con buenos resultados
'''
print("NOTA DEFINITIVA INTRO A PYTHON\nAcontinuación digite las notas obtenida y obtenga su definitiva")

lista=[]
definitiva=0
promedio=0
for i in range (0,5,1):
    nota=int(input("Digite la nota obtenida\n"))
    definitiva=definitiva+nota
    promedio=promedio+1
    lista.append(nota)
definitiva=definitiva/promedio

if definitiva<3:
    print("Estos dueron sus resultados")
    for l in lista:
        print(l)
    print(f"Su definitiva es {definitiva}\nREPROBADASTE*** :(")
elif 3<=definitiva<4:
    print("Estos dueron sus resultados")
    for l in lista:
        print(l)
    print(f"Su definitiva es {definitiva}\nPASATE RASPANDO***")
elif definitiva>4:
    print("Estos dueron sus resultados")
    for l in lista:
        print(l)
    print(f"Su definitiva es {definitiva}\n***APROBASTE MUY BIEN :D***")




