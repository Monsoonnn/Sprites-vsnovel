## variables
default chapter = 0

## End of variables
## bgm
define audio.bgm1 = "bgm/bgm1.mp3"
define audio.bgm2 = "bgm/bgm2.mp3"
define audio.bgm3 = "bgm/bgm3.mp3"
## End of bgm

# sound


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
# image background




## image character
image v1 = "viet/1.png"
image v2 = "viet/12.png"
image v3 = "viet/13.png"
image v4 = "viet/14.png"

image n1 ="ngan/23a.png"
image n2 ="ngan/24aa.png"
##image character
#image mat

image la1 = SnowBlossom("images/bg_sc1/la1.png", count=2, border=50, xspeed=(20, 40), yspeed=(100, 120), start=0.1, fast=False, horizontal=False)
image la2 = SnowBlossom("images/bg_sc1/la2.png", count=2, border=50, xspeed=(30, 50), yspeed=(120, 140), start=0.2, fast=False, horizontal=False)
image la3 = SnowBlossom("images/bg_sc1/la3.png", count=2, border=50, xspeed=(40, 60), yspeed=(140, 160), start=0.3, fast=False, horizontal=False)
image la4 = SnowBlossom("images/bg_sc1/la4.png", count=2, border=50, xspeed=(50, 70), yspeed=(150, 170), start=0.4, fast=False, horizontal=False)


## Character

#click to continue
image ctc:
        xpos 1280 ypos 1020
        alpha 2.0
        "gui/ctc.png"
        0.5
        alpha 0.0 
        0.5
        repeat
#click to continue
define narrator = Character(ctc="ctc", ctc_position="fixed")
define v = DynamicCharacter('v_name', image='v', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define none = DynamicCharacter('none', image='n', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='v', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")


default v_name = "Việt"
default n_name = "Ngân"
default none = "???"






# End of character

# color image

image white = "#ffffff"


#logo
image logo = "Game_Logo.png"

image splash_text = Text("GAME NÀY ĐƯỢC LÀM BỞI NHÓM 8", style="splash_text",)