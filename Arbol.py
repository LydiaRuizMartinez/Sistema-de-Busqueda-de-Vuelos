class Arbol():
    def __init__(self,orden:list[str]):
        self.raiz = None
        self.orden = orden

    def insertar_vuelo(self,vuelo):
        if self.raiz == None:
            self.raiz = Nodo(self.orden, self.orden[0])
        nodo:Nodo = self.raiz
        # mira si está la caracteristica del vuelo en el diccionario del vuelo  |  ver si vuelo.origen in nodo.dict
        posicion:int = 0
        for caracteristica in self.orden:
            atributo = getattr(vuelo, caracteristica)   # Atributo del vuelo
            if atributo not in nodo.diccionario:
                print(f"EL atributo {atributo} no está en el diccionario {nodo.diccionario} de {nodo}")
                if posicion+1>=len(self.orden):
                    nuevo_nodo = Nodo(self.orden)
                else:
                    nuevo_nodo = Nodo(self.orden, self.orden[posicion+1])
                nodo.diccionario[atributo] = nuevo_nodo
                print(f"\tDESPUES -> {nodo.diccionario}, {nodo.diccionario.values()}")
            
            nodo = nodo.diccionario[atributo]

            posicion = posicion + 1
        
        nodo.vuelos.append(vuelo)
        return nodo   # Return simplemente para las pruebas
        # si no está, la añade al diccionario con un nodo

        # si está, cambia al nodo del diccionario y repite el proceso

    def mostrar(self, nodo = None, rama = ""):
        if nodo == None:
            nodo = self.raiz

        if nodo:
            
            for key,nodo_hijo in nodo.diccionario.items():
                if nodo_hijo.vuelos:
                    print(rama + "->"+str(key), ":", nodo_hijo.vuelos)
                else:
                    self.mostrar(nodo_hijo, rama +"->"+ str(key))

    def _get_vuelos_ramas(self, nodo, vuelos = None):
        if vuelos == None:
            vuelos = []
        for nodo_hijo in nodo.diccionario.values():
            if nodo_hijo.vuelos:
                vuelos += nodo_hijo.vuelos
            else:
                self._get_vuelos_ramas(nodo_hijo, vuelos)
        
        return vuelos

    def buscar(self, filtros:list[str]):
        nodo = self.raiz
        i:int = 0

        while i < len(filtros) and i >= 0:
            if nodo:
                filtro = filtros[i]
                nodo = nodo.diccionario.get(filtro, None)
                i += 1
            else:
                i = -1
        
        if i == -1:
            print(f"No hay ningún vuelo con {filtro}")
            return None

        if nodo.vuelos:  # Si tiene los vuelos, se devuelven
            return nodo.vuelos
        
        vuelos =  self._get_vuelos_ramas(nodo) # Si no tiene los vuelos, devuelve todos los vuelos de las ramas de ese nodo
        return vuelos


class Nodo():
    def __init__(self, orden:list[str], caracteristica:str = None, diccionario:dict = None, vuelos = None):
        self.orden:list[str] = orden
        self.caracteristica:str = caracteristica   # ["origen", "destino", "compania", "trimestre"]
        self.diccionario:dict = {} if diccionario == None else diccionario
        self.vuelos:list = [] if vuelos == None else vuelos

    def __repr__(self) -> str:
        return f"Nodo(característica = {self.caracteristica})"