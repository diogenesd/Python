import unittest
import criaMatriz


matriz1 = [[1, 2, 3]]
matriz2 = [[2, 1, 0]]


def somaMatriz2(A, B):
    linha = len(A)
    coluna = len(A[0])
    C = criaMatriz.criaMatriz(linha, coluna, 0)

    for lin in range(linha):
        for col in range(coluna):
            C[lin][col] = A[lin][col] + B[lin][col]
    return C


def soma_matrizes(matriz1, matriz2):
    matriz = []
    linha = len(matriz1)
    coluna = len(matriz1[0])
    linha2 = len(matriz2)
    coluna2 = len(matriz2[0])

    if linha != linha2 or coluna != coluna2:
        return False

    for i in range(linha):
        matriz.append([])
        for j in range(coluna):
            soma = matriz1[i][j] + matriz2[i][j]
            matriz[i].append(soma)
    return matriz


class TestSomaMatriz(unittest.TestCase):

    def test_equals(self):
        self.assertEqual(soma_matrizes(matriz1, matriz2), [[3, 3, 3]])
        self.assertEqual(somaMatriz2(matriz1, matriz2), [[3, 3, 3]])

    def test_not_equals(self):
        self.assertNotEqual(soma_matrizes(matriz1, matriz2), [[3, 3, 0]])


if __name__ == '__main__':
    unittest.main()
