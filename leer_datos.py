from Vuelo import Vuelo
from Arbol import Arbol

def leer_datos(fichero:str, arbol:Arbol, caracteristicas:list[str], N:int = None) -> dict:
    """
    Lee el fichero con los vuelos y los inserta en el arbol

    Args:
        fichero (str): el nombre del fichero

    Returns:
        dict_opciones_por_caracteristica (dict): diccionario que guarda todos los posibles valores que puede tomar cada característica
    """
    if N == None:
        N = 100

    dict_opciones_por_caracteristica:dict = {}
    for caracteristica in caracteristicas:
        dict_opciones_por_caracteristica[caracteristica] = []

    with open(fichero, "r") as fh:
        keys = fh.readline()
        # keys = keys.split(",")
        # for _ in range(N):
        for linea in fh:
            # linea = fh.readline()
            linea = linea.split(",")
            
            kilometros = int((float(linea[9]) * 1.61) * 100)/100 # pasamos de millas a kilómetros con 2 decimales
            origen = linea[5]
            destino = linea[7]
            compania = linea[12]
            trimestre = linea[4]
            vuelo = Vuelo(origen, destino, kilometros, compania, float(linea[13].strip()), trimestre)
            arbol.insertar_vuelo(vuelo)

            for caracteristica in caracteristicas:
                valor = getattr(vuelo, caracteristica)
                if valor not in dict_opciones_por_caracteristica[caracteristica]:
                    dict_opciones_por_caracteristica[caracteristica].append(valor)

    return dict_opciones_por_caracteristica
