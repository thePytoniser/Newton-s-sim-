def is_mouse_in(mouse_pos, xy, hw_in):
    return (
        xy[0] <= mouse_pos[0] <= xy[0] + hw_in[1] and
        xy[1] - hw_in[0] <= mouse_pos[1] <= xy[1]
    )