import pygame

SIM_EVENT = pygame.event.custom_type()

class values:
    def __init__(self):
        self.sim_state = "menu"
        self.is_paused = False
        self.is_spatial = False
        self.g = (0, -9.81) # g est le poids quand la simulation est en mode référenciel terrestre
        self.G = 2          # G est la constante de gravitation quand la simulation est en mode référenciel géocentrique
        self.speed = 2      # speed est la vitesse de la simulation elle n'est pas censer aller en dessous de 0
        self.fps = 60       # !!! fps > 0 !!! fps signifie frame par seconde, la modifier reviendrait à avoir une simulation plus ou moins fluide mais plus elle est élevée, plus la simulation demande des ressources
        self.current_fps = self.fps
        self.current_speed = self.speed

    def change_sim_state(self, state):
        state_types = [["menu"], ["controls"], ["spatial", "geo"]]
        self.sim_state = state_types[state[0]][state[1]]
        print(f"sim state has change to {self.sim_state}")

        if self.sim_state == "geo" and self.is_spatial or self.sim_state == "spatial" and not self.is_spatial:
            self.trigger_spatial()


        if self.is_spatial:

            pygame.event.post(pygame.event.Event(SIM_EVENT, {"action" : "initialise spatial"}))

        if not self.is_spatial:

            pygame.event.post(pygame.event.Event(SIM_EVENT, {"action": "initialise geo"}))



    def trigger_pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.current_fps = 0
            self.current_speed = 0
        else:
            self.current_fps = self.fps
            self.current_speed = self.speed

    def trigger_spatial(self):
        self.is_spatial = not self.is_spatial

        if self.sim_state != "spatial" and self.is_spatial:
            self.change_sim_state((2, 0))
        elif self.sim_state != "geo" and not self.is_spatial:
            self.change_sim_state((2, 1))

    def change_speed(self, value):
        self.current_speed = self.current_speed + value

values = values()