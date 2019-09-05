from itertools import chain


def decodificar(string):
    string_ = (str(letter) for letter in string)
    result = ""
    for letter in string_:
        done = False
        numeros = (str(num) for num in range(10))
        letras = (letter for letter in "arquetipos")
        letras_ = zip(letras, numeros)
        numeros_ = zip(numeros, letras)
        for key in numeros_:
            if key[0] == letter:
                result += key[1]
                done = True
                break
            elif key[1] == letter:
                result += key[0]
                done = True
                break
        if not done:
            result += letter
    return result


if __name__ == "__main__":
    tests = [
        "66cqquu", 
        "P18g10m0c68n 0v0nz0d0 qaro-q",
        "E950 49 3n0 7134b0 d4l d4c8d6f6c0d81",
        "S6 734d49 l441 4958, 58d8 h0 90l6d8 m3y b64n!!"]


    print("  ---  PRUEBA DE DECODIFICADO ---  ")
    for test in tests:
        print(decodificar(test), "\n")
