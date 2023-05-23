import pygame
class SearchButton:
    def __init__(self, x, y, width, height, font = None):
        self.rect = pygame.Rect(x ,y, width, height)

        self.font = font if font else pygame.font.Font(None, 28)
        self.colors = {
        'BLACK' : (0, 0, 0),
        'WHITE' : (255, 255, 255),
        'GRAY' : (200, 200, 200),
        'LIGHT_GRAY' : (220, 220, 220)
        }
        self.color_to_draw = "GRAY"

    def draw(self, screen):
        # Draw the main dropdown button
        pygame.draw.rect(screen, self.colors[self.color_to_draw], self.rect)
        pygame.draw.rect(screen, self.colors["BLACK"], self.rect, 2)

        
        text = self.font.render("Buscar", True, self.colors["BLACK"])
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def _check_filtros(self, filtros_array):
        N = len(filtros_array)
        i = 0
        while i < N - 1: # El último elemento es optativo
            if filtros_array[i] == None:
                print("Debe poner todos los filtros obligatorios")
                return False
            i += 1
        return True


    def handle_event(self, event, arbol, filtros_array):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color_to_draw = "LIGHT_GRAY"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               if self._check_filtros(filtros_array):
                    vuelos =  arbol.buscar(filtros_array)
                    for i in range(len(filtros_array)):
                       filtros_array[i] = None
                    return vuelos
        else:
            self.color_to_draw = "GRAY"
        