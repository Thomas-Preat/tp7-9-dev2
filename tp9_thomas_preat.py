import unittest
from tp7_thomas_preat import Fraction

class TestFraction(unittest.TestCase):

    def test_initialization(self):
        self.assertEqual(str(Fraction(3, 4)), "3/4")
        self.assertEqual(str(Fraction(6, 8)), "3/4")
        self.assertEqual(str(Fraction(-3, 4)), "-3/4")
        self.assertEqual(str(Fraction(3, -4)), "-3/4")
        self.assertEqual(str(Fraction(0, 1)), "0")

        with self.assertRaises(ValueError) as context:      #Test for den == 0
            Fraction(10, 0)

        with self.assertRaises(TypeError) as context_num:   #Test for args != int
            Fraction(1.5, 2.9)


    def test_numerator_and_denominator(self):
        frac = Fraction(3, 4)
        self.assertEqual(frac.numerator, 3)
        self.assertEqual(frac.denominator, 4)


    def test_str(self):
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(4, 2)), "2")
        self.assertEqual(str(Fraction(-6, 8)), "-3/4")


    def test_as_mixed_number(self):
        self.assertEqual(Fraction(7, 3).as_mixed_number(), "2 1/3")
        self.assertEqual(Fraction(4, 2).as_mixed_number(), "2")
        self.assertEqual(Fraction(1, 2).as_mixed_number(), "1/2")
        self.assertEqual(Fraction(-7, 3).as_mixed_number(), "-2 1/3")


    def test_addition(self):
        self.assertEqual(str(Fraction(1, 2) + Fraction(1, 3)), "5/6")
        self.assertEqual(str(Fraction(-1, 2) + Fraction(1, 2)), "0")

        with self.assertRaises(TypeError) as context:       #Other isn't a Fraction
            Fraction(1, 2) + "That ain't a fraction bro"


    def test_subtraction(self):
        self.assertEqual(str(Fraction(1, 2) - Fraction(1, 3)), "1/6")
        self.assertEqual(str(Fraction(1, 2) - Fraction(1, 2)), "0")

        with self.assertRaises(TypeError) as context:       #Other isn't a Fraction
            Fraction(1, 2) - 3


    def test_multiplication(self):
        self.assertEqual(str(Fraction(2, 3) * Fraction(3, 4)), "1/2")
        self.assertEqual(str(Fraction(-2, 3) * Fraction(3, 4)), "-1/2")

        with self.assertRaises(TypeError) as context:       #Other isn't a Fraction
            Fraction(1, 2) * [1, 2]


    def test_division(self):
        self.assertEqual(str(Fraction(2, 3) / Fraction(3, 4)), "8/9")

        with self.assertRaises(ZeroDivisionError):          #Divide by zero
            Fraction(1, 2) / Fraction(0, 1)

        with self.assertRaises(TypeError) as context:       #Other isn't a Fraction
            Fraction(1, 2) / None


    def test_power(self):
        self.assertEqual(str(Fraction(2, 3) ** 2), "4/9")
        self.assertEqual(str(Fraction(2, 3) ** -1), "3/2")

        with self.assertRaises(TypeError) as context:       #Other isn't a Fraction
            Fraction(1,2) ** "im a power string"


    def test_equality(self):
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4))
        self.assertFalse(Fraction(1, 2) == Fraction(3, 4))

        with self.assertRaises(TypeError) as context:
            Fraction(1, 2) == {"still not": "a freakin fraction"}


    def test_float_conversion(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(3, 4)), 0.75)


    def test_is_zero(self):
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertFalse(Fraction(1, 2).is_zero())

    def test_is_integer(self):
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(3, 2).is_integer())

    def test_is_proper(self):
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertFalse(Fraction(3, 2).is_proper())

    def test_is_unit(self):
        self.assertTrue(Fraction(1, 3).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())

    def test_is_adjacent_to(self):
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(1, 3)))
        self.assertFalse(Fraction(1, 2).is_adjacent_to(Fraction(2, 3)))

        with self.assertRaises(TypeError) as context:
            Fraction(1, 2).is_adjacent_to(0.5)

if __name__ == "__main__":
    unittest.main()
