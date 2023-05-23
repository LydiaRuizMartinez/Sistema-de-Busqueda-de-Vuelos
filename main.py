from Arbol import Arbol
from leer_datos import leer_datos
import pygame
from DropdownMenu import DropdownMenu
from SearchButton import SearchButton


if __name__ == "__main__":
    fichero:str = "Cleaned_2018_Flights.csv"
    caracteristicas:list[str] = ["origen", "destino", "trimestre", "compania"]
    arbol:Arbol = Arbol(caracteristicas)
    dict_opciones_por_caracteristica:dict = leer_datos(fichero, arbol, caracteristicas)

    pygame.init()

    # Display
    ancho = 1050
    alto = 700
    screen = pygame.display.set_mode((ancho, alto))
    # DropdownMenu(x, y, width, height, items, max_visible_items)
    button_width = 225
    button_height = 50
    button_y = 10
    dropdowns = []
    # dropdowns = [DropdownMenu(items = dict_opciones_por_caracteristica[caracteristicas[i]], indice_filtros_array = i, titulo = caracteristicas[i], x = 1 + 200*i, y = button_y, width = button_width, height = button_height, max_visible_items = 8) for i in range(len(caracteristicas))]
    for i in range(len(caracteristicas)):
        dropdowns.append(DropdownMenu(items = dict_opciones_por_caracteristica[caracteristicas[i]], indice_filtros_array = i, titulo = caracteristicas[i], x = 1 + 200*i, y = button_y, width = button_width, height = button_height, max_visible_items = 8))
    search_button = SearchButton(x = 1 + 200*len(caracteristicas), y = button_y, width = button_width, height = button_height)

    running = True

    left = 60


    circle_radius = 50
    circle_color = (255, 255, 255)
    circle_width = 0  # 0 width means a solid circle
    circle_height = 550
    # (x - 500)**2 + (y - height)
    previous_circle_x = 140
    next_circle_x = ancho - previous_circle_x
    pause_circle_x = ancho/2
    pygame.draw.circle(screen, circle_color, (next_circle_x,circle_height), circle_radius, circle_width)
    pygame.draw.circle(screen, circle_color, (previous_circle_x,circle_height), circle_radius, circle_width)
    pygame.draw.circle(screen, circle_color, (pause_circle_x,circle_height), circle_radius, circle_width)

    filtros_array = [None for _ in range(len(caracteristicas))]
 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
                    
                elif event.key == pygame.K_RIGHT:
                    pass
                    #Aqui va el código de avanzar 
                elif event.key == pygame.K_LEFT:
                    pass
                    
                    #Aqui va el código de volver a la anterior
                elif event.key == pygame.K_SPACE:
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = event.pos
                if (click_pos[0] - next_circle_x) ** 2 + (click_pos[1] - circle_height) ** 2 <= circle_radius**2:
                    pass
                elif (click_pos[0] - previous_circle_x) ** 2 + (click_pos[1] - circle_height) ** 2 <= circle_radius**2:
                    pass
                elif (click_pos[0] - pause_circle_x) ** 2 + (click_pos[1] - circle_height) ** 2 <= circle_radius**2:
                    pass
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            for dropdown in dropdowns:
                dropdown.handle_event(event, filtros_array)
            lista_busqueda = search_button.handle_event(event,arbol,filtros_array)
            if lista_busqueda:
                
                print(lista_busqueda)

        # Clear the screen
        screen.fill((0,0,0))

        # Draw the dropdown menu
        for dropdown in dropdowns:
            dropdown.draw(screen, filtros_array)
        
        search_button.draw(screen)

    
        pygame.display.update()
