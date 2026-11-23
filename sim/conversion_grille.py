import pygame
def convert_xy_physique_to_xy_numerique(xy, return_hw = False):
    try:
        infos = pygame.display.Info()
        hw = (infos.current_h, infos.current_w)
    except:
        hw = (600, 800)

    x, y = xy[0], xy[1]

    x0 = hw[1]/2
    y0 = hw[0]/2

    x = x0 + x
    y = y0 -y
    if return_hw:
        return (x, y), hw
    return (x, y)

def convert_xy_numerique_to_xy_physique(xy, return_hw = False):
    try:
        infos = pygame.display.Info()
        hw = (infos.current_h, infos.current_w)
    except:
        hw = (600, 800)
    x, y = xy[0], xy[1]

    x0 = hw[1]/2
    y0 = hw[0]/2

    x = x - x0
    y = y0 - y
    if return_hw:
        return (x, y), hw
    return x, y


print(convert_xy_physique_to_xy_numerique((0 ,-100)))
print(convert_xy_numerique_to_xy_physique((500, 200)))