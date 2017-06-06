
def soma_hipotenusa(n):
        soma_hipotenusa = 0
        i = 1
        while i <= n:
                if éHipotenusa(i):
                        soma_hipotenusa +=1
                i += 1
        return soma_hipotenusa

def éHipotenusa(x):
        soma_hipotenusa = 0
        cateto1 = 1
        cateto2 = 1
        while cateto1 < x:
                while cateto2 < x:
                        if (cateto1 ** 2) + (cateto2 ** 2) == (x ** 2 ):
                                soma_hipotenusa += cateto2 + cateto1
                        cateto2 += 1
                cateto1 += 1
                cateto2 = cateto1
        return soma_hipotenusa
