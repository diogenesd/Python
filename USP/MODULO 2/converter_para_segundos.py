import unittest
"""
DocString for converter_para_segundos.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Class for transform hour, minutes and seconds in only secuds

"""


def hours_minutes_in_seconds(h, m, s):
    ''' This function receive racional numbers represent hour minutes and seconds,
        then transform these in seconds.

        Parameters: h: hour, m: minute: s: second

        Return: Seconds already transformed

    '''
    assert h >= 0 and m >= 0 and s >= 0
    return h * 3600 + m * 60 + s


class TestHorarioEmSegundos(unittest.TestCase):
    ''' It's internal class for unit test.'''

    def test_equals(self):
        self.assertEqual(hours_minutes_in_seconds(1, 2, 3), 3723)
        self.assertEqual(hours_minutes_in_seconds(3, 0, 50), 10850)

    def test_not_equals(self):
        self.assertNotEqual(hours_minutes_in_seconds(1, 2, 3), 5530)
        self.assertNotEqual(hours_minutes_in_seconds(3, 0, 50), 35434)


if __name__ == '__main__':
    unittest.main()
