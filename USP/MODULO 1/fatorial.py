
x = int(input("Digite o valor de n: "))
f = x
if f ==0:
	print(1)
else:
	while x >= 2:
		x = x -1
		f = f * x
	print(f)
