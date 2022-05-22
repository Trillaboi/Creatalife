# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the

# name of the character.

define narrator = Character(_(""), color="#2878ad")
image nft = Movie((1280,720), channel="movie", play="nft.webm")
image feelin = Movie((1280,720), channel="movie", play="feelin.webm")
image feelin2 = Movie((1280,720), channel="movie", play="feelin2.webm")
image finish = Movie((1280,720), channel="movie", play="finish.webm")

define wallet = Character("[wallet]")

#define address = Address("[address]")

init python:
    import urllib2, json

# Define vars that will change
default heartpoints = 5
default moneypoints = 5
default heartlover = 0
default moneylover = 0



# The game starts here.

label start:
    $ heartpoints = 5
    $ moneypoints = 5
    $ tokenpoints = 0
    scene intro
    with dissolve

    $wallet = renpy.input("Wallet detected in clipboard", length=32)
    python:
        url = "http://127.0.0.1:5000/get_clipboard"
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        wallet = json.loads(response.read().strip())["address"]

    "Wallet detected [wallet]"


label intro:

    "Let's start"

    scene intro_1
    with dissolve
    show c1 at left
    with dissolve

    menu:

        "Would you rather...?"

        "Buy your dream house":
            $ moneypoints -=1
            $ heartpoints +=1
            scene 1
            show c2 at left
            with dissolve
            jump question_2

        "Receive 500,000 CASH":

            $ moneypoints +=1
            $ heartpoints -=1
            scene 1
            show c2 at left
            with dissolve
            jump question_2



label question_2:

     menu:

        "Would you rather...?"

        "Go to college to learn Digital Art":
            $ moneypoints -=1
            $ heartpoints +=1
            scene 2
            show c3 at left
            with dissolve
            jump question_3

        "Buy materials to create your first art piece":
            $ moneypoints +=1
            $ heartpoints -=1
            scene 2
            show c3 at left
            with dissolve
            jump question_3

label question_3:

     menu:

        "A client of yours is very demanding but pays well and wants to work with you more often?"

        "Set a schedule more suitable for you":
            $ moneypoints -=1
            $ heartpoints +=1
            jump question_5

        "Do you negotiate higher pay":
            $ moneypoints +=1
            $ heartpoints -=1
            if heartpoints <= 2:
                scene 6
                show c4 at left
                with dissolve
                jump question_4
            else:
                $ moneypoints +=1
                $ heartpoints -=1
                scene 6
                show c4 at left
                with dissolve
                jump question_5
            scene 6
            jump question_4


label question_4:

     menu:

        "Do you lean more towards"

        "well-being":
            $ moneypoints -= 1
            $ heartpoints += 1
            scene trigger
            jump question_5

        "financial well-being":
            $ moneypoints = 7
            $ heartpoints -=1
            with dissolve
            jump question_congrats


label question_congrats:

        scene feelin
        pause
        scene page5
        show c5 at left
        with dissolve
        $ tokenpoints += 10


label question_5:

     menu:

        "You are not making enough money do you"

        "Create multiple streams of income":
            $ moneypoints -=1
            $ heartpoints +=1
            scene 7
            show c6 at left
            with dissolve
            jump question_6

        "Tighten your budget":
            $ moneypoints +=1
            $ heartpoints -=1
            scene 7
            show c6 at left
            with dissolve
            jump question_6

label question_6:

     menu:

        "Do you want to watch this 10 min video and earn 25 points?"

        "yes":
            with dissolve
            jump video_question

        "no":
            with dissolve
            jump chapter_3

label video_question:

    scene nft
    pause
    scene 7
    show c7 at left
    with dissolve

label question_7:

     menu:

        "Qualifying Question what was Susans friend's name"

        "Mark":
            with dissolve
            jump question_congrats_2

        "John":
            with dissolve
            jump chapter_3

label question_congrats_2:

    scene feelin2
    pause
    $ tokenpoints += 25

    python:
        data = {'wallet_address': wallet,'amount': tokenpoints}
        req = urllib2.Request("http://127.0.0.1:5000/request_tokens")
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, json.dumps(data))
        print(response.read())

    show finish
    pause

label chapter_3:

    scene black

    with dissolve

    scene black

    with dissolve

    if tokenpoints == 35:
        $ tokenpoints = 3
    elif tokenpoints == 25:
        $ tokenpoints = 2
    elif tokenpoints == 10:
        $ tokenpoints = 1
    elif tokenpoints == 0:
        $ tokenpoints = 0

    return
