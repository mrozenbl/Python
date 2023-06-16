import pygame
import time
import random

# Constants
WIDTH = 800
HEIGHT = 600
SNAKE_SIZE = 20
APPLE_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake module
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WIDTH / 2, HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x * SNAKE_SIZE)) % WIDTH, (cur[1] + (y * SNAKE_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def render(self):
        for p in self.positions:
            pygame.draw.rect(screen, self.color, (p[0], p[1], SNAKE_SIZE, SNAKE_SIZE))

    def reset(self):
        self.length = 1
        self.positions = [(WIDTH / 2, HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

# Apple module
class Apple:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.spawn()

    def spawn(self):
        self.position = (
            random.randint(0, (WIDTH - APPLE_SIZE) // APPLE_SIZE) * APPLE_SIZE,
            random.randint(0, (HEIGHT - APPLE_SIZE) // APPLE_SIZE) * APPLE_SIZE,
        )

    def render(self):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], APPLE_SIZE, APPLE_SIZE))

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game initialization
def game_init():
    snake = Snake()
    apple = Apple()

    return snake, apple

# Game over screen
def show_game_over():
    font = pygame.font.SysFont(None, 70)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.flip()
    time.sleep(2)

# Game loop
def game_loop():
    snake, apple = game_init()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT

        snake.update()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.spawn()

        screen.fill(BLACK)
        snake.render()
        apple.render()

        pygame.display.flip()
        clock.tick(FPS)

    show_game_over()
    pygame.quit()

# Start the game
if __name__ == "__main__":
    game_loop()
