class Vuelo:
    def __init__(self, origen, destino, kilometros, compania, precio, trimestre:int):
        self.origen = origen
        self.destino = destino
        self.kilometros = kilometros
        self.compania = compania
        self.precio = precio
        self.trimestre:int = trimestre

    def __repr__(self) -> str:
        return f"Vuelo(origen = {self.origen}, destino = {self.destino}, trimestre = {self.trimestre}, compañía = {self.compania}, precio = {self.precio}, km = {self.kilometros})"
