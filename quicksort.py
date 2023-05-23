class Vuelo:
    """
    La clase Vuelo
    Contiene las características de cada vuelo
    """

    def __init__(self, origen: str, destino: str, kilometros: float, compania: str, precio: float, trimestre: int):
        self.origen: str = origen
        self.destino: str = destino
        self.kilometros: float = kilometros
        self.compania: str = compania
        self.precio: float = precio
        self.trimestre: int = trimestre

    def __repr__(self) -> str:
        return f"Vuelo(origen = {self.origen}, destino = {self.destino}, trimestre = {self.trimestre}, compañía = {self.compania}, precio = {self.precio}, km = {self.kilometros})"


def divide(vuelos, iz, de):
    """
    Encuentra la posición de partición en el array
    Args:
        vuelos: El array a ordenar
        iz: El índice izquierdo
        de: El índice derecho
    """
    pivote = vuelos[de].precio  # Elige como pivote el elemento A[de]

    i = iz - 1  # Inicializa el puntero

    for j in range(iz, de):
        if vuelos[j].precio <= pivote:

            i = i + 1  # Mueve el puntero
            (vuelos[i], vuelos[j]) = (vuelos[j], vuelos[i])  # Intercambia el elemento i con el j

    # Intercambia el pivote con el elemento de la posición i+1
    (vuelos[i + 1], vuelos[de]) = (vuelos[de], vuelos[i + 1])

    return i + 1


def quickSort(vuelos, iz, de):
    """
    Función principal que implementa el algoritmo de Quicksort
    Args:
        A: El array a ordenar
        iz: El índice izquierdo
        de: El índice derecho
    """
    if iz < de:

        piv = divide(vuelos, iz, de)  # Para encontrar la posición de partición

        quickSort(vuelos, iz, piv - 1)  # Para ordenar el lado izquierdo

        quickSort(vuelos, piv + 1, de)  # Para ordenar el lado derecho
    return vuelos


vuelos = [
    Vuelo(origen="sgv", destino="shgb", kilometros=1000.0,
          compania="shg", precio=200, trimestre=1),
    Vuelo(origen="shb", destino="shf", kilometros=1500.0,
          compania="shf", precio=350, trimestre=2),
    Vuelo(origen="jfg", destino="jfng", kilometros=1200.0,
          compania="shf", precio=280, trimestre=1),
    Vuelo(origen="jfnv", destino="jgnv", kilometros=800.0,
          compania="dhg", precio=180, trimestre=3),
    Vuelo(origen="jfnv", destino="tghju", kilometros=2000.0,
          compania="htdhgc", precio=400, trimestre=2),
    Vuelo(origen="kgjfnv", destino="tghn", kilometros=1600.0,
          compania="hdhdbc", precio=320, trimestre=3)
]

print(quickSort(vuelos, 0, len(vuelos)-1))
