import math


def get_g_from_xy(xy, m,xy_ref, M_ref = None , G_gravi = None):
    if M_ref == None:
        M_ref = 5.972e24
    if G_gravi == None:
        G_gravi = 6.67430e-11

    x, y = xy[0], xy[1]
    x_ref, y_ref = xy_ref[0], xy_ref[1]

    dist = math.sqrt((x - x_ref) ** 2 + (y - y_ref) ** 2)

    if dist == 0:
        return (0, 0), 0
    gx = -G_gravi * M_ref * ((x - x_ref) / dist ** 3)

    gy = -G_gravi * M_ref * ((y - y_ref) / dist ** 3)

    return (gx, gy), dist