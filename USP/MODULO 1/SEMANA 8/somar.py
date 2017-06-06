
def diminui(as_a, as_b):
    m = []
    l = len(as_a)
    c = len(as_a[0])
    for i in range(l):
        m.append([])
        for j in range(c):
            soma = as_a[i][j] - as_b[i][j]
            m[i].append(soma)

    return m
