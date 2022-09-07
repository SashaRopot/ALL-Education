import pygame
import random

size = 30
half_size = size // 2

res = 500
res = res // size // 2 * 2 * size + size
FPS = 25

clock = pygame.time.Clock()
screen = pygame.display.set_mode((res,res))
snake_frame_speed = 5
frame_counter = 0

score = 0
snake_start_pos = res // 2 - half_size
lenght = 1
dirx, diry = 0, size
snake = [(snake_start_pos, snake_start_pos)]
apple = (random.randrange(0,res-size,size), random.randrange(0,res-size,size))

while True:
    frame_counter += 1
    pygame.display.set_caption('Snake2. Score: '+ str(score))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0,0,0))
    [pygame.draw.rect(screen,(0,160,0), (x,y,size,size)) for x, y in snake]
    pygame.draw.circle(screen, (160,0,0), (apple[0] + half_size, apple[1]+half_size), half_size)
    if frame_counter % snake_frame_speed == 0:
        newX = snake[-1][0] + dirx
        newY = snake[-1][1] + diry
        snake.append((newX, newY))
        snake = snake[-lenght-1:]

    if apple[0] == snake[-1][0] and apple[1] == snake[-1][1]:
        apple = (random.randrange(0,res-size,size), random.randrange(0,res-size,size))
        score +=1
        lenght +=1

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dirx, diry = 0, -size
    if key[pygame.K_s]:
        dirx, diry = 0, size
    if key[pygame.K_a]:
        dirx, diry = -size, 0
    if key[pygame.K_d]:
        dirx, diry = size, 0

    if snake[-1][0] <= -size or snake[-1][0] >= res or snake[-1][1] <= -size or snake[-1][1] >= res:
        print('You lose!')
        quit()
    clock.tick(FPS)
    pygame.display.flip()