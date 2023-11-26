# Coordenadas de los muros
muro = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))
"""
Defino la clase del laberinto (la clase no es más que la estructura que toman los objetos basados en esa
clase), que contiene las funciones necesarias para crearlos estas son funciones o métodos, que es como se le 
conocen a las funciones dentro de una clase. La primera es el constructorque es la que inicia los atributos 
de la instancia, la segunda crea el muero (con las X donde hay muro)y los puntos de inicio (S) y de fin (E). 
Por último, la función que genera un laberinto aleatorio con 5 filas y 5 columnas (en este caso).
"""
class Laberinto:
    """
    la primera función, es el constructor, que contiene los atributos del laberinto, es decir, numero de 
    filas y de columnas, una lista de listas para representar el laberinto, y por último, la creación final
    del laberinto que llama a una función definida posteriormente para la creación del muro
    """
    def __init__(self, muro):
        self.filas = 5
        self.columnas = 5
        self.laberinto = [[' ' for _ in range(self.columnas)] for _ in range(self.filas)]
        self.crear_laberinto(muro)
    """
    Esta función se encarga de crear el laberinto, con las casillas que contienen muros representadas con una X, y las
    de Start(S) y End(E). Cabe recalcar, que en python antes de ejecutar el código, se "lee"primero para registrar las funciones 
    y clases definidas. De esta forma se ha llamado antes a la función de creación del muro después de su definición.
    """
    def crear_laberinto(self, muro):
        for fila, columna in muro:
            self.laberinto[fila][columna] = 'X'
        
        # Agregar posición de inicio (E) y salida (S)
        self.laberinto[0][0] = 'E'
        self.laberinto[self.filas - 1][self.columnas - 1] = 'S' 
    """
    Esta última función, es la que se encarga de printear los muros y las casillas "E" y "S"   
    """   
    def imprimir_laberinto(self):
        for fila in self.laberinto:
            print(' '.join(fila))

# Crea la instancia de la clase Laberinto (El objeto en si)
laberinto = Laberinto(muro)

# Imprime el laberinto en consola
laberinto.imprimir_laberinto()
