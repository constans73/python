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
	

if vocal_a > 0 or vocal_e > 0 or vocal_i > 0 or vocal_o > 0 or vocal_u > 0:
	print("vocal a:", vocal_a, "vocal e:", vocal_e, "vocal i:", vocal_i, "vocal o:", vocal_o,"vocal u:", vocal_u)

else:
	print("no hay vocales")
