from Vuelo import Vuelo


class Nodo():
    """
    Es la clase de cada Nodo que forma el Árbol
    """

    def __init__(self, orden: list[str], caracteristica: str = None, diccionario: dict = None, vuelos: list[Vuelo] = None) -> None:
        self.orden: list[str] = orden
        # ["origen", "destino", "compania", "trimestre"]
        self.caracteristica: str = caracteristica
        self.diccionario: dict[str, Nodo] = {
        } if diccionario == None else diccionario
        self.vuelos: list[Vuelo] = [] if vuelos == None else vuelos

    def __repr__(self) -> str:
        return f"Nodo(característica = {self.caracteristica})"


class Arbol():
    """
    Clase del árbol
    Este árbol es una estructura que sirve para guardar los vuelos que tienen las mismas características
    """

    def __init__(self, orden: list[str]) -> None:
        self.raiz: Nodo = None
        self.orden: list[str] = orden

    def insertar_vuelo(self, vuelo: Vuelo) -> None:
        """
        Añade el vuelo en su correcto lugar en el árbol

        Args:
            vuelo (Vuelo): El objeto del vuelo a añadir
        """
        if self.raiz == None:  # Se crea la raíz del nodo
            self.raiz: Nodo = Nodo(self.orden, self.orden[0])

        nodo: Nodo = self.raiz
        # mira si está la caracteristica del vuelo en el diccionario del vuelo  |  ver si vuelo.origen in nodo.dict
        posicion: int = 0
        for caracteristica in self.orden:  # Recorre el árbol a partir de las características
            atributo: str = getattr(
                vuelo, caracteristica)   # Atributo del vuelo
            if atributo not in nodo.diccionario:
                if posicion + 1 >= len(self.orden):
                    nuevo_nodo = Nodo(self.orden)
                else:
                    nuevo_nodo = Nodo(self.orden, self.orden[posicion+1])
                nodo.diccionario[atributo] = nuevo_nodo

            nodo = nodo.diccionario[atributo]

            posicion = posicion + 1

        nodo.vuelos.append(vuelo)

    def mostrar(self, nodo: Nodo = None, rama: str = "") -> None:
        """
        Muestra la lista de vuelos de cada rama y el camino hasta ella

        Args:
            nodo (Nodo): El nodo desde el que se muestra (no poner nada para que empiece desde la raíz)
            rama (str): La string con el camino que lleva

        Returns:
            None
        """
        if nodo == None:  # Coge la raíz si no se le pasa ningún nodo
            nodo: Nodo = self.raiz

        if nodo:  # Para comprobar que el árbol no esté vacío
            for key, nodo_hijo in nodo.diccionario.items():
                if nodo_hijo.vuelos:  # Si el nodo hijo tiene los vuelos, muestra la rama
                    print(rama + "->"+key+":", len(nodo_hijo.vuelos), "vuelos")
                else:  # Si el nodo hijo no tiene los vuelos, vuelve a mostrar desde él mismo
                    self.mostrar(nodo_hijo, rama + "->" + str(key))

    def _get_vuelos_ramas(self, nodo: Nodo, vuelos: list[Vuelo] = None) -> list:
        """
        Busca los buelos de las ramas de un nodo

        Args:
            nodo (Nodo): El nodo desde que se quiere buscar todos los vuelos
            vuelos (list): La lista con los vuelos que ya se han añadido

        Returns:
            vuelos (list)
        """
        if vuelos == None:  # Se crea la lista de vuelos
            vuelos = []

        for nodo_hijo in nodo.diccionario.values():  # Se recorren los nodos hijos
            if nodo_hijo.vuelos:
                vuelos += nodo_hijo.vuelos
            else:
                # Se buscan los vuelos desde hijos del nodo
                self._get_vuelos_ramas(nodo_hijo, vuelos)

        return vuelos

    def buscar(self, filtros: list[str]) -> list[Vuelo]:
        """
        Busca los vuelos según ciertos filtros

        Args:
            filtos (list): lista con los valores de las caracteristicas de los vuelos que se quieren
        Returns:
            vuelos (list): lista de los vuelos
        """
        nodo = self.raiz
        i: int = 0
        while i < len(filtros) and i >= 0:  # Recorre los nodos a partir de los filtros
            filtro = filtros[i]
            caracteristica = nodo.caracteristica
            if filtro:
                nodo = nodo.diccionario.get(filtro, None)
            if nodo:
                i += 1
            else:
                i = -1

        if i == -1:
            mensaje = f"No hay ningún vuelo con esas características"
            return None, mensaje

        if nodo.vuelos:  # Si tiene los vuelos, se devuelven
            vuelos = nodo.vuelos
        else:
            # Si no tiene los vuelos, devuelve todos los vuelos de las ramas de ese nodo
            vuelos = self._get_vuelos_ramas(nodo)
        return vuelos, ""
