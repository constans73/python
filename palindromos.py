#Dado una lista de frases ingresadas por el usuario, mostrar en pantalla todas aquellas que sean palíndromo.


"""
Ejemplos:

Dábale arroz a la zorra el abad
Yo hago yoga hoy
Sí, lo sé Solís
"""


lecturas=[]
fin_frases=True
nun_frases = 0


while fin_frases == True:
	lectura = input("Ingresa una frase:")
	lecturas.append(lectura)
	nun_frases +=1
	
	print ("quieres ingresar mas frases S/N")				
	valor = input()
	valor = valor.upper()
	
	if valor == "N":
		fin_frases = False
	elif valor == "S":
		fin_frases = True
	else:
		while True:
			print("Por favor teclee S/N")
			valor = input()
			valor = valor.upper()
			if valor == "S":
				break
			elif valor == "N":
				fin_frases = False
				break


cont=0
palindromos = False
while nun_frases != 0:


	original = lecturas[cont]				#creo esta variable para que imprima el resultado original
	frase = original						#frase para poder modificarla	
	frase = frase.lower()					#cambio la frase a minusculas
	tupla = frase.split()					#la convierto en una tupla
	frase_junta = "".join(tupla)			#me queda la frase toda junta y en minusculas
	nun_frases -=1
	cont+=1


	longitud = len(frase_junta)
	resto = longitud % 2

	if resto == False:

		tope = int(longitud/2)
		i = tope
		while i != 0:
			
			if frase_junta[tope - i] == frase_junta[(tope + i)-1]:		#si es par 
				i -= 1
				if i == 0:
					print (original)
					palindromos = True
			else:
				break	

	else:

		tope = int(longitud/2)
		i = tope
		while i != 0:
			
			if frase_junta[tope - i] == frase_junta[tope + i]:			#si es impar
				i -= 1
				if i == 0:
					print (original)
					palindromos = True
			else:
				break

if palindromos == False:
	print("No hay palindromos")
