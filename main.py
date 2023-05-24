from Arbol import Arbol
from leer_datos import leer_datos
import pygame
from DropdownMenu import DropdownMenu
from SearchButton import SearchButton
from funciones import mostrar_texto_medio, imprimir_mensaje
from CartaVuelo import CartaVuelo


class MensajeError:
    """
    Clase del mensaje de error
    """
    def __init__(self) -> None:
        self.msg: str = ""

    def set_msg(self, msg="") -> None:
        self.msg = msg

    def mostrar(self, screen, font) -> None:
        """
        Muestra el mensaje de error en el medio de la pantalla
        """
        imprimir_mensaje(screen, self.msg, font, (255, 0, 0))


def main():
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    font = pygame.font.Font(None, 60)
    imp = pygame.image.load("fondo.jpg").convert()

    mostrar_texto_medio(screen, f"Cargando 9.534.417 vuelos...")

    fichero: str = "Cleaned_2018_Flights.csv"
    caracteristicas: list[str] = ["origen", "destino", "trimestre", "compania"]
    arbol: Arbol = Arbol(caracteristicas)
    dict_opciones_por_caracteristica: dict = leer_datos(
        fichero, arbol, caracteristicas, screen)

    mostrar_texto_medio(screen, "Vuelos Cargados")

    button_width:int = 225
    button_height:int = 50
    button_y:int = 50
    dropdowns: list[DropdownMenu] = []
    padding: int = (screen.get_width() - button_width *
                    (len(caracteristicas) + 1)) // 2
    
    for i in range(len(caracteristicas)):
        opciones_ordenadas = sorted(
            dict_opciones_por_caracteristica[caracteristicas[i]])
        if caracteristicas[i] == "Trimestre":
            max_visible_items = 5
        else:
            max_visible_items = 8
        dropdowns.append(DropdownMenu(items=opciones_ordenadas, indice_filtros_array=i,
                         titulo=caracteristicas[i], x=padding + button_width*i, y=button_y, width=button_width, height=button_height, max_visible_items=max_visible_items))
        

    search_button = SearchButton(x=padding + button_width*len(
        caracteristicas), y=button_y, width=button_width, height=button_height)

    carta_vuelo_width = 500
    carta_vuelo_height = 700
    carta_vuelo = CartaVuelo((screen.get_width() - carta_vuelo_width)//2,
                             (screen.get_height() - carta_vuelo_width)//2, carta_vuelo_width, carta_vuelo_height)

    running = True

    circle_radius = 50
    circle_color = (255, 255, 255)
    circle_width = 0  # 0 para que sea un circulo entero
    circle_height = (screen.get_height() -
                     carta_vuelo_width + carta_vuelo_height)//2
    previous_circle_x = (screen.get_width() -
                         carta_vuelo_width)//2 - circle_radius - 10
    next_circle_x = (screen.get_width() +
                     carta_vuelo_width)//2 + circle_radius + 10

    filtros_array: list[str] = [None for _ in range(len(caracteristicas))]

    mensaje_error = MensajeError()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass

                elif event.key == pygame.K_RIGHT:
                    if carta_vuelo.vuelos:
                        carta_vuelo.next_vuelo()

                elif event.key == pygame.K_LEFT:
                    if carta_vuelo.vuelos:
                        carta_vuelo.prev_vuelo()

                elif event.key == pygame.K_SPACE:
                    pass
                elif event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = event.pos
                if (click_pos[0] - next_circle_x) ** 2 + (click_pos[1] - circle_height) ** 2 <= circle_radius**2:
                    if carta_vuelo.vuelos:
                        carta_vuelo.next_vuelo()
                elif (click_pos[0] - previous_circle_x) ** 2 + (click_pos[1] - circle_height) ** 2 <= circle_radius**2:
                    if carta_vuelo.vuelos:
                        carta_vuelo.prev_vuelo()

            if event.type == pygame.QUIT:
                return
            
            
            for dropdown in dropdowns:
                dropdown.handle_event(event, filtros_array)
            
            search_button.handle_event(
                event, arbol, filtros_array, mensaje_error, carta_vuelo)
        
        screen.blit(imp, (0, 0))
        mensaje_error.mostrar(screen, font)
        
        if carta_vuelo.nodo_vuelo:
            carta_vuelo.draw(screen)
            pygame.draw.circle(
                screen, circle_color, (next_circle_x, circle_height), circle_radius, circle_width)
            text = font.render(">", True, (0, 0, 0))
            text_rect = text.get_rect(center=(next_circle_x, circle_height))
            screen.blit(text, text_rect)
            pygame.draw.circle(screen, circle_color, (previous_circle_x,
                               circle_height), circle_radius, circle_width)
            text = font.render("<", True, (0, 0, 0))
            text_rect = text.get_rect(
                center=(previous_circle_x, circle_height))
            screen.blit(text, text_rect)
        
        # Draw the dropdown menu
        for dropdown in dropdowns:
            dropdown.draw(screen, filtros_array)
        
        search_button.draw(screen)
        
        pygame.display.update()


if __name__ == "__main__":
    main()
