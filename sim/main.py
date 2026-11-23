import pygame
import sim

icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)


pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Sim 1")
clock = pygame.time.Clock()

running = True



while running:


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))


    sim.sim(screen, events)


    pygame.display.flip()  # 3. afficher l'image
    clock.tick(60)  # 60 tours de boucle par seconde
pygame.quit()


