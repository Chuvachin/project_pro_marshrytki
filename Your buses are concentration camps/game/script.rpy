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

    n "вот и позавтракали"

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
    
    n "о, вот и автобус"

    "*заходит*"
    scene bg bus1
    with fade

    show n normal at left

    n "ну еле забралась"

    n "народу!"

    n "о кажется контролера нет"

    n "а у меня так мало денег"

    n "скоро еще и новый год"
    
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

    if oplata = 0:

        n "пошла нахуй пидорша"

    else:

        n "да конечно вот"

        n "*показывает билет*"




        

label book:

    $ book = True

    m "It's like an interactive book that you can read on a computer or a console."

    show sylvie green surprised

    s "Interactive?"

    m "You can make choices that lead to different events and endings in the story."

    s "So where does the \"visual\" part come in?"

    m "Visual novels have pictures and even music, sound effects, and sometimes voice acting to go along with the text."

    show sylvie green smile

    s "I see! That certainly sounds like fun. I actually used to make webcomics way back when, so I've got lots of story ideas."

    m "That's great! So...would you be interested in working with me as an artist?"

    s "I'd love to!"

    jump marry

label marry:

    scene black
    with dissolve

    "And so, we become a visual novel creating duo."

    scene bg club
    with dissolve

    "Over the years, we make lots of games and have a lot of fun making them."

    if book:

        "Our first game is based on one of Sylvie's ideas, but afterwards I get to come up with stories of my own, too."

    "We take turns coming up with stories and characters and support each other to make some great games!"

    "And one day..."

    show sylvie blue normal
    with dissolve

    s "Hey..."

    m "Yes?"

    show sylvie blue giggle

    s "Will you marry me?"

    m "What? Where did this come from?"

    show sylvie blue surprised

    s "Come on, how long have we been dating?"

    m "A while..."

    show sylvie blue smile

    s "These last few years we've been making visual novels together, spending time together, helping each other..."

    s "I've gotten to know you and care about you better than anyone else. And I think the same goes for you, right?"

    m "Sylvie..."

    show sylvie blue giggle

    s "But I know you're the indecisive type. If I held back, who knows when you'd propose?"

    show sylvie blue normal

    s "So will you marry me?"

    m "Of course I will! I've actually been meaning to propose, honest!"

    s "I know, I know."

    m "I guess... I was too worried about timing. I wanted to ask the right question at the right time."

    show sylvie blue giggle

    s "You worry too much. If only this were a visual novel and I could pick an option to give you more courage!"

    scene black
    with dissolve

    "We get married shortly after that."

    "Our visual novel duo lives on even after we're married...and I try my best to be more decisive."

    "Together, we live happily ever after even now."

    "{b}Good Ending{/b}."

    return

label later:

    "I can't get up the nerve to ask right now. With a gulp, I decide to ask her later."

    scene black
    with dissolve

    "But I'm an indecisive person."

    "I couldn't ask her that day and I end up never being able to ask her."

    "I guess I'll never know the answer to my question now..."

    "{b}Bad Ending{/b}."

    return
