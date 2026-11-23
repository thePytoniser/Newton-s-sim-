import pygame
import conversion_grille
class objet:
    def __init__(self,xy, m,forces, fps, speed, v = (0, 0),z = 1, r = 10, c = None):
        if c == None:
            c = "white"

        if v == None:
            v = (0, 0)

        self.zoom = z
        self.masse = m
        self.color = c
        self.x = xy[0]
        self.y = xy[1]
        self.vx = v[0]
        self.vy = v[1]
        self.__scale_v()
        self.f = forces
        self.__f_to_a()
        self.radius = r
        self.fps = fps
        self.speed = speed

    def update(self,screen, forces = None, fps = None, speed = None, zoom = None):
        if zoom == None:
            zoom = self.zoom
        self.zoom = zoom

        if speed == None:
            speed = self.speed
        self.speed = speed

        if fps == None:
            fps = self.fps
        self.fps = fps

        if forces == None:
            forces = self.f
        self.f = forces

        self.__f_to_a()
        self.__v_from_a_nfps(speed, fps)
        self.__scale_v()
        self.__move_nfps(speed, fps)
        self.__tp_xy_in_frame()
        self.__show(screen)

    def __show(self, screen):
        xy = conversion_grille.convert_xy_physique_to_xy_numerique((self.x, self.y))
        pygame.draw.circle(screen, self.color, (xy[0], xy[1]), self.radius)

    def __get_somme_forces(self):
        fx = 0
        fy = 0
        for i in self.f:
            fx += i[0]
            fy += i[1]
        return fx, fy

    def __f_to_a(self):
        ax, ay = self.__get_somme_forces()
        self.ax = ax
        self.ay = ay

    def __v_from_a_nfps(self, speed, n = 60):
        if n == 0 or speed == 0:
            return 0
        self.vx += self.ax / (n / speed)
        self.vy += self.ay / (n / speed)


    def __scale_v(self):
        self.vx_s = self.vx * self.zoom
        self.vy_s = self.vy * self.zoom

    def __tp_xy_in_frame(self):

        xy, hw = conversion_grille.convert_xy_physique_to_xy_numerique((self.x, self.y), True)

        if xy[0] > hw[1]:
            x = xy[0] % hw[1]

        elif xy[0] < 0:
            x = xy[0] % hw[1]

        else:
            x = xy[0]

        if xy[1] > hw[0]:
            y = xy[1] % hw[0]

        elif xy[1] < 0 :
            y = xy[1] % hw[0]

        else:
            y = xy[1]

        self.x, self.y = conversion_grille.convert_xy_numerique_to_xy_physique((x, y))


    def __move_nfps(self, speed, n = 60):
        if n == 0 or speed == 0:
            return 0
        self.x += self.vx_s / (n / speed)
        self.y += self.vy_s / (n / speed)

class astre:
    def __init__(self, xy, masse, r = 10, c = None):
        if c == None:
            c = "red"
        self.x = xy[0]
        self.y = xy[1]
        self.m = masse
        self.radius = r
        self.color = c

    def update(self, screen):
        self.__show(screen)
    def __show(self, screen):
        xy = conversion_grille.convert_xy_physique_to_xy_numerique((self.x, self.y))
        pygame.draw.circle(screen, self.color, (xy[0], xy[1]), self.radius)
