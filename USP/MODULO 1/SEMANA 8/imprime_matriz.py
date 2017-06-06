

matriz = [[1], [2], [3]]
matriz2 = [[1, 2, 3], [4, 5, 6]]


def imprime_matriz(matriz):
    _matriz = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0]) - 1):
            print(matriz[i][j], end=" ")
            _matriz.append(matriz[i][j])
        print(matriz[i][len(matriz[0]) - 1], end="")
        print()
        matriz.append(matriz[i][len(matriz[0]) - 1])
    return _matriz


def test_soma_matriz():
    # Okay
    assert(imprime_matriz(matriz) == [[3, 3, 3]])
    assert(imprime_matriz(matriz) == [[1, 2, 3], [4, 5, 6]])

    # Failure
    AssertionError(imprime_matriz(matriz) == [[3, 3, 0]])
    AssertionError((imprime_matriz(matriz) == [[1, 2, 3], [4, 5, 6]]))


test_soma_matriz
