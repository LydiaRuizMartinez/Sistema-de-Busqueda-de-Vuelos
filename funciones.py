import pygame

def mostrar_texto_medio(screen, texto:str) -> None:
    font = pygame.font.Font(None, 35)
    text = font.render(texto, True, (255,255,255))
    text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.fill((0,0,0))
    screen.blit(text, text_rect)
    pygame.display.update()
