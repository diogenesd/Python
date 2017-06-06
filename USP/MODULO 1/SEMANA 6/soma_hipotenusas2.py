import math 

def soma_hipotenusas(n):
    cateto = 1
    soma = 0
    hipotenusaIso = 0
    hipotenusaEsc = 0
    while hipotenusaIso <= n or hipotenusaEsc <= n:
        hipotenusaIso = math.sqrt(cateto ** 2 + cateto ** 2)
        if (hipotenusaIso % 1) == 0 and hipotenusaIso <= n:
            soma += hipotenusaIso
            print(hipotenusaIso,cateto,cateto)
        cateto1 = cateto
        cateto2 = cateto + 1
        while cateto2 < n:
            hipotenusaEsc = math.sqrt( (cateto1 ** 2) + (cateto2 ** 2))
            if (hipotenusaEsc % 1) == 0 and hipotenusaEsc <= n:
                soma += hipotenusaEsc
                print(hipotenusaEsc,cateto1,cateto2)
            cateto2 = cateto2 + 1
        cateto = cateto + 1
    return soma
