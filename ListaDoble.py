from Vuelo import Vuelo


class NodoLista:
    def __init__(self, vuelo: Vuelo, id: int) -> None:
        self.vuelo: Vuelo = vuelo
        self.next: NodoLista = None
        self.prev: NodoLista = None
        self.id: int = id

    def get_id(self):
        return self.id

    def __repr__(self) -> str:
        return f"vuelo: {self.vuelo}"


class ListaDoble:
    """
    Lista doblemente enlazada y circular
    """

    def __init__(self) -> None:
        self.head: NodoLista = None
        self.tail: NodoLista = None
        self.n_nodos = 0

    def insertar_vuelo(self, vuelo: Vuelo) -> None:
        """
        Inserta el vuelo al final de la lista

        Args:
            vuelo (Vuelo): el vuelo a insertar
        """
        self.n_nodos += 1
        nodo_vuelo = NodoLista(vuelo, self.n_nodos)
        if self.head == None:
            self.head = nodo_vuelo
            self.tail = nodo_vuelo
        else:
            nodo_vuelo.next = self.head
            nodo_vuelo.prev = self.tail
            self.tail.next = nodo_vuelo
            self.head.prev = nodo_vuelo
            self.tail = nodo_vuelo

    def RecorrerListaCabeza(self) -> None:
        print("RECORRIDO DE LISTA DESDE LA CABEZA: ")
        if self.head is None:
            print("No existen elementos para recorrer")
        else:
            aux = self.head
            while aux:
                print(aux)
                if self.tail == aux:
                    aux = False
                else:
                    aux = aux.next
