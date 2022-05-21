# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Zeil = Character('Zeil', color="E03B8B")


# The game starts here.

label start:
    "During a video tutorial…"
    "Zeil" "Hi! This is Zeil."
    "Zeil" "I started \"Zeil Learnings\" recently to share my game-making knowledge."

label sprites:
    "Zeil"  "But wait, where are you?"
    show zeil delighted
    "Zeil"  "Oh!"
    show zeil angry
    "Zeil" "It's not like I was looking for you or anything."
    show extra normal at right
    "Random Girl" "Tsundere..."
    hide extra
    "Zeil" "..."
label character:
    show zeil bored
    "Zeil" "Wow... this is too plain."
    show zeil smile2 with dissolve
    "Zeil" "I want my color to be bright pink!"
    Zeil "Wonderful!"    
label background:
    Zeil "Come on! Let's go the gym."
    scene bg gym
    with fade
    
    show zeil smile2 at left
    Zeil "You got here faster than I did!"  
label bgm:
    play music "audio/bgm_basketball.mp3" fadein 1.0 volume 0.5
    Zeil "Oh, the basketball team is playing?"
    Zeil "It's too loud. I'll meet you in the classroom."
    
    stop music fadeout 1.0
    scene bg classroom
    with fade
    
label sfx:
    play sound "audio/sfx_bell.mp3"
    Zeil "Oh no. It's already time."


label choices:
    default learned = False
    Zeil "Did you learn a thing or two?"
menu:
    "Yes":
        jump choices1_a
    "...":
        jump   choices1_b
label choices1_a:
    Zeil "Good!"
    $ learned = True
    jump choices1_common

label choices1_b:
    Zeil "..."
    jump choices1_common

label choices1_common:
    Zeil "For more effects, you can check out Ren'Py's guides."
    Zeil "The link can be found in the description."

label flags:
    if learned:
        Zeil "If you learned a thing or two, please like the video!"
    else:
        Zeil "You can check out my other videos to learn more about game development!"

    return


    return
