# Declaring all characters.
define n = Character(_("Нина"), image="n")
image n normal = "nina2.png"
define v = Character(_("Водила"), image="v")
image v normal = "vodila.png"
define k = Character(_("Контролерша"), image="k")
image k normal = "kontrolersha.png"
define b =Character(_("Бабка"), image="b")
image b normal = "babka.png"

image bg bedroom = im.Scale("bedroom2.jpg", 1920, 1080)
image bg kitchen = im.Scale("kitchen.jpg", 1920, 1080)
image bg stop = im.Scale("stop.jpg", 1920, 1080)
image bg bus1 = im.Scale("bus1.jpg", 1920, 1080)
image bg bus2 = im.Scale("bus2.jpg", 1920, 1080)
image bg bus3 = im.Scale("bus3.jpg", 1920, 1080)
image bg bus4 = im.Scale("bus4.jpg", 1920, 1080)
image bg bus5 = im.Scale("bus5.jpg", 1920, 1080)
image bg rodionova = im.Scale("rodionova.jpg", 1920, 1080)
image bg sleep = im.Scale("sleep.jpg", 1920, 1080)

default maxhealth = 100
default minhealth = 0
default health = 50

# Экран для отображения шкалы здоровья
screen health_bar:
    bar:
        xsize 600
        ysize 300
        xalign 0.95
        yalign 0.005
        value AnimatedValue (value=health, range=maxhealth, delay=1.0)
        top_bar Frame('gui/bar/full.png', 10, 10)
        bottom_bar Frame('gui/bar/empty.png', 10, 10)
default pozdno = 0

# The game starts here.
label start:

    scene bg sleep

    # Start by playing some music.
    play music "audio/Radar-1.mp3"
    
    if pozdno == 0:
        n "о господи"
    else:
        n "чёрт"

    scene bg bedroom
    with fade

    show screen health_bar
    with fade

    if pozdno == 0: 

        menu:

            "отложить будильник на 10 минут":

                stop music

                n "хррр мимим"

                "это действие будет иметь последствия🦋"

                $ pozdno += 1

                scene bg sleep

                $ renpy.pause(2.0)

                jump start

            "встать и пойти делать завтрак":

                stop music

                show n normal at left

                n "снова не выспалась"

                n "и как я кр напишу?"

                n "...((("

                n "надо позавтракать"

                jump breakfast
    else:

        stop music

        show n normal at left

        n "снова не выспалась"

        n "и как я кр напишу?"

        n "...((("

        n "надо позавтракать"

        jump breakfast




label breakfast:

    show bg kitchen
    with fade

    show screen health_bar

    play music "audio/glyukoza_silent.mp3"

    n "как же хороша кухня в общежитии на ул. Львовской, д. 1В"

    n "хлебосол"

    n "сделаю себе кофейку"

    "*делает кофе*"

    "*пьёт кофе*"

    $ health += 10

    n "вот и позавтракала"

    n "так-с а что там с маршрутом?"

    menu:

        "поехать на маршрутке, близко дойти, но ехать с пересадками":

            $ health += 10

            n "сегодня я на уставшем"

            n "лучше просто постою на остановках пару раз"

            jump marshrutka

        "поехать на автобусе, далеко идти, но ехать без пересадок":

            n "ок ладно я задолбаюсь пересаживаться"

            jump bus


label bus:

    scene bg stop
    with fade

    show n normal at left

    n "фух добралась"
    
    n "о, вот и автобус. как быстро, бывает же!"

    "*заходит*"
    scene bg bus1
    with fade

    show n normal at left

    n "ну еле забралась"

    n "народу!"

    n "о кажется кондуктора нет"

    n "а у меня так мало денег"

    n "скоро еще и новый год"
       
    $ oplata = False

    menu:

        "оплатить проезд":

            n "совесть моя чиста"

            $ oplata = True

        "не оплачивать проезд":

            n "как-нибудь в другой раз"

    hide n

    "едут"

    "ещё немного едут"

    show k normal

    k "достаём билетики"

    hide k

    show n normal at left

    if oplata:

        n "как же мощны мои лапищи"

        n "так и знала"

        hide n

        show k normal

        k "предъявите билетик девушка"

        show n normal at left

        n "минуточку... вот"

        hide n

        show k normal

        k "ок спс"

    else:

        n "ёшкин матрёшкин"

        n "щас ко мне подойдёт"

        n "что же мне делать"

        menu:

            "дать контролерше п*зды":

                n "совесть моя чиста"

                $ oplata = True

            "не оплачивать проезд":

                n "ну как-нибудь в другой раз"


label rodionova:

    scene bg rodionova
    with fade

    show n normal at left

    n "ура этот маршруточный ад закончен"

    n "свежий воздух!"

    n "теперь начнётся ад академического характера"

    if pozdno:
        
        n "и я ещё и опоздала))"

