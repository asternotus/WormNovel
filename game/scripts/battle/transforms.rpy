define move_time = .5
define stand_anchor = (.5, .5)
define move_size = 10


transform idle_shake(t=move_time, d=move_size, a=stand_anchor):
    pause renpy.random.randint(3,6)
    function renpy.curry(_shake_function)(dt=t, dist=d/2)
    xoffset 0 yoffset 0
    renpy.random.randint(1,3)
    repeat

transform idle_sway(e=0.5):
    easein e xoffset -20
    pause e
    easein e xoffset 20
    pause e
    repeat

transform char_sway(e=1):
    ease e xoffset -30
    ease e xoffset 30
    repeat

transform shake_fade(t=move_time, d=move_size):
    function renpy.curry(_shake_function)(dt=t, dist=d*2)
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        parallel:
            linear .25 alpha 0.0
        parallel:
            linear .25 zoom 1.5
    xoffset 0 yoffset 0

transform dying_fade_out:
    alpha 1.0
    linear 3.0 alpha 0.0

transform right_above_enemy:
    xalign 0.5
    yalign 1.0
    xpos enemy_x_pos
    ypos enemy_y_pos + 30

transform invert_colors:
    matrixcolor InvertMatrix(1.0)

transform reset_invert:
    matrixcolor InvertMatrix(0.0)

transform reset_alpha:
    alpha 1.0

init python:
    global_transforms = {
        "idle_shake": idle_shake,
    }

    def _shake_function(trans, st, at, dt=.5, dist=64):
        if st <= dt:
            trans.xoffset = int((dt-st)*dist*(.5-renpy.random.random())*2)
            trans.yoffset = int((dt-st)*dist*(.5-renpy.random.random())*2)
            return 1.0/60
        else:
            return None
