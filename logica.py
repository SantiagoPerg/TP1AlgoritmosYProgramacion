import random

MULTIPLICADOR_MOV_PERMITIDOS = 5
MOVIMIENTO_ARRIBA = "w"
MOVIMIENTO_DERECHA = "d"
MOVIMIENTO_IZQUIERDA = "a"
MOVIMIENTO_ABAJO = "s"


#Tablero es una matriz. Movimientos una lista de string.
def mover(tablero, movimientos):
    for movimiento in movimientos:
        if(movimiento == MOVIMIENTO_IZQUIERDA):
            tablero = mover_izquierda(tablero)
        elif(movimiento == MOVIMIENTO_DERECHA):
            tablero = mover_derecha(tablero)
        elif(movimiento == MOVIMIENTO_ARRIBA):
            tablero = mover_arriba(tablero)
        elif(movimiento == MOVIMIENTO_ABAJO):
            tablero = mover_abajo(tablero)
    return tablero

def mover_izquierda(tablero):
    columna, fila = localizar_espacio(tablero)
    if columna != len(tablero[0]):
        auxiliar_posicion = tablero [fila - 1][columna]
        tablero [fila - 1][columna] = " "
        tablero [fila - 1][columna - 1] = auxiliar_posicion
    return tablero

def mover_derecha(tablero):
    columna, fila = localizar_espacio(tablero)
    if columna != 1:
        auxiliar_posicion = tablero [fila - 1][columna - 2]
        tablero [fila - 1][columna - 2] = " "
        tablero [fila - 1][columna-1] = auxiliar_posicion
    return tablero

def mover_abajo(tablero):
    columna, fila = localizar_espacio(tablero)
    if fila != 1:
        auxiliar_posicion = tablero [fila - 2][columna - 1]
        tablero [fila - 2][columna - 1] = " "
        tablero [fila - 1][columna - 1] = auxiliar_posicion
    return tablero

def mover_arriba(tablero):
    columna, fila = localizar_espacio(tablero)
    if fila != len(tablero):
        auxiliar_posicion = tablero [fila][columna - 1]
        tablero [fila][columna - 1] = " "
        tablero [fila - 1][columna - 1] = auxiliar_posicion
    return tablero

#Localiza el espacio en blanco para el siguiente movimiento
def localizar_espacio(tablero):
    indicador_fila = 1
    for lista in tablero:
        indicador_columna = 1
        for elemento in lista:
            if ( elemento == " " ):
                return indicador_columna, indicador_fila
            indicador_columna += 1
        indicador_fila += 1

#Recibe una lista con tamaño inicial de matriz. [Cant columnas, Cant filas]
def crear_tablero(tamanio):
    tablero = []
    auxiliar_carga = 1
    for i in range(0, tamanio[1]):
        tablero.append([])
        for j in range (0, tamanio[0]):
            tablero[i].append(str(auxiliar_carga))
            auxiliar_carga += 1
    tablero[tamanio[1] - 1][tamanio[0] - 1] = " "
    return tablero

def movimiento_inicial(tablero):
    cantidad_movimientos = 0
    movimientos = []
    for i in range (1,random.randint(10,30)):
        movimientos.append(random.choice(str(MOVIMIENTO_ARRIBA) + str(MOVIMIENTO_DERECHA) + str(MOVIMIENTO_IZQUIERDA) + str(MOVIMIENTO_ABAJO)))
        cantidad_movimientos += 1
    mover(tablero, movimientos)
    return tablero, cantidad_movimientos * MULTIPLICADOR_MOV_PERMITIDOS

def mostrar_tablero(tablero):
    for fila in tablero:
        for valor in fila:
            print("\t", valor, end=" ")
        print()















    
