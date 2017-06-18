# import unittest


class Triangulo(object):
    """ Thrid week's exercices."""

    def __init__(self, a, b, c):
        """Class for make a triangule.

            This class receives the sides of a triangle
            and creates its representation.

            Args:
                a (int): side A.
                b (int): side C.
                c (int): side C.

            Returns:
               object: return an represetation of the triangle.

        """

        super(Triangulo, self).__init__()
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        """This function definate the a triangle's perimeter.

            The triangle's perimeter is the sum of the all sides.]
            For instance: a + b + c = perimeter.

            Args:
                sideA (int): size of the side A.
                sideB (int): size of the side B.
                sideC (int): size of the side C.

            Returns:
               int: return the triangle's perimeter.

        """
        return self.a + self.b + self.c

    def tipo_lado(self):
        """This Function definate the triangle's type.

            A triangle with all equals sides is triangle equilateral,
            a triangle with two equals sides is triangle isosceles,
            and a triangle none equals sides is triangle scalene

            Returns:
               string: Return the triangle's type.

        """
        if self.a == self.b and self.a == self.c:
            return "equilátero"
        if (self.a == self.b or self.a == self.c) or self.b == self.c:
            return "isóceles"
        return "escaleno"

    def retangulo(self):
        """This function verifies this triangle is one retangle triangle.

            Returns:
               bool: Return True for retangle traiangle or False otherside.

        """
        # Make a list for find the triangle's hypotenuse and hicks.
        triangle = [self.a, self.b, self.c]
        # The hypotenuse is the max triangle's value, hicks is otherside.
        hypotenuse = max(triangle)
        triangle.remove(hypotenuse)
        hick_1 = triangle[0]
        hick_2 = triangle[1]
        return hypotenuse**2 == hick_1**2 + hick_2**2

    def semelhantes(self, other_triangle):
        """This function verify if triangle's sides of two triangles is similar.

            Two triangle are similar if your types are equals.

            Args:
                other_triangle (Triangulo): Triangle for test.

            Returns:
               bool: Return True if triangles are similar or False otherside.

        """
        return self.tipo_lado() == other_triangle.tipo_lado()


# class Testtriangulo(unittest.TestCase):
#     ''' It's internal class for unit test.'''

#     def test_equals_init(self):
#         triangle = Triangulo(1, 1, 1)
#         self.assertEqual(triangle.a, 1)
#         self.assertEqual(triangle.b, 1)
#         self.assertEqual(triangle.c, 1)

#     def test_equals_perimeter(self):
#         triangle = Triangulo(1, 1, 1)
#         self.assertEqual(triangle.perimetro(), 3)

#     def test_equals_tipo_lado(self):
#         triangle = Triangulo(1, 1, 1)
#         self.assertEqual(triangle.tipo_lado(), "equilátero")
#         triangle = Triangulo(1, 2, 2)
#         self.assertEqual(triangle.tipo_lado(), "isóceles")
#         triangle = Triangulo(1, 2, 3)
#         self.assertEqual(triangle.tipo_lado(), "escaleno")

#     def test_equals_rect_triangle(self):
#         triangle = Triangulo(1, 3, 5)
#         self.assertEqual(triangle.retangulo(), False)
#         triangle = Triangulo(3, 4, 5)
#         self.assertEqual(triangle.retangulo(), True)

#     def test_equals_similar(self):
#         triangle_1 = Triangulo(1, 3, 5)
#         triangle_2 = Triangulo(3, 4, 5)
#         triangle_3 = Triangulo(1, 3, 5)
#         self.assertEqual(triangle_1.tipo_lado(), triangle_3.tipo_lado())
#         self.assertEqual(triangle_1.tipo_lado(), triangle_2.tipo_lado())


# if __name__ == '__main__':
#     unittest.main()
