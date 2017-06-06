def soma_matrizes(m1, m2):
    m = []
    l = len(m1)
    c = len(m1[0])
    l1 = len(m2)
    c1 = len(m2[0])
    if l != l1 or c != c1:
        return False
    for i in range(l):
        m.append([])
        for j in range(c):
            soma = m1[i][j] + m2[i][j]
            m[i].append(soma)
    return m



