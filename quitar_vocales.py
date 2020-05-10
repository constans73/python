frase = input("insierte una frase\n")
frase = frase.lower()

for i in frase:
	if (i == "a") or (i == "e") or (i == "i") or (i == "o") or (i == "u"):	#alalizamos vocal por vocal
		frase = frase.replace(i,"")
print (frase)

			################    SEGUNDA FORMA DE HACERLO MEDIANTE UNA TUPLA    #####################

tupla = ("a", "e","i","o","u","A", "E", "I", "O", "U")	#he metido las vocales en una tupla
frase = input("insierte una frase\n")

for i in frase:				
	if i in tupla:							#analizamos si esta la vocal en la tupla
		frase = frase.replace(i,"")
print (frase)

			################	TERCERA FORMA MEDIANTE UN DICICIONARIO 		#########################


diccionario = {"1":"a", "2":"e", "3":"i", "4":"o", "5":"u"}		#las keys las he puesto numericas para entender mejor
frase = input ("insierte una frase\n")
frase = frase.lower()

for i in diccionario.values():				# analizamos respecto a los valores del diccionario
	frase = frase.replace(i,"")

print (frase)
