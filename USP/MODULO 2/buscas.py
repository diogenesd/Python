
import unittest

# Sequencial search


def busca_sequencial(seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
            return True
    return False


# Ordenação por seleção direta

def selecao_direta(seq):

    fim = len(seq)
    for i in range(fim - 1):
        posicao_menor = i
        for j in range(i + 1, fim - 1):
            if seq[j] < seq[posicao_menor]:
                posicao_menor = j

        seq[i], seq[posicao_menor] = seq[posicao_menor], seq[i]

    return seq


class TestFBuscas(unittest.TestCase):
    ''' It's internal class for unit test.'''

    def test_esta_na_lista(self):
        self.assertEqual(
            busca_sequencial([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 8), True)
        self.assertEqual(
            busca_sequencial([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 1), True)
        self.assertEqual(
            busca_sequencial([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 89), True)

    def test_nao_esta_na_lista(self):
        self.assertEqual(busca_sequencial(
            [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 90), False)
        self.assertEqual(busca_sequencial(
            [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 0), False)


class TestFORdenacao(unittest.TestCase):
    ''' It's internal class for unit test.'''

    def test_selecao_direta_ok(self):
        lista = [2, 1, 1, 3, 8, 5, 21, 13, 55, 34, 89]
        lista_ord = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.assertEqual(selecao_direta(lista), lista_ord)

    def test_selecao_direta_not(self):
        lista = [2, 1, 1, 3, 8, 5, 21, 13, 55, 34, 89]
        lista_ord = [1, 1, 2, 3, 5, 8, 13, 21, 34, 89, 55]
        self.assertNotEqual(selecao_direta(lista), lista_ord)


if __name__ == '__main__':
    unittest.main()
