# import unittest
import random

"""
DocString for exercicio_video_semana2.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Module make huge list

"""


def lista_grande(lenght):
    """ This funciton make one huge list.

    Explanation: This funcition receive one number integer
    represent the size for make the list, then return this:

    Args:
        lenght (int): Size for make the list

    Returns:
       list: return one list with size that received by parameter.

    """
    assert lenght > -1
    array = []
    if lenght < 1:
        return array
    for i in range(lenght):
        array.append(random.randrange(lenght))
    return array


# class TestListaOrdenada(unittest.TestCase):
#     ''' It's internal class for unit test.'''

#     def setUp(self):
#         self.p = 1000
#         self.q = 2000
#         self.z = 0

#     def test_type_error(self):
#         with self.assertRaises(AssertionError):
#             lista_grande(-1)

#     def test_one_thousand(self):
#         self.assertEqual(len(lista_grande(self.p)), 1000)

#     def test_two_thousand(self):
#         self.assertEqual(len(lista_grande(self.q)), 2000)

#     def test_zero_list(self):
#         self.assertEqual(len(lista_grande(self.z)), 0)


# if __name__ == '__main__':
#     unittest.main()
