define fade_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(3.0),
    Solid("#000"), Dissolve(1.0),
    True])
define fade = Fade(0.0, 2.0, 2.0 , color ="#000")
define normal = Dissolve(1.0)

# define wipeleft_scene = MultipleTransition([
#     False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
#     Solid("#000"), Pause(0.25),
#     Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
#     True])
transform cgfade:
        alpha 1.0
        linear 0.5 alpha 0.0