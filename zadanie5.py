suma = 0

# Przechodzimy po liczbach nieparzystych od 1 do 100
for i in range(1, 101, 2):
    suma += i  # Dodajemy każdą liczbę nieparzystą do sumy

print("Suma liczb nieparzystych od 1 do 100 wynosi:", suma)
