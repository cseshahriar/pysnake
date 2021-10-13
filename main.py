import time
import pygame
from pygame.locals import *

SIZE = 40


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()


class Snake:
    """ snake """

    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'

    def draw(self):
        self.parent_screen.fill((110, 110, 5))  # clear the state
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'

    def mode_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def mode_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= SIZE

        if self.direction == 'down':
            self.y[0] += SIZE

        if self.direction == 'left':
            self.x[0] -= SIZE

        if self.direction == 'right':
            self.x[0] += SIZE

        self.draw()


class Game:
    """ game class """

    def __init__(self):
        pygame.init()  # py game initialize
        self.surface = pygame.display.set_mode((800, 600))
        self.surface.fill((110, 110, 5))  # go rgb color picker
        # snake init
        self.snake = Snake(self.surface, 6)
        self.snake.draw()
        # apple init
        self.apple = Apple(self.surface)
        self.apple.draw()

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

            # timer
            self.snake.walk()
            self.apple.draw()
            time.sleep(0.3)


if __name__ == "__main__":
    game = Game()
    game.run()

