import random
 
words = ["python", "programación", "computadora", "código", "desarrollo", 
"inteligencia"]
 
secret_word = random.choice(words)
 
max_failures = 10
failures = 0 
 
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)
 
print(f"Palabra: {word_displayed}")

while (failures < max_failures):
    letter = input("Ingresa una letra: ").lower()

    if (len(letter) == 0):
        print("No se ha ingresado ninguna letra")
        failures += 1
        continue

    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        failures += 1
        continue
    guessed_letters.append(letter) 

    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        failures += 1
        print("Lo siento, la letra no está en la palabra.")
 
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
 
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_failures} intentos.")
    print(f"La palabra secreta era: {secret_word}")