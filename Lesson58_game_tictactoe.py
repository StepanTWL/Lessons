import sys
from typing import List, Union
import pygame

def check_win(arr: List[List[int]],sign: str) -> Union[str, bool]:
    zeroes = 0
    for row in arr:
        zeroes+=row.count(0)
        if row.count(sign)==3:
            return sign
    for col in range(3):
        if arr[0][col]==sign and arr[1][col]==sign and arr[2][col]==sign:
            return sign
    if arr[0][0]==sign and arr[1][1]==sign and arr[2][2]==sign:
            return sign
    if arr[0][2]==sign and arr[1][1]==sign and arr[2][0]==sign:
            return sign
    if not zeroes:
        return 'Peace'
    return False
    

pygame.init()

WIDTH = HEIGTH = 100
MARGIN = 15
BLACK=(0, 0, 0)
RED=(255, 0, 0)
WHITE=(255,255,255)
GREEN=(0, 255, 0)
arr = [[0]*3 for i in range(3)]
query = 0
game_over = False
size = (3*WIDTH+4*MARGIN, 3*HEIGTH+4*MARGIN)


screen = pygame.display.set_mode(size)
pygame.display.set_caption('Крестики-нолики')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse//(HEIGTH+MARGIN)
            row = y_mouse//(WIDTH+MARGIN)
            if not arr[row][col]:
                if query%2:
                    arr[row][col]='o'
                else:
                    arr[row][col]='x'
                query+=1
        elif event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
            game_over = False
            arr = [[0]*3 for i in range(3)]
            query=0
            screen.fill(BLACK)


    if not game_over:
        for row in range(3):
            for col in range(3):
                if arr[row][col]=='x':
                    color=RED
                elif arr[row][col]=='o':
                    color=GREEN
                else:
                    color=WHITE
                x = col*HEIGTH + (col+1)*MARGIN
                y = row*WIDTH + (row+1)*MARGIN
                pygame.draw.rect(screen, color, (x, y, WIDTH, HEIGTH))
                if color==RED:
                    pygame.draw.line(screen, WHITE, (x+5, y+5), (x+WIDTH-5, y+HEIGTH-5), 3)
                    pygame.draw.line(screen, WHITE, (x+WIDTH-5, y+5), (x+5, y+HEIGTH-5), 3)
                elif color==GREEN:
                    pygame.draw.circle(screen, WHITE, (x+WIDTH//2,y+HEIGTH//2), WIDTH//2-5, 3)

    if (query-1)%2:
        game_over = check_win(arr, 'o')
    else:
        game_over = check_win(arr, 'x')
    
    if game_over:
        screen.fill(BLACK)
        font=pygame.font.SysFont('stxingkai', 80)
        text1=font.render(game_over, True, WHITE)
        text_rect=text1.get_rect()
        text_x=screen.get_width()//2 - text_rect.width//2
        text_y=screen.get_height()//2 - text_rect.height//2
        screen.blit(text1, [text_x, text_y])
    pygame.display.update()