import unittest


matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[1, 2], [3, 4], [5, 6]]


def multiplicaMatriz2(A, B):
    linhaA = len(A)
    colunaA = len(A[0])
    colunaB = len(B[0])
    assert linhaA == colunaB

    C = []
    for lin in range(linhaA):
        C.append([])
        for col in range(colunaB):
            C[lin].append(0)
            for x in range(colunaA):
                C[lin][col] += A[lin][x] * B[x][col]
    return C


class TestMultiplicaMatriz(unittest.TestCase):

    def test_equals(self):
        self.assertEqual(multiplicaMatriz2(
            matriz1, matriz2), [[22, 28], [49, 64]])


if __name__ == '__main__':
    unittest.main()
