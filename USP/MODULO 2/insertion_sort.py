# import unittest
# import random

"""
DocString for exercicio_video_semana2.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Module ordenation
"""


def insertion_sort(lista):
    for i in range(1, len(lista)):
        current = lista[i]
        position = i

        while position > 0 and lista[position - 1] > current:
            lista[position] = lista[position - 1]
            position = position - 1

        lista[position] = current
    return lista


# class TestInsertionSOrt(unittest.TestCase):
#     ''' It's internal class for unit test.'''

#     def test_is_ordened(self):
#         request = list(range(10))
#         random.shuffle(request)
#         response = list(range(10))
#         self.assertEqual(insertion_sort(request), response)

#     def test_not_is_equal(self):
#         request = [1, 0, 6, 8, 9, 4, 5, 7, 3, 2]
#         response = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         response[-1], response[-2] = response[-2], response[-1]
#         self.assertNotEqual(insertion_sort(request), response)

#     def test_zero_list(self):
#         zero = []
#         self.assertEqual(insertion_sort(zero), [])


# if __name__ == '__main__':
#     unittest.main()
