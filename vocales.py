frase = input("Escribe una frase y te dire las vocales que tiene.\n")
frase = frase.lower()

vocal_a = 0
vocal_e = 0
vocal_i = 0
vocal_o = 0
vocal_u = 0


for i in range(len(frase)):			#comparamos i con un numero que sera la longitud de la frase

	if frase[i] == "a":					#hacemos las comparativas y sumamos donde sea igual
		vocal_a +=1						#que la vocal.
	elif frase[i] == "e":
		vocal_e +=1						
	elif frase[i] == "i":
		vocal_i +=1
	elif frase[i] == "o":
		vocal_o +=1
	elif frase[i] == "u":
		vocal_u +=1


print ("vocal a:", vocal_a, "veces")		#imprimimos los resultados.
print ("vocal e:", vocal_e, "veces")
print ("vocal i:", vocal_i, "veces")
print ("vocal o:", vocal_o, "veces")
print ("vocal u:", vocal_u, "veces")
