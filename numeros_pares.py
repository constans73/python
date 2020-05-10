lista = []
for i in range(101):
	lista.append(i)
print (lista[0::2])			#aqui lo imprimimos con corchetes

##################   VAMOS A HACERLO SIN CORCHETES    ##########################


lista = lista[0::2]
for i in range(len(lista)):
	print (lista[i], end=" ")
