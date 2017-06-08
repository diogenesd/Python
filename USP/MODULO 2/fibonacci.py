import unittest
"""
DocString for fibonacci.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Sequence Fibonacci

"""


def fibonacci1(n):
    ''' This function write Fibonacci series up to n,
            then print the senquence.

            Paramenters: n: limit for sequence finbonacci.
    '''

    assert n > 0  # It's should will racional.
    num_1, num_2 = 0, 1
    while num_2 < n:
        print(num_2, end=' ')
        num_1, num_2 = num_2, num_1 + num_2  # swipe
    print()


def fibonacci2(n):
    ''' This function write Fibonacci series up to n,
            then print the senquence.

            Paramenters: n: limit for sequence finbonacci.

            Return: List with sequence fibonacci util n.
    '''

    assert n > 0  # It's should will racional.
    result = []
    num_1, num_2 = 0, 1
    while num_2 < n:
        result.append(num_2)
        num_1, num_2 = num_2, num_1 + num_2  # swipe
    return result


class TestFibonacci(unittest.TestCase):
    ''' It's internal class for unit test.'''

    def test_equals(self):
        self.assertEqual(
            fibonacci2(100),
            [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        self.assertEqual(fibonacci2(500), [
            1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])

    def test_not_equals(self):
        self.assertNotEqual(
            fibonacci2(500), "1 1 2 3 5 8 13 21 34 55 89 144 233 377".split())
        self.assertNotEqual(fibonacci2(10), [
            1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])


if __name__ == '__main__':
    unittest.main()
