import pygame
import ListaDoble
class CartaVuelo:
    
    def __init__(self, x, y, width, height, vuelos:ListaDoble = None, font = None) -> None:
        self.rect = pygame.Rect(x ,y, width, height)
        self.font = font if font else pygame.font.Font(None, 28)
        self.colors = {
        'BLACK' : (0, 0, 0),
        'WHITE' : (255, 255, 255),
        'GRAY' : (200, 200, 200),
        'LIGHT_GRAY' : (220, 220, 220)
        }

        self.vuelos = vuelos
        self.vuelo = None

        if self.vuelos:
            self.vuelo = self.vuelos.head