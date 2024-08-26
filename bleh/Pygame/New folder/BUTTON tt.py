import pygame
import BS

pygame.init()

s_w = 800
s_h = 500

sc = pygame.display.set_mode((s_w,s_h))
pygame.display.set_caption('BUTTON')

#img load up

si = pygame.image.load('start_btn.png').convert_alpha()
ei = pygame.image.load('exit_btn.png').convert_alpha()

#INSTANCES

start_button = BS.Button(100, 200, si, 0.8)
exit_button = BS.Button(450, 200, ei, 0.8)
        

#GAME LOOP
run = True
 
while run:

    sc.fill((202, 228, 241))
    
    if start_button.draw(sc):
        print('Start')
    if exit_button.draw(sc):
        print('Exit')
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()