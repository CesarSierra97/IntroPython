from cgi import print_arguments


onces=["hamburguesa","sandich","pizza"]
#agregar en posisicon especifica 1 solo dato
onces.insert(2,"Empanadas")
#agregar un elemnto al final de la lista un solo elemto
onces.append("malteadas")
#agregar al final varios elementos
onces.extend(["chorizo","perro caliente"])

#agregar al final varios elementos
onces.extend(["chorizo","perro caliente"])

#borrar elemtnos de lista
onces.remove("Empanadas")
print(onces)

'''
del onces[1:4]
print(onces)
'''
#borrar ultimo elento de la lista
onces.pop()
print(onces)

#Limpiar la lista
onces.clear()


#mostrarme la posision del elemento
print(onces.index("hamburguesa"))