# import unittest

matriz1 = [[1], [2], [3]]
matriz2 = [[1, 2, 3], [4, 5, 6]]


def imprime_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0]) - 1):
            print(matriz[i][j], end=" ")
        print(matriz[i][len(matriz[0]) - 1], end="")
        print()
    # return matriz


# class TestimprimeMatriz(unittest.TestCase):
#
#    def test_equals(self):
#        self.assertEqual(imprime_matriz(matriz1), [[1], [2], [3]])
#        self.assertEqual(imprime_matriz(matriz2), [[1, 2, 3], [4, 5, 6]])
#
#    def test_not_equals(self):
#        self.assertNotEqual(imprime_matriz(matriz1), [[3, 3, 0]])
#        self.assertNotEqual(imprime_matriz(matriz2), [[1, 2, 3]])


# if __name__ == '__main__':
#    unittest.main()
