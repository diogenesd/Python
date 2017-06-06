ts = input("Digite um número inteiro: ")
ti = int(ts)
t = len(ts)
soma = 0;
i = 0
while i < t:
    x = ti % 10
    ti = ti // 10
    soma += x
    i += 1
 
print(soma)