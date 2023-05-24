from Vuelo import Vuelo


def divide(vuelos: list[Vuelo], iz: int, de: int) -> int:
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
            # Intercambia el elemento i con el j
            (vuelos[i], vuelos[j]) = (vuelos[j], vuelos[i])

    # Intercambia el pivote con el elemento de la posición i+1
    (vuelos[i + 1], vuelos[de]) = (vuelos[de], vuelos[i + 1])

    return i + 1


def quickSort(vuelos: list[Vuelo], iz: int = 0, de: int = None) -> list[Vuelo]:
    """
    Función principal que implementa el algoritmo de Quicksort
    Args:
        vuelos: El array a ordenar
        iz: El índice izquierdo
        de: El índice derecho
    """
    if not vuelos:  # Por si no hay vuelos
        return

    if de == None:
        de = len(vuelos)-1

    if iz < de:

        piv = divide(vuelos, iz, de)  # Para encontrar la posición de partición

        quickSort(vuelos, iz, piv - 1)  # Para ordenar el lado izquierdo

        quickSort(vuelos, piv + 1, de)  # Para ordenar el lado derecho
    return vuelos
