import unittest

"""
DocString for recursividade.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Module of the fucntions recursive.
"""


def fatorial_recursivo(n):
    assert isinstance(n, int)

    if n < 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)


def fibonacci_recursivo(n):
    assert isinstance(n, int)

    if n < 2:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def busca_binaria_recursiva(lista, element, min=0, max=None):
    print("*")
    if max is None:
        max = len(lista) - 1

    if max < min:
        return False
    else:
        meio = min + (max - min) // 2

    if lista[meio] > element:
        return busca_binaria_recursiva(lista, element, min, meio - 1)
    elif lista[meio] < element:
        return busca_binaria_recursiva(lista, element, meio + 1, max)
    else:
        return meio


def mergesort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2

    left_side = mergesort(lista[:meio])  # divede the list left side
    right_side = mergesort(lista[meio:])  # divede the list right side

    return __mergesort(left_side, right_side)  # intercalation


def __mergesort(left_side, right_side):
    if not left_side:  # if none return other sider
        return right_side

    if not right_side:  # if none return other sider
        return left_side

    if left_side[0] < right_side[0]:
        # if first element this left is smaller than
        # first element other side,
        # then make new list begin with this.

        return [left_side[0]] + __mergesort(left_side[1:], right_side)

    # make new list begin with right side.
    return [right_side[0]] + __mergesort(left_side, right_side[1:])


class TestRecursive(unittest.TestCase):
    ''' It's internal class for unit test.'''

    def test_fatorial_0(self):
        self.assertEqual(fatorial_recursivo(0), 1)

    def test_fatorial_1(self):
        self.assertEqual(fatorial_recursivo(1), 1)

    def test_fatorial_2(self):
        self.assertEqual(fatorial_recursivo(2), 2)

    def test_fatorial_3(self):
        self.assertEqual(fatorial_recursivo(3), 6)

    def test_fatorial_4(self):
        self.assertEqual(fatorial_recursivo(4), 24)

    def test_fatorial_5(self):
        self.assertEqual(fatorial_recursivo(5), 120)

    def test_type_error_none_paramenter(self):
        with self.assertRaises(TypeError):
            fatorial_recursivo()

    def test_assert_error_parameter_unexpected(self):
        with self.assertRaises(AssertionError):
            fatorial_recursivo('a')

    def test_fibonacci_0(self):
        self.assertEqual(fibonacci_recursivo(0), 0)

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci_recursivo(1), 1)

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci_recursivo(2), 1)

    def test_fibonacci_3(self):
        self.assertEqual(fibonacci_recursivo(3), 2)

    def test_fibonacci_4(self):
        self.assertEqual(fibonacci_recursivo(4), 3)

    def test_fibonacci_5(self):
        self.assertEqual(fibonacci_recursivo(5), 5)

    def test_type_error_none_paramenter_fibonacci(self):
        with self.assertRaises(TypeError):
            fibonacci_recursivo()

    def test_assert_error_parameter_unexpected_fibonacci(self):
        with self.assertRaises(AssertionError):
            fibonacci_recursivo('a')

    def test_busca_binaria_recursiva(self):
        a = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]
        self.assertEqual(
            busca_binaria_recursiva(a, 99), 6)


if __name__ == '__main__':
    unittest.main()
