import sys
import pygame
from .setting import Settings

class AlienInvasion:
    "starting the main game"
    pygame.get_init()

    def __init__(self):
        self.settings=Settings

        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")





    def run_game(self):
        "this runs the game and updates display"
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #accessing to the corect function for color background
            self.screen.fill(self.settings.screen_color)

            pygame.display.flip()
if __name__=="__main__":
    ai=AlienInvasion()
    ai.run_game()

