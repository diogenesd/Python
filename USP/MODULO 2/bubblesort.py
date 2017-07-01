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


def bubble_sort(lista):
    """This function sorts a list.

        This function receive one number's list aleatory,
        and sort each element putying the high element in the end.

        Args:
            lista (list): One number's list.

        Returns:
           list: return this list ordened.

    """
    end = len(lista)
    for i in range(end - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        print(lista)
    print(lista)
    return lista


def bubble_sort_short(lista):
    """Enhancement of the function sorts a list.

        This function receive one number's list aleatory,
        and sort each element putying the high element in the end.
        If in first slice loop not change any data will
        return the list because already ordered.

        Args:
            lista (list): One number's list.

        Returns:
           list: return this list ordened.

    """
    end = len(lista)
    for i in range(end - 1, 0, -1):
        change = False  # flag to control if there is data change
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                change = True  # there is data change
        if not change:  # If there isn't data change return list
            return lista
    return lista


# class TestOrdenation(unittest.TestCase):
#     ''' It's internal class for unit test.'''

#     def test_is_ordened(self):
#         request = list(range(10))
#         random.shuffle(request)
#         response = list(range(10))
#         self.assertEqual(bubble_sort(request), response)

#     def test_not_is_equal(self):
#         request = [1, 0, 6, 8, 9, 4, 5, 7, 3, 2]
#         response = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         response[-1], response[-2] = response[-2], response[-1]
#         self.assertNotEqual(bubble_sort(request), response)

#     def test_zero_list(self):
#         zero = []
#         self.assertEqual(bubble_sort(zero), [])


# if __name__ == '__main__':
#     unittest.main()
