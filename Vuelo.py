class Vuelo:
    """
    La clase Vuelo
    Contiene las características de cada vuelo
    """

    def __init__(self, origen: str, destino: str, kilometros: float, compania: str, precio: float, trimestre: int) -> None:
        self.origen: str = origen
        self.destino: str = destino
        self.kilometros: float = kilometros
        self.compania: str = compania
        self.precio: float = precio
        self.trimestre: str = trimestre

    def __repr__(self) -> str:
        return f"Vuelo(origen = {self.origen}, destino = {self.destino}, trimestre = {self.trimestre}, compañía = {self.compania}, precio = {self.precio}, km = {self.kilometros})"
