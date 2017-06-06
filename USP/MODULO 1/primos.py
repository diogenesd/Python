y = int(input("Digite um número inteiro: "))
cont = 0
i = 1
while i <= y:
	if  y % i == 0:
		cont +=1
	i+=1
	
if cont == 2:
	print("primo")
else:
	print("nao primo")

