from math import gcd
"""
is_adjacent_to made with ChatGPT
"""
class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE: -
        POST: Fraction is reduced to its simplest form, and the denominator is positive.
        RAISE:
        - TypeError: If num and/or den is not an integer.
        - ValueError: If den is zero.
        """
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError('Arguments have to be integers.')

        if den == 0:
            raise ValueError("Denominator cannot be zero.")

        self.num = num
        self.den = den
        self._reduce()

    @property
    def numerator(self):
        """Numerator of the fraction.

        PRE: -
        POST: Returns the numerator of the fraction.
        """
        return self.num

    @property
    def denominator(self):
        """Denominator of the fraction.

        PRE: -
        POST: Returns the denominator of the fraction.
        """
        return self.den

    def _reduce(self):
        """Reduce the fraction to its simplest form.

        PRE: -
        POST: Fraction is in reduced form.
        """
        common_divisor = gcd(self.num, self.den)
        self.num //= common_divisor
        self.den //= common_divisor
        if self.den < 0:  # Denominator is always positive
            self.num = -self.num
            self.den = -self.den

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction.

        PRE: -
        POST: Returns a string representation of the fraction in reduced form.
        """
        return f"{self.num}/{self.den}" if self.den != 1 else f"{self.num}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number.

        PRE: -
        POST: Returns a string with the integer part and the proper fraction, or just the fraction/number if applicable.
        """
        whole = abs(self.num) // self.den  # Partie entière absolue
        remainder = abs(self.num) % self.den  # Reste absolu
        sign = -1 if self.num < 0 else 1  # Gérer les signes

        if whole == 0:
            return self.__str__()
        elif remainder == 0:
            return str(self.num // self.den)

        if sign == -1:
            return f"-{whole} {remainder}/{self.den}"
        return f"{whole} {remainder}/{self.den}"

    def __add__(self, other):
        """Overloading of the + operator for fractions.

        PRE: -
        POST: Returns a new Fraction representing the sum of self and other.
        RAISE:
        - TypeError: If other is not an instance of Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Arguments should be Fractions.")

        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions.

        PRE: -
        POST: Returns a new Fraction representing the difference of self and other.
        RAISE:
        - TypeError: If other is not an instance of Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Arguments should be Fractions.")

        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions.

        PRE: -
        POST: Returns a new Fraction representing the product of self and other.
        RAISE:
        - TypeError: If other is not an instance of Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Arguments should be Fractions.")

        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions.

        PRE: -
        POST: Returns a new Fraction representing the division of self by other.
        RAISE:
        - TypeError: If other is not an instance of Fraction.
        - ZeroDivisionError: If other.num is zero.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Arguments should be Fractions.")

        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction.")
        return Fraction(self.num * other.den, self.den * other.num)

    def __pow__(self, power):
        """Overloading of the ** operator for fractions.

        PRE: -
        POST: Returns a new Fraction representing self raised to the given power.
        RAISE:
        - TypeError: If power is not an integer.
        """
        if not isinstance(power, int):
            raise TypeError("Power should be integer.")

        if power >= 0:
            return Fraction(self.num ** power, self.den ** power)
        else:  # Negative power
            return Fraction(self.den ** abs(power), self.num ** abs(power))

    def __eq__(self, other):
        """Overloading of the == operator for fractions.

        PRE: -
        POST: Returns True if self and other are equivalent fractions; False otherwise.
        RAISE:
        - TypeError: If other is not an instance of Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Arguments should be Fractions.")

        return self.num * other.den == self.den * other.num

    def __float__(self):
        """Returns the decimal value of the fraction.

        PRE: -
        POST: Returns a float representing the fraction's value.
        """
        return self.num / self.den

    def is_zero(self):
        """Check if a fraction's value is 0.

        PRE: -
        POST: Returns True if the fraction's value is 0; False otherwise.
        """
        return self.num == 0

    def is_integer(self):
        """Check if a fraction is an integer (e.g., 8/4, 3, 2/2).

        PRE: -
        POST: Returns True if the fraction represents an integer; False otherwise.
        """
        return self.num % self.den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1.

        PRE: -
        POST: Returns True if the absolute value of the fraction is less than 1; False otherwise.
        """
        return abs(self.num) < abs(self.den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form.

        PRE: -
        POST: Returns True if the fraction's numerator is 1 in reduced form; False otherwise.
        """
        return abs(self.num) == 1 and self.den != 0

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction.

        Two fractions are adjacent if the absolute value of the difference is a unit fraction.

        PRE: -
        POST: Returns True if the absolute value of the difference is a unit fraction; False otherwise.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Arguments should be Fractions.")

        diff = self - other
        return diff.num == 1 and diff.den != 0

