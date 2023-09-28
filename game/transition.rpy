define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

# define wipeleft_scene = MultipleTransition([
#     False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
#     Solid("#000"), Pause(0.25),
#     Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
#     True])
transform cgfade:
        alpha 1.0
        linear 0.5 alpha 0.0