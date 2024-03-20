import random
 
words = ["python", "programación", "computadora", "código", "desarrollo", 
"inteligencia"]
 
secret_word = random.choice(words)
 
max_failures = 10
failures = 0 

guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

def elegir_dificultad(level):
    if level in ["facil", "media", "dificil"]:
        if (level == "facil"):
            print("Se ha elegido la dificultad facil")
        elif (level == "media"):
            print("Se ha elegido la dificultad media")
        elif (level == "dificil"):
            print("Se ha elegido la dificultad dificil")
        return True
    else:
        print("No se ha ingresado una dificultad valida")
        return False

def mostrar_palabra (level,secret_word,word_displayed):
    if (level == "facil"):
        for char in secret_word:
            if char in "aeiou": 
                word_displayed += char
            else:
                word_displayed += "_"
    elif (level == "media"):
        word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
    elif (level == "dificil"):
        word_displayed = "_" * len(secret_word)
    return (word_displayed)

while True:
    level = input("Elegir nivel de dificultad (facil - media - dificil): ").lower()
    if elegir_dificultad(level): #si la dificultad es correcta sale del while
        break

word_displayed = ""
word_displayed = mostrar_palabra(level,secret_word,word_displayed) # imprimo segun el nivel
print(f"Palabra: {word_displayed}")

if (level != "dificil"): # si es dificil no entramos porque no se revelo ninguna letra
    letters_revealed = [] # lista con las letras que nos revelo la dificultad
    for char in word_displayed:
        if char != "_":
            letters_revealed.append(char)
    guessed_letters.extend(letters_revealed)
# para agregar las letras mostradas segun el nivel

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
else:
    print(f"¡Oh no! Has agotado tus {max_failures} intentos.")
    print(f"La palabra secreta era: {secret_word}")