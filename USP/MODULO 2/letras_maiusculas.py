# import unittest
"""
DocString for letras_maiusculas.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: This class is to find upper letters in a phrase.

"""


def maiusculas(frase):
    """This funcion find the upper letters in an frase
        and return one string with they.

        Args:
            frase (string): Receive one string with
            contains letters for to find.

    """
    string_return = ""
    for letter in frase:
        if ord(letter) > 64 and ord(letter) < 91:
            string_return += letter
    return string_return


# class TestLetrasMaiusculas(unittest.TestCase):
#     ''' It's internal class for unit test.'''

#     def test_equals_maiusculas(self):
#         self.assertEqual(
#             maiusculas('Programamos em python 2?'), "P")
#         self.assertEqual(
#             maiusculas('Programamos em Python 3.'), "PP")
#         self.assertEqual(
#             maiusculas('PrOgRaMaMoS em python!'), "PORMMS")

#     def test_not_equals_maiusculas(self):
#         self.assertNotEqual(
#             maiusculas("O carro Esta na Garagem"), 'O')
#         self.assertNotEqual(
#             maiusculas("O carro Esta na Garagem"), '')


# if __name__ == '__main__':
#     unittest.main()
