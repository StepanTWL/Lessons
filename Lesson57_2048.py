import sys
import pygame

pygame.init()

size = (510, 510)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game field')

WIGTH = HEIGTH = 40
MARGIN = 10
RED=(255, 0, 0)
WHITE=(255,255,255)
arr = [[0]*10 for i in range(10)]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            column = x_mouse//(WIGTH + MARGIN)
            row = y_mouse//(HEIGTH + MARGIN)
            arr[row][column] ^=1
    for row in range(10):
        for col in range(10):
            if arr[row][col]:
                color = RED
            else:
                color = WHITE
            pygame.draw.rect(screen, color, (col*WIGTH+MARGIN*(col+1), row*HEIGTH+MARGIN*(row+1), WIGTH, HEIGTH))
    pygame.display.update()