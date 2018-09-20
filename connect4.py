import numpy as np
import pygame
import sys
import math
import os

ROW_COUNT = 6
COL_COUNT = 7
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255, 0 , 0)
YELLOW = (255, 255, 0)

def create_board():
  board = np.zeros((ROW_COUNT,COL_COUNT))
  return board

def drop_piece(board, row, col, piece):
  board[row][col] = piece

def is_valid_location(board, col):
  return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
  for r in range(ROW_COUNT):
    if board[r][col] == 0:
      return r

def print_board(board):
  print(np.flip(board, 0))

def animate_move(board, row, col, piece):
  xposition = int(col*SQUARESIZE + SQUARESIZE/2)
  yposition = int(SQUARESIZE/2)
  COLOR = RED
  if piece == 2:
    COLOR = YELLOW
  yspeed = 1
  while yposition < (height-row*SQUARESIZE-SQUARESIZE/2):
    yspeed += .05
    yposition += yspeed
    pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
    draw_board(board)
    pygame.draw.circle(screen, COLOR, (xposition, int(yposition)), RADIUS)
    pygame.display.update()

  return True

def winning_move(board, piece):
  # check horizontal locations
  for c in range(COL_COUNT-3):
    for r in range(ROW_COUNT):
      if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
        return True

  # check vertical
  for c in range(COL_COUNT):
    for r in range(ROW_COUNT-3):
      if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
        return True
  # check for positive slopes
  for c in range(COL_COUNT-3):
    for r in range(ROW_COUNT-3):
      if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
        return True
  # check for negative slopes
  for c in range(COL_COUNT-3):
    for r in range(ROW_COUNT-3, ROW_COUNT):
      if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
        return True

def draw_board(board):
  for c in range(COL_COUNT):
    for r in range(ROW_COUNT):
      pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE ))
      pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
  
  for c in range(COL_COUNT):
    for r in range(ROW_COUNT):
      if board[r][c] == 1:
        pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
      elif board[r][c] == 2:
        pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
  pygame.display.update()

board = create_board()
game_over = False
turn = 0 

pygame.init()

SQUARESIZE = 100

width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont('monospace', 75)

while not game_over:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      os.exit(0)
    
    if event.type == pygame.MOUSEMOTION:
      pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
      posx = event.pos[0]
      if turn == 0:
        pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
      else:
        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
    pygame.display.update()

    if event.type == pygame.MOUSEBUTTONDOWN:
      pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
      # ask for player 1 input
      if turn == 0:
        posx = event.pos[0]
        col = int(math.floor(posx/SQUARESIZE))

        if is_valid_location(board, col):
          row = get_next_open_row(board, col)
          # animate_move(board, row, col, 1)
          drop_piece(board, row, col, 1)
          
          if winning_move(board, 1):
            label = myfont.render('Player 1 wins', 1, RED)
            screen.blit(label, (40, 10))
            game_over = True

      # ask for player 2 input
      else: 
        posx = event.pos[0]
        col = int(math.floor(posx/SQUARESIZE))
        print(col)

        if is_valid_location(board, col):
          row = get_next_open_row(board, col)
          # animate_move(board, row, col, 2)
          drop_piece(board, row, col, 2)
          if winning_move(board, 2):
            label = myfont.render('Player 2 wins', 1, YELLOW)
            screen.blit(label, (40, 10))
            game_over = True
      
      
      print_board(board)  
      draw_board(board)
      turn +=1
      turn = turn % 2

      if game_over:
        pygame.time.wait(3000)
  