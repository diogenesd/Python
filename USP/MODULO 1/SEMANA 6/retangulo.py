
def largura(x):
    while x > 0:
        print("#", end="")
        x -= 1

l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))

while a > 0:
    largura(l)
    print()
    a -= 1


