import unittest
from tp7_thomas_preat import Fraction

class TestFraction(unittest.TestCase):

    def test_init(self):
        """Test de l'initialisation des fractions"""
        # Test des initialisations correctes
        f1 = Fraction(1, 2)
        f2 = Fraction(10, 3)
        f3 = Fraction(0, 2)

        self.assertEqual(f1.numerator, 1, "Le numérateur de f1 devrait être 1.")
        self.assertEqual(f2.denominator, 3, "Le denominateur de f2 devrait etre 3.")
        self.assertEqual(f3.numerator, 0, "Le numérateur de f3 devrait être 0.")

    def test_add(self):
        """Test de l'opérateur d'addition"""
        f1 = Fraction(2, 4)
        f2 = Fraction(3, 4)
        result = f1 + f2

        self.assertEqual(result, Fraction(5, 4), "La somme des fractions devrait être 5/4.")

    def test_subtract(self):
        """Test de l'opérateur de soustraction"""
        f1 = Fraction(5, 4)
        f2 = Fraction(1, 4)
        result = f1 - f2
        self.assertEqual(result, Fraction(1, 1), "La différence des fractions devrait être 1.")

    def test_multiply(self):
        """Test de l'opérateur de multiplication"""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        result = f1 * f2
        self.assertEqual(result.numerator, 2, "Le produit des fractions devrait être 2/6.")
        self.assertEqual(result.denominator, 6, "Le produit des fractions devrait être 2/6.")

    def test_divide(self):
        """Test de l'opérateur de division"""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        result = f1 / f2
        self.assertEqual(result.numerator, 3, "Le quotient des fractions devrait être 3/4.")
        self.assertEqual(result.denominator, 4, "Le quotient des fractions devrait être 3/4.")

    def test_equal(self):
        """Test de l'opérateur d'égalité"""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        f3 = Fraction(3, 5)
        
        self.assertTrue(f1 == f2, "Les fractions 1/2 et 2/4 devraient être égales.")
        self.assertFalse(f1 == f3, "Les fractions 1/2 et 3/5 ne devraient pas être égales.")

    def test_float(self):
        """Test de la conversion en float"""
        f1 = Fraction(1, 2)
        self.assertEqual(float(f1), 0.5, "La conversion de 1/2 en float devrait donner 0.5.")

    def test_as_mixed_number(self):
        """Test de la représentation en nombre mixte"""
        f1 = Fraction(7, 3)
        self.assertEqual(f1.as_mixed_number(), "2 1/3", "La représentation en nombre mixte de 7/3 devrait être '2 1/3'.")

    def test_is_zero(self):
        """Test de la méthode is_zero()"""
        f1 = Fraction(0, 2)
        f2 = Fraction(1, 2)
        self.assertTrue(f1.is_zero(), "La fraction 0/2 devrait être zéro.")
        self.assertFalse(f2.is_zero(), "La fraction 1/2 ne devrait pas être zéro.")

    def test_is_integer(self):
        """Test de la méthode is_integer()"""
        f1 = Fraction(4, 2)
        f2 = Fraction(3, 4)
        self.assertTrue(f1.is_integer(), "La fraction 4/2 devrait être un entier.")
        self.assertFalse(f2.is_integer(), "La fraction 3/4 ne devrait pas être un entier.")

    def test_is_proper(self):
        """Test de la méthode is_proper()"""
        f1 = Fraction(1, 2)
        f2 = Fraction(5, 3)
        self.assertTrue(f1.is_proper(), "La fraction 1/2 devrait être propre.")
        self.assertFalse(f2.is_proper(), "La fraction 5/3 ne devrait pas être propre.")

    def test_is_unit(self):
        """Test de la méthode is_unit()"""
        f1 = Fraction(4, 12)
        f2 = Fraction(3, 4)
        self.assertTrue(f1.is_unit(), "La fraction 4/12 devrait être une unité.")
        self.assertFalse(f2.is_unit(), "La fraction 3/4 ne devrait pas être une unité.")

    def test_is_adjacent_to(self):
        """Test de la méthode is_adjacent_to()"""
        f1 = Fraction(3, 4)
        f2 = Fraction(5, 4)
        f3 = Fraction(6, 4)
        
        self.assertTrue(f1.is_adjacent_to(f2), "Les fractions 3/4 et 5/4 devraient être adjacentes.")
        self.assertFalse(f1.is_adjacent_to(f3), "Les fractions 3/4 et 7/4 ne devraient pas être adjacentes.")

    def test_invalid_denominator(self):
        """Test de l'exception ValueError pour un dénominateur nul"""
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_invalid_type(self):
        """Test de l'exception TypeError pour des entrées non entières"""
        with self.assertRaises(TypeError):
            Fraction(1.5, 2)  # Numérateur non entier
        with self.assertRaises(TypeError):
            Fraction(1, '2')  # Dénominateur non entier


if __name__ == "__main__":
    unittest.main()
