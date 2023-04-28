class Vuelo:
    def __init__(self, origen, destino, kilometros, compania, precio):
        self.origen = origen
        self.destino = destino
        self.kilometros = kilometros
        self.compania = compania
        self.precio = precio

    def __repr__(self) -> str:
        return f"Vuelo(origen = {self.origen}, destino = {self.destino}, compañía = {self.compania}, precio = {self.precio}, km = {self.kilometros})"
