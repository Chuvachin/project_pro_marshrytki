# Declaring all characters.
define n = Character(_("Нина"), image="n")
image n normal = "nina2.png"
define v = Character(_("Водила"), image="v")
image v normal = "vodila.png"
define k = Character(_("Контролерша"), image="k")
image k normal = "kontrolersha.png"
define b = Character(_("Пенсионерка"), image="b")
image b normal = "babka.png"
define au = Character(None, kind=nvl)

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
image bg stop2 = im.Scale("stop2.jpg", 1920, 1080)
image bg stop3 = im.Scale("stop3.jpg", 1920, 1080)

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
default draka = 0
default shtraf = 0
default megapozdno = 0 
default draka_s_babkoy = 0
default dance = 0
default uspeh = 0


# The game starts here.
label start:

    scene bg sleep

    # Start by playing some music
    
    if pozdno == 0:

        au '''У Нины сегодня будет контрольная работа по синтаксису. Ей нужно добраться до корпуса на Родионова. Но есть одно но... — Транспорт. В Нижнем. Новгороде.'''
        nvl hide

        play music "audio/Radar-1.mp3"

        $ renpy.pause(2.0)

        n "о господи"

    else:
        play music "audio/Radar-1.mp3"

        $ renpy.pause(2.0)

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

        "поехать на маршрутке, близко дойти, ехать дольше":

            $ health += 10

            n "сегодня я на уставшем"

            jump marshrutka

        "поехать на автобусе, далеко идти, приехать быстрее":

            n "ок ладно скупой платит дважды"

            jump bus


label marshrutka:

    scene bg stop2
    with fade

    show n normal at left

    n "надеюсь маршрутка приедет быстро и я не успею замерзнуть"
    
    n "о, моя маршрутка!"

    "*заходит*"
    scene bg bus2
    with fade

    show n normal at left

    n "капец, откуда столько людей? на работу едут что ли? лол"

    n "вот бы найти сидячее место"

    n "о, вижу одно"


    $ seat = False

    menu:

        "побежать к свободному месту (блин, через меня будут передавать эти карточки!)":

            n "ура, место завоевано"

            $ seat = True

        "ничего не делать":

            n "ну ладно, постою"

    hide n

    "*едут*"

    "*заходит пенсионерка с тележкой*"

    show b normal at right

    b "молодежь, старшим уступаем"


    show n normal at left

    if seat:
        menu:

            "начать спорить с настойчивой пенсионеркой (разблокировка режима \"трэш\")":

                $ draka_s_babkoy = 1

                n "нет"

                b "ни стыда, ни совести!"

                $ renpy.pause(2.0)

                stop music

                play music "audio/pizdilovka.mp3"

                b "на, получай, дрянь!"

                $ health -= 50

                n "да я тоже не пальцем деланная!"

                n "*повалила пенсионерку на пол*"

                b "ах ты так!"

                b "*добила тележкой*"

                $ health = 0

                jump sadend

            "уступить место":

                n "ладно, моя менталка дороже"

        hide b

    else:
        hide b

        n "ладно, я уже рада, что еду стоя"

    n "*едут дальше*"

    n "*проезжают Молитовский мост*"

    n "*приближается финальный босс (Окский съезд)*"


    if seat:

        n "ну и зачем я ей уступила..."

    else:

        n "надо было бежать к месту тогда..."

    n "*крутой поворот*"

    n "*падает на пол*"

    $ health -= 30
    
    n "ну ладно, не умерла, и на том спасибо"

    $ renpy.pause(2.0)

    "*едут*"

    "*приехали на родионова*"

    $ dance = 1

    jump rodionova 


