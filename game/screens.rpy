################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        
        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who" 

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.6, yalign=0.8)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize 351
    ypos gui.name_ypos
    ysize 109

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.4
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    font gui.text_dialoge
    
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width



screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            # textbutton _("Quay lại") action Rollback()
            textbutton _("Bỏ qua") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Lịch sử") action ShowMenu('history')
            textbutton _("Tự động") action Preference("auto-forward", "toggle")
            textbutton _("Lưu") action ShowMenu('save')
            textbutton _("Lưu nhanh") action QuickSave()
            textbutton _("Từ bỏ") action MainMenu()
            # textbutton _("Q.Load") action QuickLoad()
            textbutton _("Cài đặt") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    color gui.text_color

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    selected_color gui.selected_color
    font gui.text_font
    size gui.text_quick_size
    spacing gui.navigation_spacing
    ypadding 50
    outlines [(1, "#887F7F", 0, 0)]

style back is button
style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    # size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
 
    properties gui.button_text_properties("navigation_button")
    font gui.text_dialoge
    bold True
    outlines [(2, "#000000", 0, 0)]
    kerning 3.0


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"
    hbox:
        style_prefix "navigation"
        xalign 0.5
        yalign 0.9

        spacing gui.navigation_spacing

        if main_menu:
            
            button:
                style "button_main"
                text _("Bắt đầu"):
                    size gui.interface_text_size
                    color gui.interface_text_color
                    xalign 0.5
                    yalign 0.3    
                action Start()
            button:
                style "button_main"
                text _("Tiếp tục"):
                    size gui.interface_text_size
                    color gui.interface_text_color
                    xalign 0.5
                    yalign 0.3    
                action ShowMenu("load")
            button:
                style "button_main"
                text _("Cài đặt"):
                    size gui.interface_text_size
                    color gui.interface_text_color
                    xalign 0.5
                    yalign 0.3    
                action ShowMenu("preferences")
            button:
                style "button_main"
                text _("Trợ giúp"):
                    size gui.interface_text_size
                    color gui.interface_text_color
                    xalign 0.5
                    yalign 0.3    
                action ShowMenu("help")   
            button:
                style "button_main"
                text _("Thoát"):
                    size gui.interface_text_size
                    color gui.interface_text_color
                    xalign 0.5
                    yalign 0.3    
                action Quit(confirm=True)
        else:

            vbox:
                
                xpos gui.navigation_xpos
                ypos -800

                textbutton __("     "):
                    style "back"
                    action Return()

            if _in_replay:       
                vbox: 
                    textbutton _("End Replay") action EndReplay(confirm=True)
    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    # use navigation


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style button_main is  default
style button_main:
    xsize 288
    ysize 128
    idle_background Frame("gui/button/button_main.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.button_xalign)
    hover_background Frame("gui/button/button_main_hover.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.button_xalign)
    padding gui.namebox_borders.padding
style main_menu_frame:
    xsize 420
    yfill True

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.
image button_back = "./gui/overlay/back.png"
screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    
    frame:
        style "game_menu_outer_frame"
        imagebutton:
            xpos 0.08
            ypos 0.1
            xanchor 0.5
            yanchor 0.5
            idle "gui/overlay/back.png"
            action Return()
        hbox:
           
            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        # scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    # use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style title_text:
    color gui.hover_color

style game_menu_outer_frame:

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 0
    yfill 0

style game_menu_content_frame:
    left_margin 0
    right_margin 0
    top_margin 165

style game_menu_viewport:
    xsize 1920

style game_menu_vscrollbar:
    # xpos -100
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    ysize 120
    xalign 0.5
    yalign 0.03
    

style game_menu_label_text:
    size gui.title_text_size_big
    outlines [(0.2, "#216EB6", 0.2, 0.2)]
    color gui.hover_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

# screen about():

#     tag menu

#     ## This use statement includes the game_menu screen inside this one. The
#     ## vbox child is then included inside the viewport inside the game_menu
#     ## screen.
#     use game_menu(_("About"), scroll="viewport"):

#         style_prefix "about"

#         vbox:

#             # label "[config.name!t]"
#             # text _("Version [config.version!t]\n")

#             ## gui.about is usually set in options.rpy.
#             # if gui.about:
#             #     text "[gui.about!t]\n"

#             # text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


# style about_label is gui_label
# style about_label_text is gui_label_text
# style about_text is gui_text

# style about_label_text:
#     size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Lưu"))


screen load():

    tag menu

    use file_slots(_("Tải"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_(""), auto=_("Tự động lưu"), quick=_("Lưu nhanh"))

    use game_menu(title):

        fixed:
            order_reverse True

            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing 30

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    hbox:
                        hbox:   
                            button:
                                action FileAction(slot)
                                has vbox
                                
                                text FileTime(slot, format=_("%B %d %Y, %H:%M"), empty=_("")):
                                    style "slot_time_text"
                        
                                add FileScreenshot(slot):
                                    ypos 10
                                
                                imagebutton:
                                    xpos 350
                                    ypos -250
                                    auto "gui/button/x_%s.png" action FileDelete(slot)
                                
                                
                                text FileSaveName(slot):
                                    style "slot_name_text" 
                                key "save_delete" action FileDelete(slot)
                            
                       

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    # xalign 0.5
                    # ypos 40
                    spacing gui.page_spacing

                    textbutton _("<"):
                        background "./gui/overlay/history_page_but.png"
                        action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A"):
                            background "./gui/overlay/history_page_but.png"
                            action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q"):
                            background "./gui/overlay/history_page_but.png"
                            action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]":
                            background "./gui/overlay/history_page_but.png"
                            action FilePage(page)
                        

                    textbutton _(">") action FilePageNext()

                # if config.has_sync:
  
                #     if CurrentScreenName() == "save":
                #         textbutton _("Upload Sync"):
                #             action UploadSync()
                #             xalign 0.5
                        
                          
                #     else:
                #         textbutton _("Download Sync"):
                #             action DownloadSync()
                #             xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style frame is default


style page_label:
    xpadding 75
    ypadding 20

style page_label_text:
    textalign 0.5
    layout "subtitle"
    size gui.text_size
    color gui.hover_color
    outlines [(0.2, "#216EB6", 0.2, 0.2)]
    

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    
    color gui.text_color
    hover_color gui.hover_color
    selected_color gui.selected_color


style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    size gui.text_time_size
    color gui.idle_color
 
    


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Cài đặt"), scroll="viewport"):

        vbox:
            xpos 0.25
            ypos 0.1
            
            hbox:
                box_wrap True
                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Hiển thị")
                        textbutton _("Cửa sổ") action Preference("display", "window")
                        textbutton _("Toàn màn hình") action Preference("display", "fullscreen")
                    
                    vbox:
                        style_prefix "check"
                        label _("Bỏ qua")
                        textbutton _("Thoại chưa đọc") action Preference("skip", "toggle")
                        textbutton _("Sau mỗi lựa chọn") action Preference("after choices", "toggle")
                        textbutton _("Hiệu ứng chuyển cảnh") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Tốc độ văn bản")

                    bar value Preference("text speed")

                    label _("Tốc độ tự động đọc")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Âm lượng nhạc nền")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Âm lượng hiệu ứng")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    

                    # if config.has_music or config.has_sound or config.has_voice:
                    #     null height gui.pref_spacing

                    #     textbutton _("Tắt tiếng"):
                    #         action Preference("all mute", "toggle")
                    #         style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3
    

style pref_label_text:
    yalign 1.0
    color gui.text_settings
    size gui.text_label_settings

style pref_vbox:
    xsize 650

style radio_vbox:
    ysize 200

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
    selected_color gui.hover_color

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    color gui.idle_text_color
    hover_color gui.hover_color
style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    hover_color gui.hover_color
style check_button_text:
    properties gui.button_text_properties("check_button")
    color gui.idle_text_color
    hover_color gui.hover_color
    selected_color gui.hover_color
style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("Lịch sử"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:
                

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height


style history_name:
    
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
    

style history_name_text:
    ypos 10
    min_width gui.history_name_width
    textalign gui.history_name_xalign
    outlines [(0.5, "#000000", 0.5, 0.5)]

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    color gui.text_color
    size gui.text_history_size

style history_label:
    xfill True
    color gui.text_idle_color
    

style history_label_text:
    xalign 0.5
    


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Hướng dẫn"), scroll="viewport"):

        style_prefix "help"
        
        vbox:
            xpos 250
            ypos 50
            spacing 23
            
            hbox:
                textbutton _("Bàn phím") action SetScreenVariable("device", "keyboard")
                textbutton _("Chuột") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Phím Enter")
        text _("Tiếp tục hội thoại hoặc kích hoạt giao diện")

    hbox:
        label _("Phím Space")
        text _("Tiếp tục hội thoại mà không cần lựa chọn")

    hbox:
        label _("Phím mũi tên")
        text _("Điều hướng giao diện")

    hbox:
        label _("Phím Esc")
        text _("ruy cập menu")

    hbox:
        label _("Phím Ctrl")
        text _("Bỏ qua hội thoại khi gi")

    hbox:
        label _("Phím Tab")
        text _("Chuyển đổi chế độ bỏ qua hội thoại")

    hbox:
        label _("Phím Page Up")
        text _("Quay lại đoạn hội thoại trước đó")

    hbox:
        label _("Phím Page Down")
        text _("Chuyển tới đoạn hội thoại phía sau")

    hbox:
        label "Phím H"
        text _("Ẩn giao diện")

    hbox:
        label "Phím S"
        text _("Chụp màn hình")


screen mouse_help():

    hbox:
        label _("Chuột trái")
        text _("Tiếp tục hội thoại hoặc kích hoạt giao diện")

    hbox:
        label _("Chuột giữa")
        text _("Ẩn giao diện")

    hbox:
        label _("Chuột phải")
        text _("Truy cập Lưu")

    hbox:
        label _("Lăn chuột giữa Lên")
        text _("Quay lại đoạn hội thoại trước đó")

    hbox:
        label _("Lăn chuột giữa xuống")
        text _("Chuyển tới đoạn hội thoại phía sau")


screen gamepad_help():
    
    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 50

style help_button_text:
    properties gui.button_text_properties("help_button")
    color gui.hover_color
    hover_color gui.selected_color
    

style help_label:
    xsize 375
    xpos 60
    right_padding 100

style help_label_text:
    size gui.text_help_size
    xalign 1
    color gui.text_color
    textalign 0.5
style help_text:
    size gui.text_help_size
    color gui.text_color

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45
            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 50
                imagebutton:
                    xalign 0.2
                    yalign 0.5
                    auto "gui/button/button_yes_%s.png" action yes_action
                imagebutton:
                    xalign 0.2
                    yalign 0.5
                    auto "gui/button/button_no_%s.png" action no_action
                    
                
    

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame(["gui/box_confirm.png","gui/confirm_frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    color gui.text_color

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Đang bỏ qua")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#fff"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"

style game_menu_outer_frame:
    variant "small"


style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900


style splash_text:
    size 60
    color "#000"
    font gui.text_font
    text_align 0.5
    outlines []