class ListaDoble:
    """
    Lista doblemente enlazada y circular
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insertar_vuelo(self, vuelo):
        if self.head == None:
            self.head = vuelo
            self.tail = vuelo
        else:
            vuelo.next = self.head
            vuelo.prev = self.tail
            self.tail.next = vuelo
            self.head.prev = vuelo
            self.tail = vuelo

    def RecorrerListaCabeza(self):
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
                

class NodoLista:
    def __init__(self, vuelo) -> None:
        self.vuelo = vuelo
        self.next = None
        self.prev = None
    
    def __repr__(self) -> str:
        return f"vuelo: {self.vuelo}"
    



lista = ListaDoble()
for i in [2,1,4,5]:
    lista.insertar_vuelo(NodoLista(i))

lista.RecorrerListaCabeza()
print(lista.head, lista.tail)
