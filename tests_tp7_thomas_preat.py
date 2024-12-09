from tp7_thomas_preat import Fraction

# Initialize fractions
fraction_a = Fraction(3, 5)
fraction_b = Fraction(2, 7)
fraction_c = Fraction(3, 5)  # Same as fraction_a to test equality
fraction_d = Fraction(5, 6)

# Test addition
addition_result = fraction_a + fraction_b
print("Adding", fraction_a, "and", fraction_b, "results in:", addition_result)  # Expected: (3/5) + (2/7) = 31/35

# Test equality
if fraction_a == fraction_c:
    print("Fractions", fraction_a, "and", fraction_c, "are equal.")  # Expected: Yes
else:
    print("Fractions", fraction_a, "and", fraction_c, "are not equal.")

# Test conversion to float
decimal_value = float(fraction_b)
print("The decimal value of the fraction", fraction_b, "is approximately:", round(decimal_value, 4))  # Expected: ~0.2857

# Test adjacency
if fraction_d.is_adjacent_to(fraction_b):
    print("Fractions", fraction_d, "and", fraction_b, "are adjacent.")  # Example: May vary based on fractions
else:
    print("Fractions", fraction_d, "and", fraction_b, "are not adjacent.")

# Test for zero denominator
try:
    invalid_fraction = Fraction(4, 0)
except ValueError as error:
    print("Error when creating a fraction with a zero denominator:", error)  # Expected: "Denominator cannot be zero."

# Test with a negative denominator
negative_denominator = Fraction(-2, -5)
print("A fraction with negative numerator and denominator becomes:", negative_denominator)  # Expected: 2/5

# Test power
powered_fraction = Fraction(4, 9) ** 2
print("The fraction (4/9) raised to the power of 2 results in:", powered_fraction)  # Expected: 16/81

inverse_fraction = Fraction(4, 9) ** -1
print("The reciprocal of the fraction (4/9) is:", inverse_fraction)  # Expected: 9/4

# Test properties
if fraction_d.is_integer():
    print("The fraction", fraction_d, "represents an integer.")  # Expected: No
else:
    print("The fraction", fraction_d, "does not represent an integer.")

if fraction_b.is_proper():
    print("The fraction", fraction_b, "is proper.")  # Expected: Yes
else:
    print("The fraction", fraction_b, "is not proper.")
