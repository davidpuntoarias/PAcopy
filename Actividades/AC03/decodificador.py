from itertools import chain


def decodificar(string):
    keys = {"a": "0", "r": "1", "q": "2", "u": "3", "e": "4", "t": "5",
            "i": "6", "p": "7", "o": "8", "s": "9"}
    items = {"0": "a", "1": "r", "2": "q", "3": "u", "4": "e", "5": "t",
             "6": "i", "7": "p", "8": "o", "9": "s"}
    result = ""
    for letter in string:
        if letter in "arquetipos":
            result += keys[letter]
        elif letter in "0123456789":
            result += items[letter]
        else:
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
