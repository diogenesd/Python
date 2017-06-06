# import unittest

mTest = [[1, 2, 3], ["teste"]]


def cria_matriz(l, c, v):
    m = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(v)

        m.append(linha)

    return m


def dimensoes(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    for x in matriz:
        if len(x) != coluna:
            return "Matriz inválida."
    print('{}X{}'.format(linha, coluna))
    # return '{}X{}'.format(linha, coluna)


# class TestSimensaoMatriz(unittest.TestCase):
#
#    def test_equal(self):
#        self.assertEqual(dimensoes(cria_matriz(3, 3, 0)), "3X3")
#        self.assertEqual(dimensoes(cria_matriz(1, 1, 0)), "1X1")
#        self.assertEqual(dimensoes(cria_matriz(2, 3, 0)), "2X3")
#
#    def test_not_equal(self):
#        self.assertNotEqual(dimensoes(cria_matriz(1, 1, 0)), "1X2")
#        self.assertNotEqual(dimensoes(cria_matriz(1, 1, 0)), "1X3")
#        self.assertNotEqual(dimensoes(cria_matriz(1, 1, 0)), "2X1")


# if __name__ == '__main__':
#    unittest.main()
