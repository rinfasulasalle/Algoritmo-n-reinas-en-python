import random
from time import time
# Metodo que me indica las columnas que estan disponibles
def disponibles(y, n, columna, diagonal_izquierda, diagonal_derecha):
    columnas_dsiponibles = []
    for x in range(n):
        # por cada columna que hay,
        # if : verifico si esas columnas estan atacadas
        # si estana tacadas pasa
        # si no esta atacada la agrega a columans disponibles
        if (columna[x] or diagonal_izquierda[x + y] or diagonal_derecha[x - y + n - 1]):
            continue
        columnas_dsiponibles.append(x)
    return columnas_dsiponibles
# Metodo que realiza el recorrido en las difernetes listas    y me retorna
#una lista con las tuplas de una posible solucion basado en vegas
def nReinasVegas(n):
    solucion = []
    # mientras la solucion no haya reina por cada fila, no hay solucion para numeros menores a 4
    while (len(solucion) != n and n > 3):
        solucion = []
        columna = [False] * n
        diagonal_derecha = [False] * (n * 2)
        diagonal_izquierda = [False] * (n * 2)
        for i in range(n): # recorrido fila
            columnasDisponibles = disponibles(i, n, columna, diagonal_izquierda,diagonal_derecha)
            if (columnasDisponibles):
                x = random.choice(columnasDisponibles)
                # si hay mas de una columna disponible, va a escoger aleatoriamente entre las columnas disponibles
            else:
                # sino, significa que no hay columnas disponibles ya que está vacio, vuelve a generar el tablero
                break
            # Agrego la reina
            columna[x] = diagonal_izquierda[x + i] = diagonal_derecha[x - i + n -1] = True
            solucion.append((i, x))
    return solucion
def main():
    start = time()
    n = 500
    matrixSolucion = []
    for i in range(n): # crea tablero
        listTemp1 = ['*'] * n
        matrixSolucion.append(listTemp1)
    solucionNQ = nReinasVegas(n)
    for j in solucionNQ:
        matrixSolucion[j[0]][j[1]] = '👑'
    print(solucionNQ)
    for i in matrixSolucion:
        print('-----' * n)
        print(i)
    end = time() - start
    print("Total ",end," segundos.")
# -------------------
main()