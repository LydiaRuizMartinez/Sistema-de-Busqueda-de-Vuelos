from Arbol import Arbol
from leer_datos import leer_datos
import pygame
import sys


if __name__ == "__main__":
    fichero = "Cleaned_2018_Flights.csv"
    arbol:Arbol = Arbol(["origen", "destino", "trimestre", "compania"])
    leer_datos(fichero, arbol)

    pygame.init()

    # Display
    ancho = 640
    alto = 700
    screen = pygame.display.set_mode((ancho, alto))

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
                sys.quit()
                running = False

    
        pygame.display.update()