import pygame
import socket
import threading

# Constants
WIDTH = 700
HEIGHT = 600
BOARD_ROWS = 6
BOARD_COLS = 7
SQUARE_SIZE = 100
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5050))

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")

# Function to draw the game board
def draw_board(board):
    for c in range(BOARD_COLS):
        for r in range(BOARD_ROWS):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, WHITE, (c * SQUARE_SIZE + SQUARE_SIZE // 2, r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE // 2), 45)

    for c in range(BOARD_COLS):
        for r in range(BOARD_ROWS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - r * SQUARE_SIZE - SQUARE_SIZE // 2), 45)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - r * SQUARE_SIZE - SQUARE_SIZE // 2), 45)
    pygame.display.update()

# Function to handle player input
def handle_input():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos = event.pos[0]
                col = x_pos // SQUARE_SIZE
                client.send(str(col).encode())

# Function to receive game state updates from server
def receive_updates():
    while True:
        data = client.recv(1024).decode()
        if data == "START":
            print("Game started.")
        elif data == "WIN":
            print("You win!")
        else:
            # Parse game state and draw the board
            board = [list(map(int, row.split())) for row in data.split("\n") if row.strip()]
            draw_board(board)

# Start threads for handling input and receiving updates
input_thread = threading.Thread(target=handle_input)
input_thread.daemon = True
input_thread.start()

update_thread = threading.Thread(target=receive_updates)
update_thread.daemon = True
update_thread.start()

# Main game loop
while True:
    pass  # Keep the program running until exited