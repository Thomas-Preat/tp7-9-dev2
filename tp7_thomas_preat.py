from math import gcd

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : 
            * num doit est entier
            * den doit est entier non nul
        POST : 
            * un objet Fraction est créé
        RAISE :
            * TypeError si les arguments ne sont pas des entiers
            * ValueError si den est nul
        """
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError('Les arguments doivent etre des entiers !!!')
        if den == 0:
            raise ValueError("Le denominateur ne peut pas être nul !!!")
        
        self._num = num
        self._den = den

    @property
    def numerator(self):
        """Retourne le numerateur"""
        return self._num 

    @property
    def denominator(self):
        """Retourne le denominateur"""
        return self._den


# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : 
            * ///
        POST : 
            * retourne un fstring de la fraction reduite au max
        """
        common_divisor = gcd(self._num, self._den)

        num = self._num // common_divisor
        den = self._den // common_divisor

        if den == 1:
            return f"{num}"
        else:
            return f"{num}/{den}"
        
    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : 
            * ///
        POST : 
            * si num >= den, retourne la partie entière et une fraction propre
            * si num < den, retourne la meme chose que __str__
        """
        if abs(self._num) >= abs(self._den):
            integer_part = self._num // self._den
            remainder = abs(self._num % self._den)
            
            if remainder != 0:
                return f"{integer_part} {remainder}/{abs(self._den)}"
            else:
                return f"{integer_part}"

        return str(self)

# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : 
            * other est une instance de Fraction
         POST :
            * retourne une nouvelle fraction valant la somme de self et other
        RAISE : 
            * TypeError si other n'est pas une instance de Fraction
         """
        if not isinstance(other, Fraction):
            raise TypeError("Les parametres doivent etre des fractions !!!")
        new_num = self.numerator * other.denominator + self.denominator * other.numerator
        new_den = self.denominator * other.denominator

        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

         PRE : 
            * other doit etre une instance de Fraction
         POST :
            * retourne une nouvelle fraction qui est la substraction des parametres
        RAISE : 
            * TypeError si other n'est pas une instance de Fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Les parametres doivent etre des fractions !!!")
        return self + Fraction(-other._num, other._den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE :
            * other doit etre une instance de Fraction
        POST : 
            * retourne une nouvelle fraction valant la multiplication des parametres
        RAISE : 
            * TypeError si other n'est pas une instance de Fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Les parametres doivent etre des fractions !!!")
        num = self._num * other._num
        den = self._den * other._den

        return Fraction(num, den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE :
            * other ne peut pas avoir un numérateur nul
            * other doit etre une instance de Fraction
        POST :
            * retourne une nouvelle fraction qui est le quotient des parametres
         RAISE : 
            * TypeError si other n'est pas une instance de Fraction
            * ZeroDivisionError si le dénominateur est 0
        """
        if not isinstance(other, Fraction):
            raise TypeError("Les parametres doivent etre des fractions !!!")
        if other._num == 0:
            raise ZeroDivisionError("La division par 0 n'est pas possible !!!")
        
        return self * Fraction(other._den, other._num)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE :
            * other doit etre un entier
        POST : 
            * retourne une nouvelle fractione dans laquelle le numerateur et denominateur sont eleves à une puissance
        RAISE : 
            * TypeError si other n'est pas un entier
        """
        if not isinstance(other, int):
            raise TypeError("other doit etre un entier !!!")
        
        return Fraction(self._num ** other, self._den ** other)

    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE :
            * other doit etre une instance de Fraction 

        POST : 
            * retourne true si les fractions sont équivalentes, sinon renvoie false
        RAISE : 
            * TypeError si other n'est pas une fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Les parametres doivent etre des fractions !!!")
        return self._num * other._den == self._den * other._num

    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE :
            * ///
        POST :
            * retourne la fraction en float
        """
        return self._num / self._den

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : 
            * ///
        POST : 
            * retourne True si la fraction est égale à 0, return False sinon
        """
        return self._num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : 
            * ///
        POST : 
            * Retourne True si la fraction est un entier, False sinon
        """
        return self._num % self._den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : 
            * ///
        POST : 
            * return true si la fraction est propre, false sinon
        """
        return abs(self._num) < abs(self._den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : 
            * ///
        POST : 
            * Retourne True si la fraction est une unité, False sinon
        """
        common_divisor = gcd(self._num, self._den)
        return abs(self._num // common_divisor) == 1

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference between them is a unit fraction

        PRE :
            * other est une instance de Fraction
        POST : 
            * Retourne True si la différence est de la forme ±1/d, False sinon  (si c'est une fraction unitaire)
        RAISE : 
            * TypeError si other n'est pas une fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("other doit etre une fraction !!!")
        
        diff = self - other  # La méthode __sub__ retourne une fraction.

        # Simplifier la fraction
        gcd_value = gcd(diff.numerator, diff.denominator)
        simplified_num = diff.numerator // gcd_value
        simplified_den = diff.denominator // gcd_value

        # Vérifier si la fraction est unitaire
        return abs(simplified_num) == 1 and simplified_den > 0

 