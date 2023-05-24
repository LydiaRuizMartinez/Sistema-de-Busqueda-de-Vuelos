import pygame


def mostrar_texto_medio(screen, texto: str) -> None:
    font = pygame.font.Font(None, 35)
    screen.fill((0, 0, 0))
    imprimir_mensaje(screen, texto, font, (255, 255, 255))
    pygame.display.update()


def imprimir_mensaje(screen, mensaje, font, color):
    text_width, text_height = font.size("txt")

    text = font.render(mensaje, True, (0, 0, 0))
    text_rect = text.get_rect(
        center=(screen.get_width()/2 + 1, screen.get_height()/2 + 1))
    screen.blit(text, text_rect)

    text = font.render(mensaje, True, color)
    text_rect = text.get_rect(
        center=(screen.get_width()/2, screen.get_height()/2))
    screen.blit(text, text_rect)
