

def criaMatriz(l, c, v):
    m = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(v)

        m.append(linha)

    return m
