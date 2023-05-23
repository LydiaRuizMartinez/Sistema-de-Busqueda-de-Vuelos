from Vuelo import Vuelo
class NodoLista:
    def __init__(self, vuelo:Vuelo) -> None:
        self.vuelo:Vuelo = vuelo
        self.next:NodoLista = None
        self.prev:NodoLista = None
    
    def __repr__(self) -> str:
        return f"vuelo: {self.vuelo}"


class ListaDoble:
    """
    Lista doblemente enlazada y circular
    """
    def __init__(self) -> None:
        self.head:NodoLista = None
        self.tail:NodoLista = None

    def insertar_vuelo(self, nodo_vuelo:NodoLista) -> None:
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



lista = ListaDoble()
for i in [2,1,4,5]:
    lista.insertar_vuelo(NodoLista(i))

lista.RecorrerListaCabeza()
print(lista.head, lista.tail)
