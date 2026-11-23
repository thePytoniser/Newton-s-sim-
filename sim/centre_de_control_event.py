import pygame
import initialise
import conversion_grille
import mouse_tracker

pos_depart = None
f_v = 0.05
if not initialise.values.is_spatial:
    f_v = 0.1

key_pressed = []

def event_r_and_w(screen, events, space):
    global pos_depart
    global f_v
    global key_pressed




    mouse_pos = conversion_grille.convert_xy_numerique_to_xy_physique(pygame.mouse.get_pos())
    for event in events:

        if event.type == pygame.MOUSEBUTTONDOWN:
            if initialise.values.sim_state == "menu":
                if event.button == 1 and mouse_tracker.is_mouse_in(mouse_pos, (-225, 0), (75, 450)):
                    initialise.values.change_sim_state((1, 0))

            elif initialise.values.sim_state == "controls":
                if event.button == 1:
                    if mouse_tracker.is_mouse_in(mouse_pos, (-200, 0), (200, 200)):
                        initialise.values.change_sim_state((2, 0))
                    if mouse_tracker.is_mouse_in(mouse_pos, (0, 0), (200, 200)):
                        initialise.values.change_sim_state((2, 1))

            else:
                if event.button == 1:
                    pos_depart = mouse_pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and pos_depart != None:
                pos_fin = mouse_pos

                vx = (pos_depart[0] - pos_fin[0]) * f_v
                vy = ((pos_depart[1] - pos_fin[1]) * f_v)

                space.set_obj(pos_depart, 100, (vx, vy), 5)

                pos_depart = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o and "o" not in key_pressed:
                key_pressed.append("o")
                space.set_obj(mouse_pos, 100, (0, 0), r=5)
            if event.key == pygame.K_a and "a" not in key_pressed:
                key_pressed.append("a")
            if event.key == pygame.K_r and "r" not in key_pressed:
                key_pressed.append("r")

            if event.key == pygame.K_KP_PLUS:
                initialise.values.change_speed(1)

            if event.key == pygame.K_KP_MINUS:
                initialise.values.change_speed(-1)

            if event.key == pygame.K_TAB:
                initialise.values.trigger_spatial()
                space.clear_all()

            if event.key == pygame.K_ESCAPE:
                initialise.values.change_sim_state((0,0))

            if event.key == pygame.K_SPACE:
                initialise.values.trigger_pause()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_o and "o" in key_pressed:
                key_pressed.remove("o")
            if event.key == pygame.K_a and "a" in key_pressed:
                key_pressed.remove("a")
            if event.key == pygame.K_r:
                key_pressed.clear()

        if event.type == initialise.SIM_EVENT:
            space.clear_all()
            if event.action == "initialise geo":
                space.set_obj((-100, 0), 100, (50, 50))
            if event.action == "initialise spatial":
                space.set_astre((0, 0), 5000)
                space.set_obj((100, 0), 100, (0, 10))


    if pos_depart != None:
        pygame.draw.line(screen, "white", conversion_grille.convert_xy_physique_to_xy_numerique(pos_depart), conversion_grille.convert_xy_physique_to_xy_numerique(mouse_pos))

    if "o" in key_pressed and "r" in key_pressed:
        space.clear_objs()
    elif "a" in key_pressed and "r" in key_pressed:
        space.clear_astres()
    elif "a" in key_pressed:
        space.set_astre(mouse_pos, 5000, 10)
    elif "r" in key_pressed:
        space.clear_all()
