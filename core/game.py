import pygame as pygame

from core.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from core.level import Level
from core.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                leve_return = level.run()
            else:
                pygame.quit()
                quit()
