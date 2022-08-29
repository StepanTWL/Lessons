import pygame
pygame.init()#инициолизация экрана
size = (600,400)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('My prog')
img=pygame.image.load('tel.jpg')
pygame.display.set_icon(img)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
font = pygame.font.SysFont('arial', 32)
follow = font.render('Тук-тук, кто там? Это я дерево!!!', 1, RED, GREEN)
x, y = 110, 170
FPS=60
direct_x = 2
direct_y = 1

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    clock.tick(FPS)
    screen.fill(BLACK)
    screen.blit(follow, (x,y))#прекрепление к экрану
    x += direct_x
    if x+follow.get_width() >= 600 or x <= 0:
        direct_x = -direct_x
    y += direct_y
    if y+follow.get_height() >= 400 or y <= 0:
        direct_y = -direct_y

    pygame.display.update()#что бы надпись отобразилась