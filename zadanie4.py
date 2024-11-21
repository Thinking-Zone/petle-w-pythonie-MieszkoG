tekst = input("Podaj ciąg znaków: ")
odwrocony = ""

# Iterowanie przez tekst od ostatniego do pierwszego znaku
for znak in tekst:
    odwrocony = znak + odwrocony  # Dodawanie każdego znaku na początek zmiennej 'odwrocony'

print("Odwrócony ciąg:", odwrocony)
