import pygame
from pygame.locals import *


class Snake:
    """ snake """

    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_screen.fill((110, 110, 5))  # clear the state
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def move_left(self):
        self.x -= 10
        self.draw()

    def mode_right(self):
        self.x += 10
        self.draw()

    def move_up(self):
        self.y -= 10
        self.draw()

    def mode_down(self):
        self.y += 10
        self.draw()


class Game:
    """ game class """

    def __init__(self):
        pygame.init()  # py game initialize
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((110, 110, 5))  # go rgb color picker
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.mode_down()

                    if event.key == K_RIGHT:
                        self.snake.mode_right()

                elif event.type == QUIT:
                    running = False  # exit


if __name__ == "__main__":
    game = Game()
    game.run()

