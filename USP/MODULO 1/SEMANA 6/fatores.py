n = int(input("Digite um numero inteiro: "))

fator = 2
while n > 1:
    multi = 0
    while n % fator == 0:
        multi += 1
        n = n / fator
    if(multi > 0):
        print("fator =",fator,"multiplicidade =", multi)
    fator += 1

def eh_primo(y):
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
