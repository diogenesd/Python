adj = False
valor = -1
ts = input("Digite um número inteiro: ")
ti = int(ts)
t = len(ts)
i = 1
anterior = -999999999
 
while i < t and not adj:
    x = ti % 10
    ti = ti // 10
    y = ti % 10
    if y == x:
        adj = True
    i += 1
 
if adj:
    print("sim")
else:
    print("nao")
    