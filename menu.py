# menu.py
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
LIGHT_GRAY = (170, 170, 170)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 50)

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        color = LIGHT_GRAY if self.rect.collidepoint(mouse_pos) else GRAY
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 3)
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos)

def show_difficulty_menu(screen):
    # Buttons
    button_width = 200
    button_height = 60
    button_y_start = HEIGHT // 2 - 100
    button_spacing = 80

    easy_button = Button("Easy", WIDTH//2 - button_width//2, button_y_start, button_width, button_height)
    medium_button = Button("Medium", WIDTH//2 - button_width//2, button_y_start + button_spacing, button_width, button_height)
    hard_button = Button("Hard", WIDTH//2 - button_width//2, button_y_start + button_spacing*2, button_width, button_height)

    selected_difficulty = None
    while selected_difficulty is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if easy_button.is_clicked(event):
                selected_difficulty = "easy"
            elif medium_button.is_clicked(event):
                selected_difficulty = "medium"
            elif hard_button.is_clicked(event):
                selected_difficulty = "hard"

        # Draw
        screen.fill(WHITE)
        title = font.render("Select Difficulty", True, BLACK)
        title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//2 - 180))
        screen.blit(title, title_rect)

        easy_button.draw(screen)
        medium_button.draw(screen)
        hard_button.draw(screen)

        pygame.display.flip()

    return selected_difficulty
