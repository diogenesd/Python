# import unittest

"""
DocString for exercicio_video_semana2.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Module for ordenation one list

"""


def ordena(list_not_ordened):
    """ This function will do ordaned one list

    Explanation: This funcition recevie one integer number's
    list and return this ordened.

    Args:
        list_not_ordened (list:int): One aleatory number's list not ordened.

    Returns:
       list:int: return this list ordened

    """

    fim = len(list_not_ordened)
    for i in range(fim):
        posicao_menor = i
        for j in range(i + 1, fim):
            if list_not_ordened[j] < list_not_ordened[posicao_menor]:
                posicao_menor = j

        list_not_ordened[i], list_not_ordened[posicao_menor] = list_not_ordened[
            posicao_menor], list_not_ordened[i]

    return list_not_ordened


# def ordenada(numbers):
#     """ This funciton verify if the numbers in list it's ordenation

#     Explanation: This funcition recevie one int number's
#     list and verify one for each if it's ordenation:

#     Args:
#         numbers (list:int): One aleatory number's list for to verify.

#     Returns:
#        bool: return true if list is ordanation or False for otherside

#     """

#     assert len(numbers) > 0
#     small = numbers[0]
#     for i in range(len(numbers)):
#         if numbers[i] < small:
#             return False
#     small = numbers[i]
#     return True


# class TestListaOrdenada(unittest.TestCase):
#     ''' It's internal class for unit test.'''

#     def setUp(self):
#         self.p = [1, 3, 2, 4, 5, 6, 7, 9, 8]
#         self.pp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         self.q = [1, 2, 3, 4, 5, 6, 7, 8, 1]

#     # def test_type_error(self):
#     #     with self.assertRaises(AssertionError):
#     #         ordenada([])

#     def test_true(self):
#         self.assertEqual(ordenada(self.p), self.pp)

#     def test_false(self):
#         self.assertNotEqual(ordenada(self.p), self.q)

#     # def test_one_item(self):
#     #     self.assertEqual(ordenada([1]), True)

#     def test_selecao_direta_ok(self):
#         lista = [2, 1, 1, 3, 8, 5, 21, 13, 55, 34, 89]
#         lista_ord = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#         self.assertEqual(ordena(lista), lista_ord)

#     def test_selecao_direta_not(self):
#         lista = [2, 1, 1, 3, 8, 5, 21, 13, 55, 34, 89]
#         lista_ord = [1, 1, 2, 3, 5, 8, 13, 21, 34, 89, 55]
#         self.assertNotEqual(ordena(lista), lista_ord)


# if __name__ == '__main__':
#     unittest.main()
