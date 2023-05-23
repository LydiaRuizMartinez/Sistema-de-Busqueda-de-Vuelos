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
