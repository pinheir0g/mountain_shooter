import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from core.const import WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load("asset/menuBG.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        while True:
            self.window.blit(self.surf, self.rect)
            self.menu_text(50, "Mountain", (255, 128, 0), ((WIN_WIDTH / 2), 70))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Ending Game")
                    pygame.quit()
                    quit()

    def menu_text(self, text_size, text, text_color, text_center_pos):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
