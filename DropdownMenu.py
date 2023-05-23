import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
LIGHT_GRAY = (220, 220, 220)


class DropdownMenu:
    def __init__(self, x, y, width, height, items, max_visible_items, titulo:str, indice_filtros_array:int, font = None):
        self.rect = pygame.Rect(x, y, width, height)
        self.items = items
        self.max_visible_items = max_visible_items
        self.is_open = False
        self.selected_item = None
        self.scroll_position = 0
        self.titulo = titulo
        self.indice_filtros_array = indice_filtros_array
        self.font = font if font else pygame.font.Font(None, 28)
        
        if self.titulo != "compania":
            self.titulo += "*"
        else:
            self.titulo = "compañia"

    def handle_event(self, event, filtros_array):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_open = not self.is_open
            elif self.is_open:
                for i, item_rect in enumerate(self.item_rects):
                    if item_rect.collidepoint(event.pos):
                        self.selected_item = self.items[i + self.scroll_position]
                        filtros_array[self.indice_filtros_array] = self.selected_item
                        print(filtros_array)
                        self.is_open = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4 and self.is_open:
            if self.scroll_position > 0:
                self.scroll_position -= 1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5 and self.is_open:
            if self.scroll_position < len(self.items) - self.max_visible_items:
                self.scroll_position += 1

    def draw(self, screen, filtros_array):
        # Draw the main dropdown button
        pygame.draw.rect(screen, GRAY, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

        # Draw the selected item or "Choose" text
        if filtros_array[self.indice_filtros_array]:
            text = self.font.render(filtros_array[self.indice_filtros_array], True, BLACK)
        else:
            text = self.font.render(self.titulo, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

        # Draw the dropdown list
        if self.is_open:
            visible_items = self.items[self.scroll_position : self.scroll_position + self.max_visible_items]
            dropdown_height = self.rect.height * (self.max_visible_items + 1)
            dropdown_rect = pygame.Rect(self.rect.x, self.rect.y + self.rect.height, self.rect.width, dropdown_height)
            pygame.draw.rect(screen, LIGHT_GRAY, dropdown_rect)
            pygame.draw.rect(screen, BLACK, dropdown_rect, 2)

            self.item_rects = []
            for i, item in enumerate(visible_items):
                item_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height + self.rect.height, self.rect.width, self.rect.height)
                pygame.draw.rect(screen, GRAY, item_rect)
                pygame.draw.rect(screen, BLACK, item_rect, 2)
                item_text = self.font.render(item, True, BLACK)
                item_text_rect = item_text.get_rect(center=item_rect.center)
                screen.blit(item_text, item_text_rect)
                self.item_rects.append(item_rect)

            # Draw scrollbar
            scrollbar_x = self.rect.x + self.rect.width - 10
            scrollbar_rect = pygame.Rect(scrollbar_x, self.rect.y + self.rect.height + 1, 10, dropdown_height - 2)
            pygame.draw.rect(screen, GRAY, scrollbar_rect)
            pygame.draw.rect(screen, BLACK, scrollbar_rect, 2)

            # Calculate the scrollbar thumb position and height
            thumb_height = dropdown_height / len(self.items) * self.max_visible_items
            thumb_position = dropdown_rect.y + (self.scroll_position / len(self.items)) * (dropdown_height - thumb_height)
            thumb_rect = pygame.Rect(scrollbar_x + 2, thumb_position, 6, thumb_height)
            pygame.draw.rect(screen, BLACK, thumb_rect)
