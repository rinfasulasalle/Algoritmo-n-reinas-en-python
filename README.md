# Algoritmo-n-reinas-en-python
A continuacion, la explicacion del codigo
```python
def disponibles(y, n, columna, diagonal_izquierda, diagonal_derecha):
    columnas_disponibles = []
    for x in range(n):
        if (columna[x] or diagonal_izquierda[x + y] or diagonal_derecha[x - y + n - 1]):
            continue
        columnas_disponibles.append(x)
    return columnas_disponibles
```
Aquí tenemos una función llamada `disponibles` que toma como argumentos la posición de una reina `(y)`, el tamaño del tablero `(n)`, las listas `columna`, `diagonal_izquierda` y `diagonal_derecha`. Esta función devuelve una lista de columnas disponibles para colocar una reina en la fila `y`. Comprueba si una columna, una diagonal izquierda o una diagonal derecha están atacadas por alguna reina y agrega las columnas no atacadas a la lista `columnas_disponibles`.

```python
def nReinasVegas(n):
    solucion = []
    while (len(solucion) != n and n > 3):
        solucion = []
        columna = [False] * n
        diagonal_derecha = [False] * (n * 2)
        diagonal_izquierda = [False] * (n * 2)
        for i in range(n):
            columnas_disponibles = disponibles(i, n, columna, diagonal_izquierda, diagonal_derecha)
            if (columnas_disponibles):
                x = random.choice(columnas_disponibles)
            else:
                break
            columna[x] = diagonal_izquierda[x + i] = diagonal_derecha[x - i + n - 1] = True
            solucion.append((i, x))
    return solucion
```
Aquí tenemos la función `nReinasVegas`, que utiliza un algoritmo de búsqueda aleatoria para encontrar una solución al problema de las N reinas. La función toma como argumento el tamaño del tablero `(n)`. Utiliza un bucle `while` para iterar hasta que se encuentre una solución válida o hasta que `n` sea menor o igual a 3 (no hay solución para `n` menor a 4).

Dentro del bucle `while`, se reinicia la lista `solucion` y se crean tres listas: `columna`, `diagonal_derecha` y `diagonal_izquierda`, todas inicializadas con valores booleanos `False`. Estas listas se utilizan para realizar un seguimiento de las columnas, diagonales izquierdas y diagonales derechas atacadas por las reinas colocadas.

Luego, se itera sobre las filas del tablero y se llama a la función `disponibles` para obtener las columnas disponibles para colocar una reina en esa fila. Si hay columnas disponibles, se elige aleatoriamente una de ellas utilizando `random.choice`, se marca esa columna, la diagonal izquierda

 y la diagonal derecha como atacadas, y se agrega la posición `(fila, columna)` a la lista `solucion`.

Una vez que se encuentra una solución válida o se determina que no hay solución para `n`, se devuelve la lista `solucion`.

```python
def main():
    start = time()
    n = 500
    matrix_solucion = []
    for i in range(n):
        list_temp = ['*'] * n
        matrix_solucion.append(list_temp)
    solucionNQ = nReinasVegas(n)
    for j in solucionNQ:
        matrix_solucion[j[0]][j[1]] = '👑'
    print(solucionNQ)
    for i in matrix_solucion:
        print('-----' * n)
        print(i)
    end = time() - start
    print("Total ", end, " segundos.")

main()
```
En la función `main`, se realiza el flujo principal del programa. Primero, se inicializa una variable `start` con el tiempo actual utilizando `time()` para medir el tiempo de ejecución.

Luego, se define el tamaño del tablero `n` como 500. Se crea una lista bidimensional `matrix_solucion` de tamaño `n x n` inicializada con el carácter `'*'`. Esta lista se utiliza para representar visualmente el tablero con las reinas.

# Ejecucion 
Para poder ejecutar el código, debemos seguir los siguientes pasos según el sistema operativo:

### Windows:
1. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde el sitio web oficial de Python (https://www.python.org) y seguir las instrucciones de instalación.

2. Guarda el código en un archivo con extensión `.py`, por ejemplo, `nreinas.py`.

3. Abre la línea de comandos (Command Prompt) en tu sistema Windows.

4. Navega hasta la ubicación donde hayas guardado el archivo `nreinas.py` usando el comando `cd <ruta>`.

5. Ejecuta el código Python usando el siguiente comando:
   ```
   python nreinas.py
   ```

### Linux:
1. Asegúrate de tener Python instalado en tu sistema. La mayoría de las distribuciones de Linux ya incluyen Python de forma predeterminada.

2. Guarda el código en un archivo con extensión `.py`, por ejemplo, `nreinas.py`.

3. Abre una terminal en tu sistema Linux.

4. Navega hasta la ubicación donde hayas guardado el archivo `nreinas.py` usando el comando `cd <ruta>`.

5. Ejecuta el código Python usando el siguiente comando:
   ```
   python3 nreinas.py
   ```

Al ejecutar el código, verás la solución encontrada para el problema de las N reinas en el tablero. Además, se imprimirá una representación visual del tablero con las reinas marcadas como "👑". Al final, se mostrará el tiempo total de ejecución en segundos.

Recuerda que debes tener instalado Python en tu sistema y configurar correctamente las variables de entorno para poder ejecutarlo desde cualquier ubicación en la línea de comandos.

A continuación, se llama a la función `nReinasVegas` con `n` como argumento para obtener la solución al problema de las N reinas.

Después, se recorre la lista de posiciones `solucionNQ` y se marca las celdas correspondientes en `matrix_solucion` con el símbolo `'👑'`.

Luego, se imprime la lista `solucionNQ`, que contiene las posiciones de las reinas.

A continuación, se imprime visualmente el tablero utilizando la lista `matrix_solucion`, mostrando las reinas como `'👑'` y las celdas vacías como `'*'`.

Finalmente, se calcula el tiempo total de ejecución restando el tiempo actual (`time()`) menos `start`, y se imprime en segundos.
