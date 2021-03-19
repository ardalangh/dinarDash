import pygame 


pygame.init()







size = (700, 500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dinar Dash")






running = True 

clock - pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False

    







    pygame.display.flip()
    clock.tick(60)
    