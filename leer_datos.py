from Vuelo import Vuelo
from Arbol import Arbol
from funciones import mostrar_texto_medio


def data_reader(fh):
    fh.readline()  # Para saltarnos la primera linea
    
    for linea in fh:
        linea = linea.split(",")
        # pasamos de millas a kilómetros con 2 decimales
        kilometros = int((float(linea[9]) * 1.61) * 100)/100
        vuelo = Vuelo(linea[5], linea[7], kilometros,
                      linea[12], float(linea[13].strip()), linea[4])
        yield vuelo


def leer_datos(fichero: str, arbol: Arbol, caracteristicas: list[str], screen=None, N: int = None) -> dict:
    """
    Lee el fichero con los vuelos y los inserta en el arbol

    Args:
        fichero (str): el nombre del fichero

    Returns:
        dict_opciones_por_caracteristica (dict): diccionario que guarda todos los posibles valores que puede tomar cada característica
    """
    print("LEYENDO DATOS", end="")

    dict_opciones_por_caracteristica: dict = {}
    for caracteristica in caracteristicas:
        dict_opciones_por_caracteristica[caracteristica] = []
    j = 1
    with open(fichero, "r") as fh:
        
        for vuelo in data_reader(fh):
            
            arbol.insertar_vuelo(vuelo)
            
            for caracteristica in caracteristicas:
                valor = getattr(vuelo, caracteristica)
                if valor not in dict_opciones_por_caracteristica[caracteristica]:
                    dict_opciones_por_caracteristica[caracteristica].append(
                        valor)
            
            if screen != None and j % 500_000 == 0:
                mostrar_texto_medio(
                    screen, f"Cargando 9.534.417 vuelos... {j/9_534_417:.02%}")
            
            j += 1
        
        print("\nCarga de datos finalizada")
    
    return dict_opciones_por_caracteristica