label bus:

    $ renpy.pause(2.0)

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

            $ uspeh = 1

            $ oplata = True

        "не оплачивать проезд":

            n "как-нибудь в другой раз"

    hide n

    "*едут*"

    $ renpy.pause(2.0)

    "*ещё немного едут*"

    $ renpy.pause(2.0)

    "*входит контролёрша*"

    show k normal at left

    k "достаём билетики"

    hide k

    show n normal at left

    if oplata:

        n "как же мощны мои лапищи"

        n "так и знала"

        hide n

        show k normal at left

        k "предъявите билетик девушка"

        hide k

        show n normal at left

        n "минуточку... вот"

        hide n

        show k normal at left

        k "ок спс"

        hide k

        $ renpy.pause(2.0)

        "*едут*"

        "*приехали на родионова*"

        jump rodionova

        

    else:

        n "ёшкин матрёшкин"

        n "щас ко мне подойдёт"

        n "что же мне делать"

        menu:

            "напасть на контролершу (разблокировка режима \"трэш\")":

                $ draka = 1

                hide n

                show k normal at left

                k "девушка, билетик!"

                hide k

                show n normal at left

                $ renpy.pause(2.0)

                stop music

                play music "audio/pizdilovka.mp3"

                n "а вот этого не хочешь?"

                n "*жестко даёт ей в челюсть*"

                hide n

                show k normal at left

                k "ах ты тварь!"

                k "ну я тебе покажу!"

                k "*бьёт в лицо*"

                hide k

                show n normal at left

                n "ай!!!"

                $ health -= 20

                menu:

                    "продолжить драться":

                        n "ну держись!"

                        n "*кидает на прогиб*"

                        n "*удар в аперкот*"

                        hide n

                        show k normal at left

                        k "доигралась."

                        k "*высасывает душу*"

                        hide k

                        show n normal at left

                        n "ААААААА!!!!!!!!"

                        $ health = minhealth

                        n "кажется я умираю"

                        hide n

                        jump sadend

                    "выбежать из автобуса":

                        n "асталависта паршивка"

                        n "*выбегает*"

                        n "фух еле отделалась"

                        stop music

                        play music "audio/glyukoza_silent.mp3"

                        jump stop2

            "сознаться и оплатить штраф":

                $ shtraf = 1

                n "я... умпк-пупк... я без.. билета....."

                hide n

                show k normal at left

                k "мда подруга"

                k "ну придётся платить штраф"

                hide k

                show n normal at left

                n "эх(("

                n "на тайного санту подружки от меня получат объятия"

                n "*платит*"

                "едут"

                $ renpy.pause(2.0)

                "ещё едут"

                $ renpy.pause(2.0)

                "приехали"

                jump rodionova



label stop2:

    scene bg stop2
    with fade

    show n normal at left

    n "мда"

    n "#girlythings"

    n "ну короче через метро поеду"

    $ megapozdno = 1

    scene bg sleep
    with fade

    $ renpy.pause(2.0)

    jump rodionova


label sadend:

    scene bg sleep

    $ renpy.pause(2.0)

    "..."

    "вы умерли"

    "но это полноправный вариант прохождения игры!"

    jump itog


label rodionova:

    scene bg rodionova
    with fade

    show n normal at left

    n "ура этот маршруточный ад закончен"

    n "свежий воздух!"

    n "теперь начнётся ад академического характера"

    if pozdno:
        
        n "и я ещё и опоздала))"

    elif megapozdno:

        n "кажется сегодня я не напишу контрольную по синтаксису"

    if draka:

        n "ещё и побитая)))"

    if shtraf:

        n "ещё и без денег осталась...."

    jump itog


label itog:

    scene bg sleep

    $ renpy.pause(2.0)

    "вы прошли игру"

    "ваши награды..."

    if draka:

        "борец против капитализма (за драку с контролершей)"


    if draka_s_babkoy:

        "борец против эйджизма (за драку с пенсионеркой)"

    if shtraf:

        "Bis dat qui cito dat (за неуплату проезда и штраф)"

    if megapozdno:

        "лохудра (за опоздание на контрольную)"

    if dance:

        "брейкданс (за падение на пол в маршрутке)"

    if uspeh:

        "честная нижегородка (за оплату проезда)"

        "шутки шутками но проезд оплачивать надо"

        "по крайней мере так говорят наши инвесторы"

    "THE END"

    return
