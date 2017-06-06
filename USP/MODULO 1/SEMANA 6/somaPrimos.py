
def n_primos(n):
    soma = 0
    i = 2
    while i <= n:
        soma += eh_primo(i)
        i+= 1
    return soma

def eh_primo(n):
    cont = 0
    i = 1
    while i <= n:
        if  n % i == 0:
            cont +=1
        i+=1
    if cont == 2:
        return 1
    return 0

def test_ehPrimo():
    assert eh_primo(2) == 1
    assert eh_primo(73) == 1
    assert eh_primo(4) == 0
    assert eh_primo(100) == 0

def test_nPrimos():
    assert n_primos(2) == 1
    assert n_primos(100) == 25
    assert n_primos(1) == 0
