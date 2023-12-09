init python:
    renpy.music.register_channel("sfx1", "sfx", True)
    renpy.music.register_channel("sfx2", "sfx", True)
    renpy.music.register_channel("sfx3", "sfx", True)
## variables
default chapter = 0

## End of variables
## bgm
define audio.bgm1 = "bgm/bgm1.mp3"
define audio.bgm2 = "bgm/bgm2.mp3"
define audio.bgm3 = "bgm/bgm3.mp3"
define audio.bgm4 = "bgm/bgm4.mp3"
define audio.bgm5 = "bgm/bgm-5.mp3"
define audio.bgm6 = "bgm/bgm-6.mp3"
define audio.bgm7 = "bgm/bgm-7.mp3"
define audio.bgm8 = "bgm/bgm-8.mp3"
## End of bgm

# sound


define audio.foot = "sound/footstep.mp3"
define audio.body_fall = "sound/body_fall.mp3"
define audio.breaking_new = "sound/breaking_new.mp3"
define audio.car_moving = "sound/car_moving.mp3"
define audio.heart_beat = "sound/heart_beat.mp3"
define audio.heavy_breathing = "sound/heavy_breathing.mp3"
define audio.hit_sound = "sound/hit_sound.mp3"
define audio.phone_ring = "sound/phone_ring.mp3"
define audio.running = "sound/running.mp3"
define audio.wind = "sound/wind.mp3"
define audio.vehicles = "sound/vehicles.mp3"
define audio.Electric = "sound/Electric.mp3"
define audio.glass_break = "sound/glass_break.mp3"


# define audio.bell = 


# End of sound


# image background
image bg sc0_1 = "bg_sc0/1.png"
image bg sc0_2 = "bg_sc0/2.png"
image bg sc0_3 = "bg_sc0/3.png"
image bg sc0_4 = "bg_sc0/4.png"
image bg sc0_5 = "bg_sc0/5.png"
image bg sc0_6 = "bg_sc0/6.png"
image bg sc0_7 = "bg_sc0/7.png"
image bg sc0_8 = "bg_sc0/8.png"
image bg sc0_9 = "bg_sc0/9.png"


image bg sc1_1 = "bg_sc1/bg.png"
image bg sc1_2 = "bg_sc1/64.png"
image bg sc1_3 = "bg_sc1/2.png"
image bg sc1_31 = "bg_sc1/31.png"
image bg sc1_4 = "bg_sc1/66.png"

image bg op1_1 = "bg_op/69.png"
image bg op1_2 = "bg_op/68.png"
image bg op1_3 = "bg_op/76.png"
image bg op1_4 = "bg_op/77.png"
image bg op1_5 = "bg_op/78.png"
image bg op1_6 = "bg_op/79.png"
image bg op1_7 = "bg_op/75.png"
image bg op1_8 = "bg_op/80.png"

image bg op2_1 = "bg_op/70.png"
image bg op2_2 = "bg_op/81.png"
image bg op2_3 = "bg_op/82.png"
image bg op2_4 = "bg_op/83.png"
image bg op2_5 = "bg_op/84.png"
image bg op2_6 = "bg_op/85.png"
image bg op2_7 = "bg_op/86.png"
image bg op2_8 = "bg_op/87.png"
image bg op2_9 = "bg_op/88.png"
image bg op2_10 = "bg_op/90.png"

image bg op2_11:
        yalign 1
        "bg_op/91.png"
        ease 0.2 yalign 0.95
        ease 0.2 yalign 0.85
        ease 0.2 yalign 0.75
        ease 0.2 yalign 0.65
        ease 0.2 yalign 0.55
        ease 0.2 yalign 0.45
        ease 0.2 yalign 0.35
        ease 0.2 yalign 0.25
        ease 0.2 yalign 0.15
        ease 0.2 yalign 0.05
        ease 0.2 yalign 0.00
        yalign 0

image bg_1 = "BG/148.png"
image bg_2 = "BG/162.png"

