import tablero as table
import parametros as constant
from random import randint
from os import path, makedirs
from sys import exit
comando, largo, ancho, legos_tablero, board, board_showed,\
 user = "", 0, 0, 0, [], [], "default"
folder = path.join(path.dirname(__file__), "partidas")
rank = path.join(path.dirname(__file__), "puntajes.dat")
acento = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "Á": "A", "É": "E",
          "Í": "I", "Ó": "O", "Ú": "U"}
valores_validos = ["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                   "14", "15"]
menu_juego = ["Descubrir baldosa", "Guardar la partida", "Guardar y" +
              " volver al menú principal"]
menu_principal = ["Nueva Partida", "Cargar Partida", "Ranking"]
columna_a_index = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def error(type):
    if type == 0:
        print("Error - Se ha ingresado un valor inválido")
    elif type == 1:
        print("Error - No se ha encontrado ninguna partida asociado con el\
              apodo ingresado")
    print(" ------ ------")


def menu(options, back):
    global comando
    if back == 1:
        exit = "Salir"
    else:
        exit = "Volver al menú principal"
    print("\n-Seleccione una opción:")
    for option in range(1, len(options) + 1):
        print("[" + str(option) + "] " + options[option - 1])
    print("[0]", exit + "\n")
    comando = input("Ingrese el número de la opción que deseea utilizar:\n")
    print(" ------ ------ ")


def verificar(nombre):
    resultado = 0
    while True:
        resultado = input("Ingrese un valor entre 3 y 15 para el " + nombre +
                          " del tablero:\n")
        if resultado in valores_validos:
            return resultado
        print(" ------ ------\nError - El valor ingresado no es un número\
              entre 3 y 15\n ------ ------ ")


def agregar_lego(probabilidad, legos, excepcion):
    global board
    while legos != 0:
        for fila in range(largo):
            for columna in range(ancho):
                if randint(1, probabilidad) == 1 and\
                 board[fila][columna] != "L" and [fila, columna] != excepcion:
                    board[fila][columna] = "L"
                    legos -= 1
                if legos == 0:
                    break
            if legos == 0:
                break


def generar_tablero():
    global board, board_showed, user, legos_tablero, largo, ancho
    board, board_showed = [], []
    user = quitar_acento(input("Elige una apodo al que asignar tu partida:\n"))
    largo = int(verificar("largo"))
    ancho = int(verificar("ancho"))
    legos_tablero = int(largo * ancho * constant.PROB_LEGO // 1)
    row = []
    for y in range(ancho):
        row.append(" ")
    for x in range(largo):
        board.append(row[:])
        board_showed.append(row[:])
    agregar_lego(((largo * ancho) // legos_tablero), legos_tablero, [" ", " "])


def fila_a_dato(fila):
    linea = ""
    for columna in range(len(fila)):
        if columna != 0:
            linea += "/" + fila[columna]
        else:
            linea += fila[columna]
    return linea


def guardar_tablero():
    global board, board_showed, user, largo, ancho, legos_tablero, folder
    directorio = path.join(folder, user + ".sav")
    if not path.exists(folder):
        makedirs(folder)
    if path.isfile(directorio):
        comando = input("Se ha detectado un archivo guardado con tu mismo " +
                        "apodo " + "¿Deseas sobreescribir el archivo?\n[1]" +
                        " Sí\n[0] No\n\n")
        if comando == "1":
            pass
        elif comando == "0":
            return False
        else:
            comando = " "
            error(0)
            return False
    with open(directorio, "w") as save:
        save.writelines("\n".join([str(largo), str(ancho),
                        str(legos_tablero), ""]))
        for fila in board:
            save.writelines(fila_a_dato(fila) + "\n")
        for fila in board_showed:
            save.writelines(fila_a_dato(fila) + "\n")
        print("Partida guardada de manera exitosa" +
              "\n ------ ------")
        return True


def dato_a_lista(datos):
    resultado = datos
    for dato in range(len(datos)):
        resultado[dato] = resultado[dato][:-1]
        resultado[dato] = resultado[dato].split("/")
    return resultado


def cargar_tablero():
    global ancho, largo, legos_tablero, board, board_showed, user, folder
    user = input("Ingresa el apodo asignado a tu partida:\n")
    directorio = path.join(folder, user + ".sav")
    if path.isfile(directorio):
        with open(directorio, "rt") as save:
            datos = save.readlines()
        ancho = int(datos.pop(0)[:-1])
        largo = int(datos.pop(0)[:-1])
        legos_tablero = int(datos.pop(0)[:-1])
        datos = dato_a_lista(datos)
        board = datos[:largo]
        board_showed = datos[largo:]
        return True
    else:
        error(1)
        return False


def lego_alrededor(fila, columna):
    global board, board_showed, largo, ancho
    numero_legos, suma, posiciones_proximas = 0, [-1, 0, 1], []
    if not board_showed[fila][columna].isdigit():
        for i in suma:
            for e in suma:
                if fila + i < 0 or columna + e < 0 or fila + i >= largo\
                 or columna + e >= ancho or (i == 0 and e == 0):
                    continue
                elif board[fila + i][columna + e] == "L":
                    numero_legos += 1
                posiciones_proximas.append([fila + i, columna + e])
        board_showed[fila][columna] = str(numero_legos)
        if numero_legos == 0:
            for posicion in posiciones_proximas:
                if not board_showed[posicion[0]][posicion[1]].isdigit():
                    lego_alrededor(posicion[0], posicion[1])
    else:
        print("Esa baldosa ya ha sido revelada\n ------ ------\n")


def baldosas_descubiertas():
    global board_showed
    numero_baldosas = 0
    for fila in board_showed:
        for columna in fila:
            if columna.isdigit():
                numero_baldosas += 1
    return numero_baldosas


def game_end():
    global comando, legos_tablero, board, board_showed, rank, user
    for fila in range(len(board)):
        for columna in range(len(board[0])):
            if board[fila][columna] == "L":
                board_showed[fila][columna] = "L"
    table.print_tablero(board_showed)
    puntaje = baldosas_descubiertas() * constant.POND_PUNT * legos_tablero
    print("\n-||Game over||-\n Felicidades tu puntuación es:\n\n" +
          " ----|| " + user, str(puntaje) +
          "pts ||----\n\n ------ ------")
    comando = " "
    if not path.isfile(rank):
        default_ranking(rank)
    with open(rank, "rt") as ranking:
        datos = ranking.readlines()
    datos = dato_a_lista(datos)
    for dato in range(len(datos)):
        if int(datos[dato][1]) < puntaje and dato + 1 != len(datos):
            datos = datos[:dato] + [[user, str(puntaje)]] + datos[dato:]
            break
    with open(rank, "w") as ranking:
        for dato in datos:
            ranking.writelines(fila_a_dato(dato) + "\n")
    imprimir_ranking()


def salir(volver):
    global comando
    while True:
        comando = input("¿Estás seguro de que deseas salir?\n[1] " +
                        "Sí\n[0] No\n\n")
        if comando == "0":
            comando = " "
            return False
        elif volver:
            comando = " "
            return True
        elif comando == 1:
            exit(0)
        else:
            print(" ------ ------")
            error(0)


def partida():
    global board, board_showed, menu_juego, comando, largo, ancho,\
     legos_tablero
    baldosas_iniciales = baldosas_descubiertas()
    while True:
        table.print_tablero(board_showed)
#       table.print_tablero(board) //
#       Si se desea visualizar la posición de las minas descomentar
#       linea anterior
        if (largo * ancho) - baldosas_descubiertas() == legos_tablero:
            game_end()
            break
        menu(menu_juego, 0)
        if comando == "1":
            posicion = input("Ingresa la coordenada de la baldosa (Ej: A4)\n")
            if posicion[0].isupper() and posicion[1].isdigit() and\
               int(posicion[1:]) < largo:
                columna = columna_a_index.index(posicion[0])
                fila = int(posicion[1:])
                if board[fila][columna] == "L":
                    if baldosas_iniciales == 0:
                        board[fila][columna] = " "
                        agregar_lego(((largo * ancho) // legos_tablero) +
                                     1, 1, [fila, columna])
                        baldosas_iniciales = 1
                        lego_alrededor(fila, columna)
                    else:
                        game_end()
                        break
                else:
                    lego_alrededor(fila, columna)
                    if baldosas_iniciales == 0:
                        baldosas_iniciales = 1
            else:
                print(" ------ ------")
                error(0)
        elif comando in ["2", "3"]:
            if guardar_tablero() and comando == "3":
                if salir(True):
                    break
        elif comando == "0":
            if salir(True):
                break
        else:
            error(0)


def default_ranking(rank):
    with open(rank, "w") as ranking:
        for user_score in ["Vid/2019", "Robert Donner/1989", "Pajitnov/1984",
                           "Iwatani/1980", "Bushnell/1972", "Paper/1000",
                           "Mario/64", "Megaman/11", "Age HD/2", "Jesus/0"]:
            ranking.writelines(user_score + "\n")


def imprimir_ranking():
    global rank
    if not path.isfile(rank):
        default_ranking(rank)
    with open(rank, "rt") as ranking:
        datos = ranking.readlines()
    datos = dato_a_lista(datos)[:10]
    print("-||Top 10 Mejores puntajes||-")
    for score in datos:
        print(score[0] + ":", score[1], "ptos")


def quitar_acento(user):
    global acento
    resultado = ""
    for letra in range(len(user)):
        if user[letra] in acento:
            resultado += acento[user[letra]]
        else:
            resultado += user[letra]
    return resultado


while comando != 0:
    print("\n-||Bienvenido a LegoSweeper v1.0 Beta||-")
    menu(menu_principal, 1)
    if comando == "1":
        generar_tablero()
        partida()
    elif comando == "2":
        if cargar_tablero():
            partida()
    elif comando == "3":
        imprimir_ranking()
    elif comando == "0":
        salir(False)
    else:
        error(0)
