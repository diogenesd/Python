

def cheio(x):
    while x > 0:
        print("#", end="")
        x -= 1

def vazio(x):
    print("#", end="")
    x -= 1
    while x > 1:
        print(" ", end="")
        x -= 1
    print("#", end="")

l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))

while a > 0:
    cheio(l)
    print()
    while a > 2:
        vazio(l)
        print()
        a -= 1
    a -= 1
