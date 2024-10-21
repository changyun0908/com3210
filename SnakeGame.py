import pygame
import time
import random

def message(fonts, msg, color, posx, posy):
    mesg = fonts.render(msg, True, color)
    mesg_Rect = mesg.get_rect()
    mesg_Rect.centerx = posx
    mesg_Rect.centery = posy
    screen.blit(mesg, mesg_Rect)

def message_score(fonts, msg, score, color, posx, posy):
    mesg = fonts.render(msg+score, True, color)
    mesg_Rect = mesg.get_rect()
    mesg_Rect.centerx = posx
    mesg_Rect.centery = posy
    screen.blit(mesg, mesg_Rect)


def food():
    global foodx, foody
    while True:
        foodx = random.randrange(10,DISPLAY_SIZE[0] - SNAKE_SIZE, SNAKE_SIZE)
        foody = random.randrange(10,DISPLAY_SIZE[1] - SNAKE_SIZE, SNAKE_SIZE)
        food_pos = [foodx,foody]

        if food_pos in [snake_pos_x, snake_pos_y]:
            continue
        else:
            break
        
DISPLAY_SIZE = (800,600)

#snake
SNAKE_SIZE = 20
snake_speed = 5
snake_pos_x = DISPLAY_SIZE[0] / 2 - SNAKE_SIZE / 2
snake_pos_y = DISPLAY_SIZE[1] / 2 - SNAKE_SIZE / 2
snake_pos_x_change = 0
snake_pos_y_change = 0

#food
foodx = None
foody = None
score = 0

#color
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
GRAY = (127,127,127)

pygame.init()

#font
font_gameOver = pygame.font.SysFont(None, 50)
font_madeBy = pygame.font.SysFont(None, 20)
font_score = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()
            
screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("SNAKE GAME")

running = True
food()

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_pos_x_change = 0
                snake_pos_y_change = -20
            elif event.key == pygame.K_DOWN:
                snake_pos_x_change = 0
                snake_pos_y_change = +20
            elif event.key == pygame.K_LEFT:
                snake_pos_x_change = -20
                snake_pos_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_pos_x_change = +20
                snake_pos_y_change = 0
    
    snake_pos_x += snake_pos_x_change
    snake_pos_y += snake_pos_y_change
    screen.fill(WHITE)
    message_score(font_score, "score:", str(score), GREEN, 700, 50)
    if foodx == snake_pos_x and foody == snake_pos_y:
        food()
        score += 10
    pygame.draw.rect(screen, BLUE, [foodx, foody, 20, 20])
    pygame.draw.rect(screen, GRAY, [0,0, DISPLAY_SIZE[0], DISPLAY_SIZE[1]],10)
    pygame.draw.rect(screen, RED, [snake_pos_x, snake_pos_y,\
                                   SNAKE_SIZE,SNAKE_SIZE])
    if snake_pos_x >= (DISPLAY_SIZE[0] - SNAKE_SIZE - 5) or \
       snake_pos_x - (SNAKE_SIZE/2) - 5 < 0 or \
       snake_pos_y >= (DISPLAY_SIZE[1] - SNAKE_SIZE - 5) or \
       snake_pos_y - (SNAKE_SIZE/2) - 5 < 0:
        running = False
    pygame.display.update()
    clock.tick(snake_speed)

message(font_gameOver, "Game Over", RED, int(DISPLAY_SIZE[0]/2), int(DISPLAY_SIZE[1]/2))
message(font_madeBy, "made in changyun", GRAY, int(DISPLAY_SIZE[0]/2), int(DISPLAY_SIZE[1]/2) + 30)

pygame.display.update()
time.sleep(2)
pygame.quit()
