# import unittest

"""
DocString for exercicio_video_semana2.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Module for search elements

"""


def busca(elements, element):
    """ This funciton search one element in one list

    Explanation: This funcition receive one element's list
    and verify if the element received is into list:

    Args:
        elements (list:object): One aleatory element's list for to verify.

    Returns:
       bool: return true if element is into list or False otherside

    """

    assert len(elements) > 0
    for i in range(len(elements)):
        if elements[i] == element:
            return i
    return False


# class TestListaOrdenada(unittest.TestCase):
#     ''' It's internal class for unit test.'''

#     def setUp(self):
#         self.p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         self.q = ["a", "b", "c", "d", "e", "f", "g"]

#     def test_type_error(self):
#         with self.assertRaises(AssertionError):
#             busca([], 1)

#     def test_number_true(self):
#         self.assertEqual(busca(self.p, 8), 7)

#     def test_number_false(self):
#         self.assertEqual(busca(self.p, -1), False)

#     def test_string_true(self):
#         self.assertEqual(busca(self.q, 'a'), 0)

#     def test_string_false(self):
#         self.assertEqual(busca(self.q, 'z'), False)


# if __name__ == '__main__':
#     unittest.main()
