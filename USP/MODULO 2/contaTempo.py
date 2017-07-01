import lista_grande
import lista_ordenada
import bubblesort
import time
import unittest
"""
DocString for contaTempo.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Module for camparation
"""


def compara_tempo(lista_1, lista_2):
    """This function compares two sort functions

        Receives two equals lists and checks which of the
        two functions takes less time to execute.

        Args:
            lista_1 (list): One list of data
            lista_2 (list): One list of data e.quals to first parameter.

        Returns:
           float: Delta timing elapsed by the first function.
           float: Delta timing elapsed by the second function.

    """
    antes_1 = time.time()
    lista_ordenada.ordena(lista_1)
    depois_1 = time.time()
    delta_1 = depois_1 - antes_1

    antes_2 = time.time()
    bubblesort.bubblesort(lista_2)
    depois_2 = time.time()
    delta_2 = depois_2 - antes_2
    return delta_1, delta_2


class TestOrdenation(unittest.TestCase):
    ''' It's internal class for unit test.'''

    def test_first_is_faster(self):
        l_1 = lista_grande.lista_grande(1000)
        l_2 = l_1[:]  # clone list 1 for compare same data
        d1, d2 = compara_tempo(l_1, l_2)
        self.assertTrue(d1 < d2)

    def test_empty_list(self):
        l_1 = []
        l_2 = []
        d1, d2 = compara_tempo(l_1, l_2)
        self.assertEqual(d1, d2)


if __name__ == '__main__':
    unittest.main()
