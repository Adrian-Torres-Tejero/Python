# Python
![Logo de JavaScript](https://imgs.search.brave.com/035VGjn0RgjXJWfzLvXH_vnuvFpVCcbl1zM_GukencM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4z/ZC5pY29uc2NvdXQu/Y29tLzNkL2ZyZWUv/dGh1bWIvZnJlZS1w/eXRob24tM2QtaWNv/bi1wbmctZG93bmxv/YWQtNTMyNjM4NS5w/bmc)
## Descripción
### Este ejercicio es el juego wordle, consiste en adivinar una palabra secreta en un numero de intentos, cuando se terminan los intentos o el usuario acierta la palabra el juego finaliza y el programa muestra el resultado de la partida
---
### EjercicioWorlde.py
```python
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
```
