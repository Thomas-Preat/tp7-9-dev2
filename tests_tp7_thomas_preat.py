from tp7_thomas_preat import Fraction


fraction1 = Fraction(1, 4)
fraction2 = Fraction(2, 5)
fraction3 = Fraction(1, 3)
fraction4 = Fraction(3, 4) #identique pour le egal
fraction5 = Fraction(3, 4) #identique pour le egal


fraction_sum = fraction1 + fraction2
print(f"fraction1 + fraction2 = {fraction_sum}")  # Attendu: (1/4) + (2/5) = 13/20


print(f"fraction1 == fraction2: {fraction1 == fraction2}")  # Attendu: False
print(f"fraction4 == fraction5: {fraction4 == fraction5}")  # Attendu: True


fraction1_as_float = float(fraction1)
print(f"fraction1 en float: {fraction1_as_float}")  # Attendu: 0.25


print(f"fraction1 est adjacente à fraction2: {fraction1.is_adjacent_to(fraction2)}")  # Attendu: False, car |(1/4) - (2/5)| = 3/20
print(f"fraction1 est adjacente à fraction3: {fraction1.is_adjacent_to(fraction3)}")  # Attendu: True, car |(1/4) - (1/3)| = 1/12

# test pour le den nul
try:
    fraction_invalid = Fraction(1, 0)
except ValueError as e:
    print(f"Erreur de création de fraction: {e}")  # Attendu "denominateur ne peut pas etre nul" 