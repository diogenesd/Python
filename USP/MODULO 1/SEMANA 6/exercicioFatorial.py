
def fatorial(x):
    f = 1
    while x > 1:
        f = f * x
        x = x -1
    return f

def test_fatorial():
    assert fatorial(0) == 1
    assert fatorial(1) == 1
    assert fatorial(2) == 2
    assert fatorial(3) == 6
    assert fatorial(4) == 24
    assert fatorial(5) == 120


x = 1
while x >= 0:
    x = int(input("Digite o valor para fatorial ou -1 para sair: "))
    if(x >=0):
        print(fatorial(x))
