import pygame
import random

pygame.init()

blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)
eat = (0, 160, 0)
x1 = 300
y1 = 400
clock = pygame.time.Clock()
dis = pygame.display.set_mode((800, 500))
snake = [(x1, y1)]
apple = (random.randrange(0, 790, 10), random.randrange(0, 490, 10))
game_over = False
dirx, diry = 0, 10

score = 0
lenght = 1
frame_counter = 0

x1_change = 0
y1_change = 0
while not game_over:
    frame_counter += 1
    pygame.display.set_caption('Snake2. Score: ' + str(score))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    x1 += x1_change
    y1 += y1_change
    snake.append((x1, y1))
    snake = snake[-lenght - 1:]

    dis.fill(white)
    [pygame.draw.rect(dis, blue, (x1, y1, 10, 10)) for x1, y1 in snake]
    pygame.draw.circle(dis, eat, (apple[0] + 5, apple[1] + 5), 5)
    pygame.display.update()

    if apple[0] == snake[-1][0] and apple[1] == snake[-1][1]:
        apple = (random.randrange(0, 790, 10), random.randrange(0, 490, 10))
        score += 1
        lenght += 1

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x1_change = -10
            y1_change = 0
        elif event.key == pygame.K_RIGHT:
            x1_change = 10
            y1_change = 0
        elif event.key == pygame.K_UP:
            x1_change = 0
            y1_change = -10
        elif event.key == pygame.K_DOWN:
            x1_change = 0
            y1_change = 10

    if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
        game_over = True

    clock.tick(10)
pygame = quit()
quit()
