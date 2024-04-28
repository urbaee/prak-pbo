# Rahmat Aldi Nasda
# 122140077
# RB
# X and O game

import pygame
import sys
from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def draw_symbols(self):
        pass

    @abstractmethod
    def draw_result(self):
        pass

    @abstractmethod
    def winner_check(self):
        pass

    @abstractmethod
    def gameplay(self):
        pass

class XandO(Game):
    def __init__(self):
        self.board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.turn = 'X'
        self.winner = None

    def draw_symbols(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == 'X':
                    pygame.draw.line(self.screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE * 0.1, row * SQUARE_SIZE + SQUARE_SIZE * 0.1),
                                     (col * SQUARE_SIZE + SQUARE_SIZE * 0.9, row * SQUARE_SIZE + SQUARE_SIZE * 0.9), 5)
                    pygame.draw.line(self.screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE * 0.9, row * SQUARE_SIZE + SQUARE_SIZE * 0.1),
                                     (col * SQUARE_SIZE + SQUARE_SIZE * 0.1, row * SQUARE_SIZE + SQUARE_SIZE * 0.9), 5)
                elif self.board[row][col] == 'O':
                    pygame.draw.circle(self.screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5, 2)

    def draw_result(self):
        if self.winner:
            result = f"Pemain {self.winner} menang!"
        elif all(all(cell != '' for cell in row) for row in self.board):
            result = "Permainan seri!"
        else:
            result = ""        
        
        text = CUSTOM_FONT2.render(result, True, "#2a3cb0")
        self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    def winner_check(self):
        for row in range(BOARD_ROWS):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != '':
                self.winner = self.board[row][0]
        for col in range(BOARD_COLS):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                self.winner = self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            self.winner = self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            self.winner = self.board[0][2]

    def gameplay(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not self.winner:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if self.board[clicked_row][clicked_col] == '':
                    self.board[clicked_row][clicked_col] = self.turn

                    if self.turn == 'X':
                        self.turn = 'O'
                    else:
                        self.turn = 'X'

                    self.winner_check()

            if event.type == pygame.MOUSEBUTTONDOWN and self.restart_button.collidepoint(event.pos):
                self.board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
                self.winner = None
                self.turn = 'X'

class XandODisplay(XandO):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("X and O")
        self.restart_button = pygame.Rect(0, HEIGHT - 50, WIDTH, 50)
        
    def draw_lines(self):
        pygame.draw.line(self.screen, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, BLACK, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT - 50), LINE_WIDTH)
        pygame.draw.line(self.screen, BLACK, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT - 50), LINE_WIDTH)

    def restart_game(self):
        self.board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.winner = None
        self.turn = 'X'

    def main(self):
        while True:
            self.screen.fill("#e0f500")

            self.draw_lines()
            self.draw_symbols()

            pygame.draw.rect(self.screen, WHITE, self.restart_button)
            restart_text = CUSTOM_FONT.render("Restart", True, BLACK)
            self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT - 35))

            self.gameplay()

            self.draw_result()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and self.restart_button.collidepoint(event.pos):
                    self.restart_game()

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

WIDTH, HEIGHT = 500, 550
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

FONT = pygame.font.SysFont("Pixelfont.ttf", 40)

CUSTOM_FONT = pygame.font.Font("Pixelfont.ttf", 30)
CUSTOM_FONT2 = pygame.font.Font("Pixelfont.ttf", 50)

game = XandODisplay()
game.main()
