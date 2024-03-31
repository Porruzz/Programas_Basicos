import random

def hangman():
    words = ["python", "programming", "computer", "science", "algorithm"]
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    attempts = 6
    guessed_letters = []

    print("¡Bienvenido al juego del ahorcado!")
    print("Tienes 6 intentos para adivinar la palabra.")

    while attempts > 0 and "_" in guessed_word:
        print(" ".join(guessed_word))
        guess = input("Ingresa una letra: ").lower()

        if guess in guessed_letters:
            print(f"Ya intentaste la letra '{guess}', ¡intenta con otra!")
        else:
            guessed_letters.append(guess)

            if guess in word_to_guess:
                for i, letter in enumerate(word_to_guess):
                    if letter == guess:
                        guessed_word[i] = letter
            else:
                attempts -= 1
                print(f"Lo siento, '{guess}' no está en la palabra. Te quedan {attempts} intentos.")

    if "_" not in guessed_word:
        print("¡Felicidades! Adivinaste la palabra.")
    else:
        print(f"Lo siento, no adivinaste la palabra. La palabra era '{word_to_guess}'.")

hangman()