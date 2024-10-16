import pygame

DISPLAY_SIZE = (800,600)
SNAKE_SIZE = 20
snake_pos_x = DISPLAY_SIZE[0] / 2 - SNAKE_SIZE / 2
snake_pos_y = DISPLAY_SIZE[1] / 2 - SNAKE_SIZE / 2
snake_pos_x_change = 0
snake_pos_y_change = 0
#color
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

pygame.init()
clock = pygame.time.Clock()
            
screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("SNAKE GAME")

running = True
while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_pos_x_change = 0
                snake_pos_y_change = -10
            elif event.key == pygame.K_DOWN:
                snake_pos_x_change = 0
                snake_pos_y_change = +10
            elif event.key == pygame.K_LEFT:
                snake_pos_x_change = -10
                snake_pos_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_pos_x_change = +10
                snake_pos_y_change = 0
    
    snake_pos_x += snake_pos_x_change
    snake_pos_y += snake_pos_y_change
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [snake_pos_x, snake_pos_y,\
                                   SNAKE_SIZE,SNAKE_SIZE])
    pygame.display.update()
    clock.tick(60)
pygame.quit()
