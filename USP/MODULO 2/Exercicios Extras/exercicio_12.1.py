import unittest

# teste
A = [[1, 2, 1],
     [2, 2, 2],
     [1, 3, 2]]
B = [[1, 1],
     [2, 0],
     [0, 1]]


def produto_lincol(lin, a_mat, col, b_mat):
    '''(int, matriz, int, matriz) -> float

    Recebe duas matriz a_mat e b_mat e dois inteiros lin e col
    e calcula a soma o produto entre a linha lin de a_mat com
    a coluna col de b_mat

    Pre-condicao: a funcao supoe que o numero
           de colunas de a_mat e igual ao numero de linhas
           de b_mat
    '''
    linhas = len(a_mat)
    colunas = len(b_mat[0])

    if colunas != linhas:
        return False

    soma = 0

    a = a_mat[lin]
    b = b_mat[:][col]
    for i in range(len(a)):
        for j in range(len(b)):
            soma += a[i] * b[j]

    return soma


print(produto_lincol(1, B, 0, A))


class TestExercicio12_1(unittest.TestCase):

    def test_equals(self):
        self.assertEqual(produto_lincol(1, A, 0, B), 50)

    def test_not_equals(self):
        self.assertNotEqual(produto_lincol(1, A, 0, B), 50)

    if __name__ == '__main__':
        unittest.main()
