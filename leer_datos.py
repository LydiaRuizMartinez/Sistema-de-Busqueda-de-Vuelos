from Vuelo import Vuelo
import pickle

def leer_fichero(fichero:str):
    """
    Lee el fichero con los vuelos

    Args:
        fichero (str): el nombre del fichero

    Returns:
        vuelos (list): lista con los objetos de todos los vuelos
    """
    vuelos:list[Vuelo] = []
    with open(fichero, "r") as fh:
        keys = fh.readline()
        keys = keys.split(",")

        for _ in range(1000):
        # for linea in fh:
            linea = fh.readline()
            linea = linea.split(",")
            kilometros = int((float(linea[9]) * 1.61) * 100)/100 # pasamos de millas a kilómetros con 2 decimales
            vuelo = Vuelo(linea[5], linea[7], kilometros, linea[12], float(linea[13].strip()), int(linea[4]))
            vuelos.append(vuelo)
    
    with open("vuelos.obj", "wb") as f:
        pickle.dump(vuelos, f)
    return vuelos

# leer_fichero("Cleaned_2018_Flights.csv")