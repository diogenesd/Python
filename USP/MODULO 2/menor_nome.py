import unittest
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

"""
DocString for exercicio_video_semana2.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Exercicio do vídeo semana 2

"""


def menor_nome(nomes):
    """ This funciton find the shorter word in a word's list.

        Explanation: This funcition recevie one word's list and find
        shorter word that it's contains:

        Args:
            nomes (list:string): One word's list for to find the shorter word.

        Returns:
           string: return the shorter word that has finder.

    """
    word = nomes[0].strip()
    shorter = len(nomes[0].strip())
    for i in range(len(nomes)):
        if len(nomes[i].strip()) < shorter:
            word = nomes[i].strip()
            shorter = len(word)

    return word.capitalize()


class TestMenorPalavra(unittest.TestCase):
    ''' It's internal class for unit test.'''

    def test_equals(self):
        self.assertEqual(menor_nome(
            ['LU   ', ' josé ', 'PAULO', 'Catarina']), "Lu")
        self.assertEqual(menor_nome(
            ['zé', ' lu', 'fê']), "Zé")
        self.assertEqual(menor_nome(
            ['maria', ' josé ', '   PAULO', 'Catarina   ']), "José")


if __name__ == '__main__':
    unittest.main()


def fibol(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibol(n - 1) + fibol(n - 2)


def fibol2(n):
    return ((1 + sqrt(5)) ** n - (1 - sqrt(5))**n) / (2**n * sqrt(5))


x = np.linspace(0, 1, 300)
for w in range(2, 6, 2):
    plt.plot(x, np.sin(np.pi * x) * np.sin(2 * w * np.pi * x))
