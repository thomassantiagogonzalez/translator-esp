import random
import time

eng_words = ['Hi','Bye','Task', 'Program']
sp_words = ['Hola','Adiós','Tarea', 'Programa']
score = 0

mode = input("Elige un modo: 0 - añadir nuevas palabras, 1 - entrenamiento: \n")

while (mode != '0' and mode != '1'):
    mode = input("Símbolo no válido. Elija 0 o 1. \n")

if mode == "1":
    print("¡Traduce tantas palabras como puedas! ¡Tienes 10 intentos!")

    for i in range(10):
        number = random.randint(0, len(eng_words)-1)

        print("¿Cómo se traduce " + eng_words[number] + "?")
        respuesta = input()

        if respuesta.lower() == sp_words[number].lower():
            print("¡¡¡Genial!!!")
            score = score + 1
        else:
            print("Incorrecto. La palabra correcta es: " + sp_words[number])

        time.sleep(1)

    print("Tu puntuación final es: " + str(score))

else:
    word = input("Escribe una palabra en español: ")
    translate = input("Escribe la traducción en inglés: ")

    if len(word) > 0 and len(translate) > 0:
        sp_words.append(word)
        eng_words.append(translate)
        print("La palabra se ha añadido correctamente")
    else:
        print("No se añadió la palabra (entrada vacía)")
