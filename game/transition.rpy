define fade_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(3.0),
    Solid("#000"), Dissolve(1.0),
    True])
define fadestart = Fade(1.0, 2.0, 1.0 , color ="#000")
define normal = Dissolve(1.0)
transform lout:
    leftin(3000)
transform rout:
    rightin(3000)

transform leftin(x=640):
    xcenter -800 yoffset 0 yanchor 1.0 ypos 1.00 alpha 1.00 subpixel True
    pause 2.0
    linear 0.8 xcenter x
transform rightin(x=640):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.00 alpha 1.00 subpixel True
    pause 1.5
    linear 2 xcenter -800


# define wipeleft_scene = MultipleTransition([
#     False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
#     Solid("#000"), Pause(0.25),
#     Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
#     True])
