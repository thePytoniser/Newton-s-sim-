import pygame
import space
import centre_de_control_event
import initialise
import conversion_grille

banner = pygame.image.load('assets/banner.png')

button_menu = pygame.image.load('assets/button_main_menu.png')
button_menu = pygame.transform.scale(button_menu, (450, 75))

control_msg = pygame.image.load('assets/controles_msg.png')
control_msg = pygame.transform.scale(control_msg, (500, 200))

icon_spatial = pygame.image.load('assets/spatial_icon.png')

icon_geo = pygame.image.load('assets/geo_icone.png')

space = space.space(initialise.values.current_fps, initialise.values.current_speed, initialise.values.G, initialise.values.g)
def sim(screen, events):
    if initialise.values.sim_state == "menu":
        screen.blit(banner, conversion_grille.convert_xy_physique_to_xy_numerique((-300,200)))
        screen.blit(button_menu, conversion_grille.convert_xy_physique_to_xy_numerique((-225,0)))
    elif initialise.values.sim_state == "controls":
        screen.blit(control_msg, conversion_grille.convert_xy_physique_to_xy_numerique((-250, 200)))
        screen.blit(icon_spatial, conversion_grille.convert_xy_physique_to_xy_numerique((-200, 0)))
        screen.blit(icon_geo, conversion_grille.convert_xy_physique_to_xy_numerique((0, 0)))
    else:
        #space.show_stat_obj(0)
        space.update_all(screen, initialise.values.is_spatial, initialise.values.current_fps, initialise.values.current_speed)
    centre_de_control_event.event_r_and_w(screen, events, space)
