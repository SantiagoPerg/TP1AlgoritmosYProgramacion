import logica as log

def iniciar_juego():
    columnas = int(input("Ingrese la cantidad de columnas del juego: "))
    filas = int(input("Ingrese la cantidad de filas del juego: "))
    movimientos_realizados = 0
    movimientos_ingresados = " "
    movimientos = []
    tablero_ordenado = log.crear_tablero([columnas,filas])
    tablero_juego, movimientos_permitidos = log.movimiento_inicial(log.crear_tablero([columnas,filas]))
    while (movimientos_realizados < movimientos_permitidos and movimientos_ingresados != "o"):
        log.mostrar_tablero(tablero_juego)
        movimientos_restantes = movimientos_permitidos - movimientos_realizados
        print("Intentos realizados: " + str(movimientos_realizados))
        print("Restan " + str(movimientos_restantes) + " movimientos")
        print("Para finalizar el juego o chequear la solucion, ingrese o")
        movimientos_ingresados = input("Ingrese los movimientos a realizar: ")
        for letra in movimientos_ingresados:
            movimientos.append(letra)
            movimientos_realizados += 1
        tablero_juego = log.mover(tablero_juego, movimientos)
        movimientos.clear()
    if(tablero_ordenado == tablero_juego):
        print ("Felicitaciones!!! Ganaste!!")
    else:
        print ("Más suerte la proxima!")

iniciar_juego()
