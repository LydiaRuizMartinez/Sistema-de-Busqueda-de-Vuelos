from Arbol import Arbol
from leer_datos import leer_datos
from quicksort import quickSort


if __name__ == "__main__":
    arbol = Arbol(["origen", "destino","trimestre", "compania"])
    N = 1000
    
    leer_datos("Cleaned_2018_Flights.csv", arbol, N)
    arbol.mostrar()
    print(len(arbol.buscar(["PHL","LAX",1,"AA"])))
    
    print(quickSort(arbol.buscar(["SFO","JFK",1,"AA"])))

# vuelos = [
#     Vuelo(origen="sgv", destino="shgb", kilometros=1000.0,
#           compania="shg", precio=200, trimestre=1),
#     Vuelo(origen="shb", destino="shf", kilometros=1500.0,
#           compania="shf", precio=350, trimestre=2),
#     Vuelo(origen="jfg", destino="jfng", kilometros=1200.0,
#           compania="shf", precio=280, trimestre=1),
#     Vuelo(origen="jfnv", destino="jgnv", kilometros=800.0,
#           compania="dhg", precio=180, trimestre=3),
#     Vuelo(origen="jfnv", destino="tghju", kilometros=2000.0,
#           compania="htdhgc", precio=400, trimestre=2),
#     Vuelo(origen="kgjfnv", destino="tghn", kilometros=1600.0,
#           compania="hdhdbc", precio=320, trimestre=3)
# ]

# print(quickSort(vuelos, 0, len(vuelos)-1))