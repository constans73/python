abecedario = "abcdefghijklmnopqrstuvwxyz"

frase = input ("Introduce una frase\n")
frase = frase.lower()
tupla = frase.split()
matriz = []
for i in range(len(tupla)):
	palabra = tupla[i]					#sacamos una palabra de una tupla de palbras
	tupla_numeros = []
	for i in palabra:
		letra = abecedario.index(i) + 1		#convertimos la palabra en una tupla en numeros
		tupla_numeros.append(letra)				
	matriz.append(tupla_numeros)
print (matriz)

						################		VAMOS A QUITAR CORCHETES DE LA TUPLA DE TUPLAS   Y PONER 
						################		ESPACIOS ENTRE LAS PALABRAS CONVERTIDAS A NUMEROS.		
for i in range(len(matriz)):
	numeros = matriz[i]				#   dividimos la tupla de tuplas en una tupla llamada numeros
	for numero in numeros:				#  elegimos el numero de nuestra tupla y abajo lo imprimimos
		print (numero, end="")			#  con   end=""   no hay saltos de carro
	print(end=" ")						#dejo espacio en blanco entre las palabras convertidas a numeros.
