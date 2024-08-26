import pygame
pygame.init()

s_w = 1200
s_h = 650
screen = pygame.display.set_mode((s_w, s_h))

player = pygame.Rect(240,200,25,25)

run = True 
while run:

    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255,0,255), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
