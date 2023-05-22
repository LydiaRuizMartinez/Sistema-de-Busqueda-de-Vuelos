from Vuelo import Vuelo
import pickle

def leer_fichero(fichero:str):

    vuelos:list[Vuelo] = []
    with open(fichero, "r") as fh:
        keys = fh.readline()
        keys = keys.split(",")
        print(keys)
        print(len(keys))

        for i in range(10):
            linea = fh.readline()
            linea = linea.split(",")
            print(linea)
            print(len(linea))
            kilometros = float(linea[9]) * 1.60934 # pasamos de millas a kilómetros
            vuelo = Vuelo(linea[5], linea[7], kilometros, linea[12], float(linea[13].strip()), int(linea[4]))
            vuelos.append(vuelo)
    print(vuelos)
    with open("vuelos.obj", "wb") as f:
        pickle.dump(vuelos, f)
    return vuelos

leer_fichero("Cleaned_2018_Flights.csv")