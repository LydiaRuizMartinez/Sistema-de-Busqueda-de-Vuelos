import pygame
from ListaDoble import ListaDoble, NodoLista


class CartaVuelo:

    def __init__(self, x:int, y:int, width:int, height:int, vuelos: ListaDoble = None, font = None) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font if font else pygame.font.Font(None, 45)
        self.colors = {
            'BLACK': (0, 0, 0),
            'WHITE': (255, 255, 255),
            'GRAY': (200, 200, 200),
            'LIGHT_GRAY': (220, 220, 220),
            'BLUE': (0, 0, 255)
        }

        self.set_vuelos(vuelos)

    def set_vuelos(self, vuelos):
        self.vuelos:ListaDoble = vuelos
        self.first_vuelo()

    def first_vuelo(self):
        """
        Coloca el puntero de nodo_vuelo en el primer vuelo de la lista
        """
        if self.vuelos:
            self.nodo_vuelo: NodoLista = self.vuelos.head
        else:
            self.nodo_vuelo: NodoLista = None

    def last_vuelo(self):
        self.nodo_vuelo = self.vuelos.tail

    def next_vuelo(self):
        self.nodo_vuelo = self.nodo_vuelo.next

    def prev_vuelo(self):
        self.nodo_vuelo = self.nodo_vuelo.prev

    def draw(self, screen) -> None:
        """
        Dibuja la información del vuelo
        """
        pygame.draw.rect(screen, self.colors["BLUE"], self.rect)

        x, y = self.rect.center
        text = self.font.render(
            f"{self.nodo_vuelo.get_id()}/{self.vuelos.n_nodos}", True, self.colors["WHITE"])
        text_rect = text.get_rect(center=(x, y - 250))
        screen.blit(text, text_rect)
        text = self.font.render(
            f"Origen: {self.nodo_vuelo.vuelo.origen}", True, self.colors["WHITE"])
        text_rect = text.get_rect(center=(x, y - 150))
        screen.blit(text, text_rect)
        text = self.font.render(
            f"Destino: {self.nodo_vuelo.vuelo.destino}", True, self.colors["WHITE"])
        text_rect = text.get_rect(center=(x, y - 90))
        screen.blit(text, text_rect)
        text = self.font.render(
            f"Trimestre: {self.nodo_vuelo.vuelo.trimestre}", True, self.colors["WHITE"])
        text_rect = text.get_rect(center=(x, y - 30))
        screen.blit(text, text_rect)
        text = self.font.render(
            f"Compañía: {self.nodo_vuelo.vuelo.compania}", True, self.colors["WHITE"])
        text_rect = text.get_rect(center=(x, y + 30))
        screen.blit(text, text_rect)
        text = self.font.render(
            f"Distancia: {self.nodo_vuelo.vuelo.kilometros}km", True, self.colors["WHITE"])
        text_rect = text.get_rect(center=(x, y + 90))
        screen.blit(text, text_rect)
        text = self.font.render(
            f"Precio: {self.nodo_vuelo.vuelo.precio}€", True, self.colors["WHITE"])
        text_rect = text.get_rect(center=(x, y + 150))

        screen.blit(text, text_rect)
