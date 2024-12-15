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
        POST: Fraction is reduced to its simplest form,
                and the denominator is positive.
        RAISE:
        - TypeError: If num and/or den is not an integer.
        - ValueError: If den is zero.
        """
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError('Arguments have to be integers.')

        if den == 0:
            raise ValueError("Denominator cannot be zero.")

        self._num = num
        self._den = den
        self._reduce()

    def _reduce(self):
        """Reduce the fraction to its simplest form.

        PRE: -
        POST: Fraction is in reduced form.
        """
        common_divisor = gcd(self._num, self._den)
        self._num //= common_divisor
        self._den //= common_divisor
        if self._den < 0:  # Denominator is always positive
            self._num = -self._num
            self._den = -self._den

    @property
    def numerator(self):
        """Get the numerator."""
        return self._num

    @numerator.setter
    def numerator(self, value):
        """Set the numerator with validation."""
        if not isinstance(value, int):
            raise TypeError("Numerator must be an integer.")
        self._num = value
        self._reduce()

    @property
    def denominator(self):
        """Get the denominator."""
        return self._den

    @denominator.setter
    def denominator(self, value):
        """Set the denominator with validation."""
        if not isinstance(value, int):
            raise TypeError("Denominator must be an integer.")
        if value == 0:
            raise ValueError("Denominator cannot be zero.")
        self._den = value
        self._reduce()

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction.

        PRE: -
        POST: Returns a string representation of the fraction in reduced form.
        """
        return f"{self._num}/{self._den}" if self._den != 1 else f"{self._num}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction
            as a mixed number.

        PRE: -
        POST: Returns a string with the integer part and the proper fraction,
            or just the fraction/number if applicable.
        """
        whole = abs(self._num) // self._den  # Partie entière absolue
        remainder = abs(self._num) % self._den  # Reste absolu
        sign = -1 if self._num < 0 else 1  # Gérer les signes

        if whole == 0:
            return self.__str__()
        elif remainder == 0:
            return str(self._num // self._den)

        if sign == -1:
            return f"-{whole} {remainder}/{self._den}"
        return f"{whole} {remainder}/{self._den}"

    def __add__(self, other):
        """Overloading of the + operator for fractions.

        PRE: -
        POST: Returns a new Fraction representing the sum of self and other.
        RAISE:
        - TypeError: If other is not an instance of Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Arguments should be Fractions.")

        new_num = self._num * other._den + other._num * self._den
        new_den = self._den * other._den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions.

        PRE: -
        POST: Returns a new Fraction representing the difference
            of self and other.
        RAISE:
        - TypeError: If other is not an instance of Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Arguments should be Fractions.")

        new_num = self._num * other._den - other._num * self._den
        new_den = self._den * other._den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions.

        PRE: -
        POST: Returns a new Fraction representing
            the product of self and other.
        RAISE:
        - TypeError: If other is not an instance of Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Arguments should be Fractions.")

        return Fraction(self._num * other._num, self._den * other._den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions.

        PRE: -
        POST: Returns a new Fraction representing
            the division of self by other.
        RAISE:
        - TypeError: If other is not an instance of Fraction.
        - ZeroDivisionError: If other.num is zero.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Arguments should be Fractions.")

        if other._num == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction.")
        return Fraction(self._num * other._den, self._den * other._num)

    def __pow__(self, power):
        """Overloading of the ** operator for fractions.

        PRE: -
        POST: Returns a new Fraction representing
            self raised to the given power.
        RAISE:
        - TypeError: If power is not an integer.
        """
        if not isinstance(power, int):
            raise TypeError("Power should be integer.")

        if power >= 0:
            return Fraction(self._num ** power, self._den ** power)
        else:  # Negative power
            return Fraction(self._den ** abs(power), self._num ** abs(power))

    def __eq__(self, other):
        """Overloading of the == operator for fractions.

        PRE: -
        POST: Returns True if self and other are equivalent fractions;
            False otherwise.
        RAISE:
        - TypeError: If other is not an instance of Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Arguments should be Fractions.")

        return self._num * other._den == self._den * other._num

    def __float__(self):
        """Returns the decimal value of the fraction.

        PRE: -
        POST: Returns a float representing the fraction's value.
        """
        return self._num / self._den

    def is_zero(self):
        """Check if a fraction's value is 0.

        PRE: -
        POST: Returns True if the fraction's value is 0; False otherwise.
        """
        return self._num == 0

    def is_integer(self):
        """Check if a fraction is an integer (e.g., 8/4, 3, 2/2).

        PRE: -
        POST: Returns True if the fraction represents an integer;
            False otherwise.
        """
        return self._num % self._den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1.

        PRE: -
        POST: Returns True if the absolute value of the fraction is
            less than 1; False otherwise.
        """
        return abs(self._num) < abs(self._den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form.

        PRE: -
        POST: Returns True if the fraction's numerator is 1 in reduced form;
            False otherwise.
        """
        return abs(self._num) == 1 and self._den != 0

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction.

        Two fractions are adjacent if the absolute value of the difference
        is a unit fraction.

        PRE: -
        POST: Returns True if the absolute value of the difference is
            a unit fraction; False otherwise.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Arguments should be Fractions.")

        diff = self - other
        result = Fraction(abs(diff._num), abs(diff._den))

        return result._num == 1
