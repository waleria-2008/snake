import pygame
import random

pygame.init()
# палитра
white   = (255,255,255)
yellow  = (255,255,102)
black   = (0,0,0)
red     = (213,50,80)
green   = (0,255,0)
blue    = (50,153,213)

# окно
win_width   = 800
win_height  = 600
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption('Змейка')

# переменные и инициализация
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont('Calibri',20)
score_font = pygame.font.SysFont('comicsansms',35)

# функции для работы

def score(scr):
    value = score_font.render('Ваш счет:' + str(scr),True,yellow)
    win.blit(value,[0,0])

def message(msg,color):
    mesg = font_style.render(msg,True,color)
    win.blit(mesg,[win_width/6, win_height/3])

def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(win,black,[x[0],x[1],snake_block,snake_block])

def apple():
    return  round(random.randrange(0,win_width-snake_block)/10) * 10.0 ,\
            round(random.randrange(0,win_height-snake_block)/10) * 10.0

def gameloop():
    game_over = False
    game_close = False
    # координаты появления змейки
    x1 = win_width / 2
    y1 = win_height / 2
    # направление змейки
    x1_change = 0
    y1_change = 0
    # длинна змейки и сама змейка
    length_of_snake = 1
    snake_list = []
    # координаты первого яблока
    foodx,foody = apple()
    while not game_over:
        # обработка проигрыша
        if game_close:
            win.fill(blue)
            message('Вы проиграли! Нажмите Q для выхода или C для повторной игры',red)
            score(length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        # game_close = False
                    if event.key == pygame.K_c:
                        gameloop()
        # обработка управления
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                if event.key == pygame.K_UP:
                    y1_change = snake_block
                if event.key == pygame.K_DOWN:
                    y1_change = -snake_block
        win.fill(blue)
        
        pygame.display.update()
        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameloop()
