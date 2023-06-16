import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 6
BOARD_SIZE = 3
CELL_SIZE = WIDTH // BOARD_SIZE
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 255, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Game board
board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Function to draw the grid lines
def draw_lines():
    pygame.draw.line(window, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(window, LINE_COLOR, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(window, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(window, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw X's and O's on the board
def draw_symbols():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = col * CELL_SIZE + CELL_SIZE // 2
            y = row * CELL_SIZE + CELL_SIZE // 2

            if board[row][col] == 'X':
                pygame.draw.line(window, X_COLOR, (x - 30, y - 30), (x + 30, y + 30), LINE_WIDTH)
                pygame.draw.line(window, X_COLOR, (x + 30, y - 30), (x - 30, y + 30), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(window, O_COLOR, (x, y), 30, LINE_WIDTH)

# Function to check if a player has won
def check_winner(player):
    # Check rows and columns
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)):
            return True
        if all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)):
        return True

    return False

# Main game loop
def game_loop(current_player):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    col = x // CELL_SIZE
                    row = y // CELL_SIZE
                    if board[row][col] == ' ':
                        board[row][col] = current_player
                        if check_winner(current_player):
                            print("Player", current_player, "wins!")
                            pygame.time.wait(2000)
                            pygame.quit()
                            sys.exit()
                        elif all(board[i][j] != ' ' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
                            print("It's a draw!")
                            pygame.time.wait(2000)
                            pygame.quit()
                            sys.exit()
                        current_player = 'O' if current_player == 'X' else 'X'

        window.fill(BG_COLOR)
        draw_lines()
        draw_symbols()
        pygame.display.update()

# Start the game
game_loop('X')  # Pass the initial current_player value as a parameter
