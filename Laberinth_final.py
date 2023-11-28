"""
El módulo "laberinth", es una función creada por mi para la primera práctica del laberinto.
hago un import de ese módulo, para evitar poner tódo el código, encargado de printear el laberinto, 
con las X donde hay muro, y la casilla de comienzo "E" y de fin "S". En este caso, lo único que estoy
haciendo, es importar la clase del laberinto, que es lo que necesito.
"""
import laberinto_módulo

# Cambio el nombre de la instancia de laberinto para evitar conflictos, ya que al haber hecho un impo
lab_instancia = laberinto_módulo.Laberinto(laberinto_módulo.muro)
"""
Para el programa que va a recorrer el laberinto y va a printear, los movimientos que ha de hacer para llegar
desde la entrada hasta la salida, he decidido simplemente definir una función que contendrá a otras en ved
de hacerlo con una clase, de esta forma, el código es más sencillo. Además la función hace todo el rato lo
mismo. Esto se consigue gracias a el algorítmo de busqueda en profundidad dfs o "Depth-First Search", de esta 
forma, el programa encontrará la salida
"""
def recorrer_laberinto(lab):
    #Almacena los movimientos en una lista, para mostrarla después
    movimientos = []
    
    def dfs(fila, columna):
        # Verifica si estamos en la salida (si se cumple el if, quiere decir que estamos en la salida)
        if fila == lab.filas - 1 and columna == lab.columnas - 1:
            return True
        
        # Marcar la casilla actual como vista (registrada)
        lab.laberinto[fila][columna] = 'V'
        
        # Intenta moverse hacia abajo, si lo consigue, añade el movimiento a la lista
        if fila + 1 < lab.filas and lab.laberinto[fila + 1][columna] not in ('X', 'V'):
            movimientos.append('Abajo')
            if dfs(fila + 1, columna):
                return True
            movimientos.pop()  # Deshace el movimiento si no lleva a la casilla de Salida
        
        # Intenta moverse hacia la derecha, si lo consigue, añade el movimiento a la lista
        if columna + 1 < lab.columnas and lab.laberinto[fila][columna + 1] not in ('X', 'V'):
            movimientos.append('Derecha')
            if dfs(fila, columna + 1):
                return True
            movimientos.pop()    
        
        # Intenta moverse hacia arriba
        if fila - 1 >= 0 and lab.laberinto[fila - 1][columna] not in ('X', 'V'):
            movimientos.append('Arriba')
            if dfs(fila - 1, columna):
                return True
            movimientos.pop()
        
        # Intenta moverse hacia la izquierda
        if columna - 1 >= 0 and lab.laberinto[fila][columna - 1] not in ('X', 'V'):
            movimientos.append('Izquierda')
            if dfs(fila, columna - 1):
                return True
            movimientos.pop()
        
        return False  # No hay movimientos válidos desde esta posición
    
    # Llama a la función de búsqueda en profundidad
    dfs(0, 0)
    
    return movimientos
"""
Llama a la función recorrer_laberinto pasándole como argumento la instancia del laberinto lab_instancia.
Luego, imprime la lista de movimientos resultante, para mostrar en pantalla en forma de lista "[]"
"""
movimientos = recorrer_laberinto(lab_instancia)
print(movimientos)
