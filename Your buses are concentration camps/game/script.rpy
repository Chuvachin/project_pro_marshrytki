# Declaring all characters.
define n = Character(_("Нина"), image="n")
image n normal = "nina2.png"
define v = Character(_("Водила"), image="v")
image v normal = "vodila.png"
define k = Character(_("Контролерша"), image="k")
image k normal = "kontrlersha.png"
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


# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False

# The game starts here.
label start:

    # Start by playing some music.
    play music "audio/Radar-1.mp3"
    
    n "о господи"

    scene bg bedroom
    with fade

    menu:

        "отложить будильник на 10 минут":

            stop music

            n "хррр мимим"

            "это действие будет иметь последствия🦋"

            jump coming_late

        "встать и пойти делать завтрак":

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



    n "как же хороша кухня в общежитии на ул. Львовской, д. 1В"

    n "сделаю себе кофейку"

    "*делает кофе*"

    "*пьёт кофе*"

    n "вот и позавтракала"

    n "так-с а что там с маршрутом?"

    menu:

        "поехать на маршрутке, близко дойти, но ехать с пересадками":

            n "сегодня я на уставшем"

            n "лучше просто постою на остановках пару раз"

            jump marshrutka

        "поехать на автобусе, далеко дойти, но ехать без пересадок":

            n "ок ладно я задолбаюсь пересаживаться"

            jump bus


label bus:

    scene bg stop
    with fade

    show n normal at left

    n "фух добралась"
    
    n "о, вот и автобус, неужели так быстро!"

    "*заходит*"
    scene bg bus1
    with fade

    show n normal at left

    n "ну еле забралась"

    n "народу!"

    n "о кажется кондуктора нет"

    n "а у меня так мало денег"

    n "скоро еще и новый год"

    n "хочу какать"
       
    $ oplata = 0

    menu:

        "оплатить проезд":

            n "совесть моя чиста"

            $ oplata += 1

        "не оплачивать проезд":

            n "ну как-нибудь в другой раз"

    hide n

    "едут"

    "ещё немного едут"

    show k normal

    k "достаём билетики"

    n "ооооооо"

    n "щас ко мне подойдёт"

    k "предъявите билетик девушка"

    if oplata == 0:

        n "пошла нахуй пидорша"

        return

    else:

        n "да конечно вот"

        n "*показывает билет*"

        return