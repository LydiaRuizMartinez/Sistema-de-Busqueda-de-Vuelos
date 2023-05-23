from Vuelo import Vuelo
from Arbol import Arbol

def leer_datos(fichero:str, arbol:Arbol, N:int = None) -> Arbol:
    """
    Lee el fichero con los vuelos y los inserta en el arbol

    Args:
        fichero (str): el nombre del fichero

    Returns:
        arbol (Arbol): el arbol con todos los vuelos metidos
    """
    if N == None:
        N = 100

    with open(fichero, "r") as fh:
        keys = fh.readline()
        # keys = keys.split(",")
        for _ in range(N):
        # for linea in fh:
            linea = fh.readline()
            linea = linea.split(",")
            kilometros = int((float(linea[9]) * 1.61) * 100)/100 # pasamos de millas a kilómetros con 2 decimales
            vuelo = Vuelo(linea[5], linea[7], kilometros, linea[12], float(linea[13].strip()), int(linea[4]))
            arbol.insertar_vuelo(vuelo)

    return arbol
