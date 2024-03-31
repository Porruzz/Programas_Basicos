import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    guess = int(input("Adivine el número entre 1 y 100: "))
    attempts = 1

    while guess != number_to_guess:
        if guess < number_to_guess:
            print("¡Intente un número más alto!")
        else:
            print("¡Intente un número más bajo!")
        guess = int(input("Ingrese otro número: "))
        attempts += 1

    print(f"¡Felicidades! Adivinaste el número en {attempts} intentos.")

guess_number()