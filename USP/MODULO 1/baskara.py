# ax^2 + bx + c = 0
import math
a = input("Digite o valor de a: ")
b = input("Digite o valor de b: ")
c = input("Digite o valor de c: ")

# convert
a = float(a)
b = float(b)
c = float(c)

# calc delta
delta = (b**2) - (4 * (a * c))

# calc roots
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    mDelta = math.sqrt(delta)
    if delta == 0:
        x = (-(b) + mDelta) / (2 * a)
        print("a raiz desta equação é", x)
    else:
        x = (-(b) + mDelta) / (2 * a)
        y = (-(b) - mDelta) / (2 * a)
        if x <= y:
            print("as raízes da equação são", x, "e", y)
        else:
            print("as raízes da equação são", y, "e", x)