image bg op3_1 = "bg_op3/1.png"
image bg op3_2 = "bg_op3/2.png"
image bg op3_3 = "bg_op3/3.png"
image bg op3_4 = "bg_op3/4.png"
image bg op3_5 = "bg_op3/5.png"
image bg op3_6 = "bg_op3/6.png"
image bg op3_7 = "bg_op3/7.png"
image bg op3_8 = "bg_op3/8.png"
image bg op3_9 = "bg_op3/9.png"
image bg op3_10 = "bg_op3/10.png"
image bg op3_11 = "bg_op3/11.png"
image bg op3_12 = "bg_op3/12.png"
image bg op3_13 = "bg_op3/13.png"
image bg op3_14 = "bg_op3/14.png"
image bg op3_15 = "bg_op3/15.png"
image bg op3_16 = "bg_op3/16.png"
image bg op3_17 = "bg_op3/17.png"
image bg op3_18 = "bg_op3/18.png"
image bg op3_19 = "bg_op3/19.png"
image bg op3_20 = "bg_op3/20.png"
image bg op3_21 = "bg_op3/21.png"
image bg op3_22 = "bg_op3/22.png"
image bg op3_23 = "bg_op3/23.png"
image bg op3_24 = "bg_op3/24.png"
image bg op3_25 = "bg_op3/25.png"
image bg op3_26 = "bg_op3/26.png"
image bg op3_27 = "bg_op3/27.png"
image bg op3_28 = "bg_op3/28.png"
image bg op3_29 = "bg_op3/29.png"
image bg op3_30 = "bg_op3/30.png"
image bg op3_31 = "bg_op3/31.png"
image bg op3_32 = "bg_op3/32.png"
image bg op3_33 = "bg_op3/33.png"
image bg op3_34 = "bg_op3/34.png"
image bg op3_35 = "bg_op3/35.png"
image bg op3_36 = "bg_op3/36.png"
image bg op3_37 = "bg_op3/37.png"
image bg op3_38 = "bg_op3/38.png"
image bg op3_39 = "bg_op3/39.png"
image bg op3_40 = "bg_op3/40.png"

# image background




## image character
image v1 = "viet/1.png"
image v2 = "viet/12.png"
image v3 = "viet/13.png"
image v4 = "viet/14.png"
image v5 = "viet/33.3a.png"
image v6 = "viet/15.png"
image v7 = "viet/16.png"
image v8 = "viet/17.png"
image v9 = "viet/18.png"
image v10 = "viet/19.png"
image v11 = "viet/20.png"
image v12 = "viet/21.png"

image n1 = "ngan/23a.png"
image n2 = "ngan/24aa.png"
image n3 = "ngan/33.2a.png"
image n4 = "ngan/1.png"
image n5 = "ngan/2.png"
image n6 = "ngan/3.png"
image n7 = "ngan/4.png"
image n8 = "ngan/5.png"
image n9 = "ngan/6.png"

image g1 ="giang/1.png"
image g2 ="giang/2.png"
image g3 ="giang/3.png"
image g4 ="giang/4.png"
image g5 ="giang/5.png"
image g6 ="giang/6.png"
image g7 ="giang/7.png"
image g8 ="giang/8.png"
##image character
#image mat

image la1 = SnowBlossom("images/bg_sc1/la1.png", count=2, border=50, xspeed=(20, 40), yspeed=(100, 120), start=0.1, fast=False, horizontal=False)
image la2 = SnowBlossom("images/bg_sc1/la2.png", count=2, border=50, xspeed=(30, 50), yspeed=(120, 140), start=0.2, fast=False, horizontal=False)
image la3 = SnowBlossom("images/bg_sc1/la3.png", count=2, border=50, xspeed=(40, 60), yspeed=(140, 160), start=0.3, fast=False, horizontal=False)
image la4 = SnowBlossom("images/bg_sc1/la4.png", count=2, border=50, xspeed=(50, 70), yspeed=(150, 170), start=0.4, fast=False, horizontal=False)


## Character

#click to continue
image ctc:
        xpos 1680 ypos 950
        alpha 2.0
        "gui/ctc.png"
        0.5
        alpha 0.0 
        0.5
        repeat
#click to continue

define narrator = Character(ctc="ctc", ctc_position="fixed")
define v = DynamicCharacter('v_name', image='v', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed",color="#fff")
define none = DynamicCharacter('none', image='n', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define v_a_g = DynamicCharacter('v_a_g', image='v_a_g', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='v', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#fff")
define g = DynamicCharacter('g_name', image='g', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#fff")


default v_name = "Việt"
default n_name = "Ngân"
default none = "???"
default g_name = "Giang"
default v_a_g = "Việt/Giang"






# End of character

# color image

image white = "#ffffff"


#logo
image logo = "Game_Logo.png"

image splash_text = Text("GAME NÀY ĐƯỢC LÀM BỞI NHÓM 8", style="splash_text",)