import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 128)

MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT'
               )

WIN_WIDTH = 576
WIN_HEIGHT = 324

EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'bg0': 0,
                'bg1': 1,
                'bg2': 2,
                'bg3': 3,
                'bg4': 4,
                'bg5': 5,
                'bg6': 6,
                'player1': 4,
                'player2': 4,
                'enemy1': 3,
                }

PLAYER_KEY_UP = {'player1': pygame.K_UP,
                 'player2': pygame.K_w}

PLAYER_KEY_DOWN = {'player1': pygame.K_DOWN,
                   'player2': pygame.K_s}

PLAYER_KEY_LEFT = {'player1': pygame.K_LEFT,
                   'player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'player1': pygame.K_RIGHT,
                    'player2': pygame.K_d}
