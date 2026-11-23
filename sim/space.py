#import pygame
import object
from gravite_centre import get_g_from_xy

class space:
    def __init__(self, fps, speed, const_G = 2, g_ref_t = (0.0, -9.81)):
        self.fps = fps
        self.speed = speed
        self.const_gravitation = const_G
        self.objs = []
        self.astres = []
        self.gravitation_terrestre = g_ref_t

    def set_obj(self, xy, m, v = (0, 0), z = 1, r=5, forces_add = None, color=None):

        if forces_add == None:
            forces_add = []
        forces = [self.gravitation_terrestre] + forces_add
        obj = object.objet(xy, m, forces, self.fps, self.speed, v, z, r, color)
        self.objs.append(obj)

    def clear_objs(self):
        self.objs = []

    def set_astre(self, xy, masse, r = 10, c = None):
        astre = object.astre(xy, masse, r, c)
        self.astres.append(astre)

    def clear_astres(self):
        self.astres = []

    def show_stat_obj(self, obj):
        if type(obj) == type(1):
            obj = self.objs[obj]
            print("Vxy:(", obj.vx, obj.vy, ") forces:(", obj.f, ") xy:(", obj.x, obj.y, ") dist:(", "r", ")")

        else:
            if obj not in self.objs:
                print("objet non répertorié")
            else:
                for i in self.objs:
                    if i == obj:
                        print("Vxy:(", obj.vx, obj.vy, ") forces:(", obj.f, ") xy:(", obj.x, obj.y, ") dist:(", "r", ")")

    def clear_all(self):
        self.clear_objs()
        self.clear_astres()

    def update_all(self, screen, is_spatial, fps = None, speed = None, forces_add = None):
        if forces_add == None:
            forces_add = []

        if speed == None:
            speed = self.speed
        self.speed = speed

        if fps == None:
            fps = self.fps
        self.fps = fps

        if is_spatial:
            for astre in self.astres:
                astre.update(screen)

        for obj in self.objs:
            if is_spatial:
                grav = []
                for astre in self.astres:
                    g, r = get_g_from_xy([obj.x, obj.y], obj.masse, [astre.x, astre.y], astre.m, self.const_gravitation)

                    if r < obj.radius + astre.radius:
                        obj.vy, obj.vx = 0, 0
                        grav = [(-g[0], -g[1])]

                        break

                    elif r == obj.radius + astre.radius:
                        obj.vx, obj.vy = 0, 0
                        grav = [(0, 0)]
                        break

                    else:
                        grav += [(g[0], g[1])]
                obj.update(screen, grav + forces_add, self.fps, self.speed)

            else:
                obj.update(screen, [self.gravitation_terrestre] + forces_add, self.fps, self.speed)