import pygame
import time
import random

def food():
    global foodx, foody
    while True:
        foodx = random.randrange(10, DISPLAY_SIZE[0] - SNAKE_SIZE, SNAKE_SIZE)
        foody = random.randrange(10, DISPLAY_SIZE[1] - SNAKE_SIZE, SNAKE_SIZE)
        food_pos = [foodx, foody]
        if food_pos in snake_list:  # 사과가 지렁이 몸에 겹치지 않도록
            continue
        else:
            break

def message(fonts, msg, color, posx, posy):
    mesg = fonts.render(msg, True, color)
    mesg_Rect = mesg.get_rect()
    mesg_Rect.centerx = posx
    mesg_Rect.centery = posy
    screen.blit(mesg, mesg_Rect)

# food
foodx = None
foody = None

DISPLAY_SIZE = (800, 600)

# snake
snake_tail = 1
SNAKE_SIZE = 20
snake_pos_x = DISPLAY_SIZE[0] // 2 - SNAKE_SIZE // 2
snake_pos_y = DISPLAY_SIZE[1] // 2 - SNAKE_SIZE // 2
snake_pos_x_change = 0
snake_pos_y_change = 0
snake_list = []
snake_speed = 10
score = 0

def snake(SNAKE_SIZE, snake_list):
    for pos in snake_list:
        pygame.draw.rect(screen, RED, [pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE])

# color
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

pygame.init()
# fonts
font_gameOver = pygame.font.SysFont(None, 50)
font_madeBy = pygame.font.SysFont(None, 20)
font_score = pygame.font.SysFont(None, 30)
font_Restart = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("SNAKE GAME ver 0.1")
food()  # 초기 사과 생성

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_pos_y_change != SNAKE_SIZE:
                snake_pos_x_change = 0
                snake_pos_y_change = -SNAKE_SIZE
            elif event.key == pygame.K_DOWN and snake_pos_y_change != -SNAKE_SIZE:
                snake_pos_x_change = 0
                snake_pos_y_change = SNAKE_SIZE
            elif event.key == pygame.K_LEFT and snake_pos_x_change != SNAKE_SIZE:
                snake_pos_x_change = -SNAKE_SIZE
                snake_pos_y_change = 0
            elif event.key == pygame.K_RIGHT and snake_pos_x_change != -SNAKE_SIZE:
                snake_pos_x_change = SNAKE_SIZE
                snake_pos_y_change = 0

    snake_pos_x += snake_pos_x_change
    snake_pos_y += snake_pos_y_change
    snake_head = [snake_pos_x, snake_pos_y]
    
    if len(snake_list) > 0 and snake_head in snake_list[:-1]:  # 자기 몸에 부딪히는 조건 추가
        running = False

    snake_list.append(snake_head)

    if len(snake_list) > snake_tail:
        del snake_list[0]

    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, [0, 0, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], 10)
    snake(SNAKE_SIZE, snake_list)

    pygame.draw.rect(screen, BLUE, [foodx, foody, SNAKE_SIZE, SNAKE_SIZE])
    message(font_score, "Score : " + str(score), GREEN, DISPLAY_SIZE[0] / 2, 30)

    if snake_pos_x >= (DISPLAY_SIZE[0] - SNAKE_SIZE) or \
       snake_pos_x < 0 or \
       snake_pos_y >= (DISPLAY_SIZE[1] - SNAKE_SIZE) or \
       snake_pos_y < 0:
        running = False

    if snake_pos_x == foodx and snake_pos_y == foody:
        snake_speed += 1
        score += 10
        snake_tail += 1
        food()  # 새 사과 생성

    pygame.display.update()
    clock.tick(snake_speed)

message(font_gameOver, 'Game Over', RED, int(DISPLAY_SIZE[0] / 2), int(DISPLAY_SIZE[1] / 2))
message(font_madeBy, 'made by changyun', GRAY, int(DISPLAY_SIZE[0] / 2), int(DISPLAY_SIZE[1] / 2) + 30)

pygame.display.update()
time.sleep(5)
pygame.quit()
