frase = input("Insierte una frase\n")
frase = frase.lower()


vocal_a = 0
vocal_e = 0
vocal_i = 0
vocal_o = 0
vocal_u = 0

for i in frase:
	if i == "a":
		vocal_a +=1
	elif i == "e":
		vocal_e +=1
	elif i == "i":
		vocal_i +=1
	elif i == "o":
		vocal_o +=1
	elif i == "u":
		vocal_u +=1
	


if vocal_a > 0:
	print ("vocal a:", vocal_a)
if vocal_e > 0:
	print ("vocal e:", vocal_e)
if vocal_i > 0:
	print ("vocal i:", vocal_i)
if vocal_o > 0:
	print ("vocal o:", vocal_o)
if vocal_u > 0:
	print ("vocal u:", vocal_u)

else:
	print("no hay vocales")
