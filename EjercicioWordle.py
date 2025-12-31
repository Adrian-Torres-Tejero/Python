import secrets

def elegir_palabra():
    foo = ["cabal","perro","libro","plato","flaco","raton"]
    return secrets.choice(foo)

def comprobar_palabra(intento,palabra_secreta):
    resultado = ""
    for i in range(len(intento)):
        if intento[i] == palabra_secreta[i]:
            resultado += "🟩"
        elif intento[i] in palabra_secreta:
            resultado += "🟨"
        else:
            resultado += "⬛"
    return resultado

def jugar_wordle():
    palabra = elegir_palabra()
    intentos_maximos = 5
    longitud = len(palabra)
    resultados = []

    print("Adivina la palabra secreta. Tienes 5 intentos.\n")

    for intento_num in range(1,intentos_maximos+1):
        intento = input(f"Intento {intento_num}:").lower()

        if len(intento) != longitud or not intento.isalpha():
            print("La palabra debe tener 5 letras y solo contener letras.")
            continue

        resultado = comprobar_palabra(intento,palabra)
        resultados.append(resultado)
        print("Resultado: ",resultado)

        if intento == palabra:
            break
    
    print("\nLa palabra secreta era: ",palabra.upper())
    print("Resumen de la partida: ")
    for r in resultados:
        print(r)
jugar_wordle()