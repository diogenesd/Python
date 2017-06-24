# import unittest

"""
DocString for exercicio_video_semana2.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Module for ordenation one list

"""


def ordenada(numbers):
    """ This funciton verify if the numbers in list it's ordenation

    Explanation: This funcition recevie one int number's
    list and verify one for each if it's ordenation:

    Args:
        numbers (list:int): One aleatory number's list for to verify.

    Returns:
       bool: return true if list is ordanation or False for otherside

    """

    assert len(numbers) > 0
    small = numbers[0]
    for i in range(len(numbers) - 1):
        if numbers[i] < small:
            return False
    small = numbers[i]
    return True


# class TestListaOrdenada(unittest.TestCase):
#     ''' It's internal class for unit test.'''

#     def setUp(self):
#         self.p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         self.q = [1, 2, 3, 4, 5, 6, 7, 8, 1]

#     def test_type_error(self):
#         with self.assertRaises(AssertionError):
#             ordenada([])

#     def test_true(self):
#         self.assertEqual(ordenada([1, 2, 3, 4, 5, 6, 7, 8, 9]), True)

#     def test_false(self):
#         self.assertNotEqual(ordenada([1, 2, 3, 4, 5, 6, 7, 8, 1]), False)


# if __name__ == '__main__':
#     unittest.main()
