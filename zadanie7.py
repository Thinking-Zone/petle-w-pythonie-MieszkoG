import random

# Losowanie pogody (True = pada, False = nie pada)
pogoda = random.choice([True, False])

# Pytanie użytkownika dopóki nie zgadnie poprawnie
while True:
    odpowiedz = input("Czy pada deszcz? (tak/nie): ").lower()

    if odpowiedz == "tak" and pogoda:
        print("Brawo! Zgadłeś!")
        break
    elif odpowiedz == "nie" and not pogoda:
        print("Brawo! Zgadłeś!")
        break
    else:
        print("Nie zgadłeś. Spróbuj ponownie.")
