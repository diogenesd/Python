# import unittest


# matriz1 = [[1, 2, 3]]
# matriz2 = [[2, 1, 0], [2, 1, 0], [2, 1, 0]]
# matriz3 = [[2, 1]]
# matriz4 = [[2, 1, 0], [2, 1, 0]]


def sao_multiplicaveis(matriz1, matriz2):
    coluna = len(matriz1[0])
    linha2 = len(matriz2)

    if coluna != linha2:
        return False

    return True


# class TestSomaMatriz(unittest.TestCase):

#     def test_is_multipicate(self):
#         self.assertTrue(sao_multiplicaveis(matriz1, matriz2), True)
#         self.assertTrue(sao_multiplicaveis(matriz3, matriz4), True)

#     def test_not_is_multiplicate(self):
#         self.assertFalse(sao_multiplicaveis(matriz2, matriz1), False)
#         self.assertFalse(sao_multiplicaveis(matriz4, matriz3), False)

#     if __name__ == '__main__':
#         unittest.main()
