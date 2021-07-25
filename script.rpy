init python:
  def eyewarp(x):
    return x**1.33
  eye_open = ImageDissolve("eye.png", .8, ramplen=128, reverse=False, time_warp=eyewarp)
  eye_shut = ImageDissolve("eye.png", .8, ramplen=128, reverse=True, time_warp=eyewarp)
image black:
  Solid("#000")
image bggg:
  Solid("#101018")
image white:
  Solid("#FFF")

# Определение персонажей игры.
define r = Character('Рома', color="#000000")
define u = Character('Юля', color="#000000")
define k = Character('Кондуктор', color="#000000")
define rau = Character('Рома и Юля', color="#000000")
define bd = Character('???', color="#000000")

init:
    image forest_background = "images/forest background.png"
    image space_background = "images/stars.png"
    image ulya normal glitch = Glitch(_fps=3.)("ulya normal.png")
    transform scroll_in(delay = 10.0):
        ypos 150
        xpos config.screen_width xzoom -1.0
        linear delay xpos 0
        pause delay
        repeat
    transform scroll_in2(delay = 10.0):
        ypos 150
        xpos config.screen_width
        pause delay
        linear delay xpos 0
        repeat
    transform scroll_out(delay = 10.0):
        ypos 150
        xpos 0
        linear delay xpos -config.screen_width
        pause delay
        repeat
    transform scroll_out2(delay = 10.0):
        ypos 150
        xpos config.screen_width
        pause delay
        xpos 0 xzoom -1.0
        linear delay xpos -config.screen_width
        repeat
    transform down_to_up:
        xanchor 0
        yanchor 0
        xpos 0
        ypos 0
        linear 2.0 xalign 1.0 yalign 1.0
        repeat
    transform left_to_right:
        xalign 1.0
        linear 1.2 xalign 0.0
        repeat



init python:
    # функция объединаяет трансформации
    # выводит на экран 
    def _scroll(img, effect = None, delay = 10.0):
        renpy.show(img + "1", what = ImageReference(img), at_list = [scroll_in(delay)])
        renpy.show(img + "2", what = ImageReference(img), at_list = [scroll_out(delay)])
        renpy.show(img + "3", what = ImageReference(img), at_list = [scroll_in2(delay)])
        renpy.show(img + "4", what = ImageReference(img), at_list = [scroll_out2(delay)])
        renpy.with_statement(effect)
    def _hide(img, effect = None):
        renpy.hide(img + "1")
        renpy.hide(img + "2")
        renpy.hide(img + "3")
        renpy.hide(img + "4")
        renpy.with_statement(effect)

init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # центральная позиция
                self.dist = dist    # максимальное расстояние, в пикселях, от начальной точки
                self.child = child
                
            def __call__(self, t, sizes):
                # Число с плавающей точкой в целое число... превращает числа с плавающей точкой
                # в целые.      
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)


init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

image noise:
    "images/shum2.png"
    pause 0.5
    "images/shum3.png"
    pause 0.5
    "images/shum4.png"
    pause 0.5
    "images/shum5.png"
    pause 0.5
    "images/shum6.png"
    pause 0.5
    repeat

image noize:
    "images/shum2.png"
    pause 0.5
    "images/shum3.png"
    pause 0.5
    "images/shum4.png"
    pause 0.5
    "images/shum5.png"
    pause 0.5
    "images/shum6.png"
    pause 0.5
    repeat


screen daytime():
    if dt == "Утро":
        add "#8404"
    if dt == "Вечер":
        add "#0484"
    if dt == "Ночь":
        add "#000b"

#Здесь начинается текстовая часть игры
  
label start:

    $ rootz = 0

    #$ config.rollback_enabled = False

    stop music

    stop audio

    stop sound
    
    scene black
    with fade

    k "Так, всё совпадает, можете проходить, удачной поездки."

    "С этими словами кондуктор протягивает мои документы и билет."

    "Засунув всё в карман, я взял ручку чемодана и прошёл в вагон."

    #Дневной фон

    play music "audio/Warmth.wav" volume 0.6 

    scene train corridor day
    with fade

    "Перед моими глазами возник коридор поезда."

    "Спеша к своему месту, я пытался разглядеть всех пассажиров и вид из окна."

    "Довольно редко мне выдаётся возможность сбежать из городской суеты и насладится такой банальной вещью как отдых." 

    "Заглядывая в купе, можно было увидеть отдельные мирки."

    "Копошащиеся семьи, которые пытаются быстро разобрать свои вещи."

    "Одиночки, уже залезшие на верхние полки."

    "Плачущие дети и их родители, пытающиеся успокоить своё чадо."

    "Удивительная атмосфера."

    "Разглядывая пассажиров и пейзажи за окном, я и не заметил, как подошёл к своему купе."

    "Поставив перед собой небольшой чемодан, я открыл дверь и вошёл."

    play audio "audio/slidedoor.wav"
    
    #Дневной фон

    scene black

    show forest_background:
        ypos 150

    show train coupe day
    with fade

    "Купе было пустое."

    "Затащив чемодан внутрь, я задвинул дверь и присел."
    
    "За окном вокзал, но совсем скоро поезд тронется и можно будет увидеть умопомрачительные виды, далёкие деревни и невероятных размеров поля."

    "Озёра, реки или пасущийся скот."
    
    "Каждая картина за окном шедевральна."

    "Встав, я приподнял свою полку и ногой толкнул туда чемодан."

    "Опустив и зафиксировав полку, я для верности присел на неё."

    r "Фух!"

    "Достав телефон из кармана брюк, я посмотрел на время.{p}Через две минуты поезд должен тронуться."

    "Телефон я решил выключить."

    "Не хочу во время поездки отвлекаться на сообщения с работы или другие уведомления."

    "Отпуск всё-таки нужен чтобы отдохнуть от рабочей рутины и насладиться свободой действий."

    "Поезд тронулся."

    "Оттолкнувшись назад поезд спустя пару секунд двинулся вперёд."

    scene black

    $ _scroll("forest_background", None, 1.35)

    show train coupe day

    play sound "audio/intrain.wav" volume 0.4 loop

    "Чучух-чучух."

    "Звук колёс стучащий по рельсам и пошатывание вагона.{p}Идеальное сочетание."

    "Постепенно за окном, город начинает растворятся, переходя в различные композиции, сменяющиеся ежесекундно."

    "Поезд уже едет пару минут, но я до сих пор один в купе."

    "Надо насладиться возможностью."

    "Я взял упаковку с пастельным бельём, застелил полку и лёг на неё."

    "Стук колёс начинает перерастать в колыбельную песенку."

    scene black
    with eye_shut
    $ renpy.pause(1.0, hard=True)

    "Не имея ни малейшего желания сопротивляться этой музыке, в полном умиротворении я задремал."

    "Настолько спокойно на душе и в голове, что даже мысли не появляются."

    "Чучух-чучух..."

    window hide dissolve

    $ renpy.pause(6.0, hard=True)

    window show dissolve

    jump girl_enter

label girl_enter:

    play audio "audio/slidedoor.wav"

    "Дверь открылась?"

    #Вечерний фон

    scene black

    show train coupe night
    with eye_open

    $ _scroll("forest_background", None, 1.35)

    hide train coupe night

    

    show train coupe night

    "В купе вошла девушка."

    show ulya normal at center:
        zoom 0.6
    with dissolve

    r "Здравствуйте."

    "Спросонья сказал я тихим голосом."

    u "Здравствуйте, я Юля."

    r "Я Рома."
    
    $ renpy.pause(0.5, hard=True)

    show ulya smile at center:
        zoom 0.6
    with dissolve

    rau "Приятно познакомиться!"

    "Хех. Одновременно."

    "Я встал, взял полотенце и пошёл в уборную."

    $ _hide("forest_background", None)

    #Вечерний фон

    scene train corridor night
    with fade

    "Все купе закрыты."

    "Кажется я проспал остановку.{w} Обидно."

    "Я быстро умылся, вытерся и пошёл обратно."

    #Вечерний фон

    play audio "audio/slidedoor.wav"

    scene black

    show train coupe night
    with fade

    $ _scroll("forest_background", None, 1.35)
    
    hide train coupe night

    show train coupe night

    "Подойдя к своему купе я открыл дверь и зашёл."

    "Купе было пустое."

    "Я закрыл дверь"

    play audio "audio/slidedoor.wav"

    "Странно, наверное, девушка ошиблась и вошла не в то купе."

    "Я сел на полку и посмотрел в окно, красота."

    "Из соседнего купе доносился тихий плачь."

    "Странно, минуту назад всё было тихо."

    "Кроме плача из соседнего купе не исходило ни одного звука."

    "Оставили ребёнка одного и ушли?"

    jump strange



label strange:

    "Мне стало не по себе, и я решил проверить что там происходит."

    $ _hide("forest_background", None)

    scene train corridor night
    with fade

    play audio "audio/doorknock.wav"

    "Я подошёл к купе откуда исходил звук и постучал."

    r "Извините, можно войти!?"

    "Никто мне не ответил, однако плачь не прекращался.{p}Я открываю купе."

    play audio "audio/slidedoor.wav"

    play music "audio/Magical Forest.wav" volume 0.8 fadein 3.0

    stop sound fadeout 2.0

    scene forest
    with fade

    "Подвинув дверь, перед собой я увидел лес."

    "Прямо перед глазами сидя на корточках, посреди леса, плакала девушка, которая зашла ко мне в купе, Юля."

    r "Юля!"

    "Крикнул я и побежал в её сторону."

    show ulya cry at center:
        zoom 0.6
    with dissolve

    "Юля обернулась, когда я почти добежал до неё."

    u "Рома! Где ты был!?"

    "Юля кинулась ко мне и обняла."

    r "Где я был?"

    u "Мы тут гуляли, и ты внезапно пропал. Я испугалась, не шути так больше."

    u "Пошли быстрее, а то поезд уедет!"

    hide ulya cry
    with dissolve

    "Юля взяла меня за руку, и мы стремительным шагом пошли к вокзалу."

    "Ничего не понимаю."

    u "Ты можешь идти быстрее!? Мне холодно."

    stop music fadeout 3.0

    play music "audio/Warmth.wav" volume 0.6 fadein 3.0

    "Я ускорил шаг и вскоре мы вышли к платформе и забежали в поезд."

    scene train corridor night
    with fade

    k "Вы где пропадали!? Поезд с минуты на минуту тронется, заходите быстрее."

    "Юля тянет меня в купе, но я остановился."

    r "Юля, почему мы были в лесу, вдвоём?"

    show ulya cry at center:
        zoom 0.6
    with dissolve

    u "Что значит почему? Мы же вышли на остановке и решили прогуляться в лесу."

    u "Ты сам сказал, что в лесу тебе находится нравиться больше, чем на платформе."

    r "Я сказал?{w} Мы же с тобой даже не разговаривали."

    u "В смысле не разговаривали?"

    u "Мы ехали в одном купе несколько часов и разговорились."

    u "Ты рассказал, что природу любишь, то что ты в офисе работаешь."

    u "Пошли быстрее в купе, там поговорим."

    "Я всё забыл?"

    "Юля тянула меня внуть купе, я не стал сопротивляться."

    scene polyana
    with fade

    stop music fadeout 3.0

    play music "audio/High End Party.wav" volume 0.6 fadein 3.0

    "Зайдя внуть, я оказался на поляне с Юлей."

    "Чего?"

    show ulya normal at center:
        zoom 0.6
    with dissolve

    u "Ты чего остановился?"

    u "Поднимайся быстрее я уже коврик постелила."

    scene polyana kover
    with fade

    show ulya smile at center:
        zoom 0.6
    with dissolve

    u "Приятного аппетита!"

    r "Приятного аппетита..."

    hide ulya
    with dissolve

    "Я ничего не понимаю."

    "Сначала лес.{w} Теперь поляна."

    scene black
    with eye_shut

    $ renpy.pause(1.0, hard=True)

    scene funeral
    with eye_open

    play music "audio/Forever Lost.wav" volume 0.6 fadein 3.0

    "Снова?"

    "Теперь чьи-то похороны."

    #В идеале тут должен быть спрайт Юли в чёрном платье на похоры.

    show ulya dress normal at center:
        zoom 0.6
    with dissolve

    u "Рома, не переживай."

    u "Всё будет хорошо, главное не сдаваться."

    "Ага."

    hide ulya dress normal
    with dissolve

    "Я развернулся и пошёл."

    scene funeral train
    with fade

    "Ходя по кладбищу я вышел к вагону."

    "Вагон на кладбище?{w} Я сам в шоке."

    "Я подошёл поближе."

    "Рядом с вагоном стоит табличка."

    "Поезд «Воспоминания»."

    "Правило первое: Для работы поезда необходимо пристегнуться."

    "Правило второе: Во время поездки никогда не открывайте глаза."

    "Ну давай попробуем, всё равно я уже в богом забытом месте."

    "Внутри как обычный поезд, только вагону будто тысяча с копейками лет."

    "Я сел на первое же сиденье в вагоне, пристегнулся и закрыл глаза."

    scene black
    with eye_shut

    $ renpy.pause(2.0, hard=True)

    "Н-н-а-ча-ло тр-р-р-я-сти." with sshake

    jump memory_train_first

label memory_train_first:

    window hide dissolve

    $ renpy.pause(2.5, hard=True)

    window show dissolve

    play sound "audio/intrain.wav" loop volume 0.4 fadein 3.0

    play music "audio/Warmth.wav" volume 0.6 fadein 3.0

    play audio "audio/slidedoor.wav"

    "Дверь открылась?"

    #Вечерний фон

    scene black

    show train coupe night
    with eye_open

    $ _scroll("forest_background", None, 1.35)

    hide train coupe night

    show train coupe night

    "В купе вошла девушка."

    show ulya normal at center:
        zoom 0.6
    with dissolve

    r "Здравствуйте."

    "Спросонья сказал я тихим голосом."

    u "Здравствуйте, я Юля."

    r "Я Рома."
    
    $ renpy.pause(1.0, hard=True)

    rau "Приятно познакомиться!"

    show ulya smile at center:
        zoom 0.6
    with dissolve

    "Хех. Одновременно."

    "Я встал, взял полотенце и пошёл в уборную."

    $ _hide("forest_background", None)

    #Вечерний фон
    #Можно придумать анимацию в коридоре

    scene train corridor night
    with fade

    "Все купе закрыты."

    "И кажется я проспал остановку.{w} Обидно."

    "Я быстро умылся, вытерся и пошёл обратно."

    #Вечерний фон

    scene black

    show train coupe night
    with fade

    $ _scroll("forest_background", None, 1.35)
    
    hide train coupe night

    show train coupe night

    pause(0.3)

    show ulya normal at center:
        zoom 0.6
    with dissolve

    u "О вы вернулись, можете помочь пожалуйста?"

    r "Да, сейчас."

    "Я взял её сумку и положил на верхнюю полку, она всё равно пока не занята."
    
    u "Спасибо."

    hide ulya normal
    with dissolve

    "Я присел около окна."

    "Вечерние виды завораживают."

    "Юля закончила застилать полку и тоже села рядом с окном."

    show ulya normal at right:
        zoom 0.6
    with dissolve

    u "Вам так нравиться смотреть в окно?"

    r "Можешь на ты.{w} Да нравиться."

    r "Я довольно редко выезжаю за город, так что для меня это всегда в новинку."

    u "А мне как-то скучно смотреть."

    r "Каждому своё, мне очень интересно смотреть на формы пролетающих мимо зданий, на узоры, которые создают своими листьями деревья."

    r "Смотреть на полёт птиц, собравшихся в стаю, на цвета проезжающих автомобилей."

    r "Простые вещи, однако настолько красивые."

    show ulya smile at right:
        zoom 0.6
    with dissolve

    "Юля посмотрела в окно и слегка улыбнулась."

    u "Ты, наверное, творческий человек, раз видишь столько хорошего в обычном окне поезда."

    r "Хех. Не угадала, я всего-то офисный работник."

    r "Пишу отчёты, печатаю отчёты, сдаю отчёты."

    r "Думать о творчестве даже времени не остаётся."

    r "После рабочего дня, бывает настолько устаёшь, что даже поесть не можешь, сразу спать ложишься."
    
    show ulya wonder at right:
        zoom 0.6
    with dissolve
    
    u "Это так тяжело?"

    r "Работа не сложная, но скучная."

    r "Она монотонная, я просто переношу данные из компьютера на бумагу, в течении всего рабочего дня."

    r "Иногда не успеваешь всё доделать вовремя и приходится оставаться в офисе до поздна, а иногда даже и спать там. "

    r "И в общем такая на первый взгяд лёгкая работа, может доставить немерено хлопот."

    show ulya normal at right:
        zoom 0.6
    with dissolve

    u "А что тебя держит на такой плохой работе?"

    "Действительно, что меня там держит?"

    r "У меня не плохие коллеги, я с ними хорошо сдружился."

    r "Корпоративы каждый квартал.{w} В конце рабочей недели все вместе ходим в ресторан."

    r "Думаю ради хорошего коллектива и не плохой зарплаты я могу продолжать работать в таком месте."

    show ulya wonder at right:
        zoom 0.6
    with dissolve

    u "Понятно. Я вот ездила на подработку в город."

    u "Живу я в деревне, там вообще негде работать."

    u "Поэтому пришлось искать работу в ближайших городах."

    u "Нашла вакансию официантки, созвонилась и поехала."

    show ulya smile at right:
        zoom 0.6
    with dissolve

    u "Коллектив у меня тоже классный был."

    u "Директор нам банкеты устраивал на каждый праздник."

    u "Даже жалко, что уезжаю."

    r "А почему не осталась?"

    show ulya normal at right:
        zoom 0.6
    with dissolve

    u "Мама жаловаться начала, что ей сложно одной в огороде работать, да и соскучилась по мне."

    "Поезд начал тормозить."

    stop sound fadeout 10.0

    r "Не хочешь выйти на остановке?"

    u "Почему бы и нет."

    $ _hide("forest_background", None)

    scene train corridor night
    with fade

    show ulya normal at center:
        zoom 0.6
    with dissolve

    r "Не хочешь погулять по лесу?"

    show ulya wonder at center:
        zoom 0.6
    with dissolve

    u "Я не против, но мы на поезд не опоздаем?"

    r "Остановка больше получаса, так что успеем."

    u "Хорошо."

    scene forest
    with fade

    "Выйдя на платформу мы сразу же спустились с неё и пошли в лес."

    show ulya normal at center:
        zoom 0.6
    with dissolve

    stop music fadeout 3.0

    play music "audio/Magical Forest.wav" volume 0.6 fadein 3.0

    "Я взял Юлю за руку, она слегка дрожала от холода."

    r "Ну как тебе?"

    u "Красиво, только холодно немного."

    hide ulya normal
    with dissolve

    "Пройдя в глубь леса, Юля отпустила мою руку."

    "Она пробежала вперёд и начала звать меня."

    u "Рома!{w} Рома! Ты где!?"

    "Она села на корточки и заплакала."

    r "Юля!"

    "Крикнул я и побежал в её сторону."

    show ulya cry at center:
        zoom 0.6
    with dissolve

    "Юля обернулась, когда я почти добежал до неё."

    u "Рома! Где ты был!?"

    "Юля кинулась ко мне и обняла."

    r "Где я был?"

    u "Мы тут гуляли, и ты внезапно пропал. Я испугалась, не шути так больше."

    u "Пошли быстрее, а то поезд уедет!"

    hide ulya cry
    with dissolve

    "Юля взяла меня за руку и мы стремительным шагом пошли к вокзалу."

    u "Ты можешь идти быстрее!? Мне холодно."

    stop music fadeout 3.0

    play music "audio/Warmth.wav" volume 0.6 fadein 3.0

    scene train corridor night
    with fade

    "Мы быстро забежали в поезд и пошли к своему купе."

    k "Вы где пропадали!? Поезд с минуты на минуту тронется."

    $ renpy.pause(1.0, hard=True)

    scene black

    show train coupe night
    with eye_open

    $ _scroll("forest_background", None, 1.35)

    hide train coupe night

    show train coupe night

    pause(0.3)

    show ulya cry at right:
        zoom 0.6
    with dissolve

    u "Что случилось, куда ты делся в лесу?"

    r "Я не поминаю о чём ты говоришь. Ты отпустила мою руку и пошла впёред."

    u "Это не правда! Ты будто бы исчез, а потом появился..."

    show ulya wonder at right:
        zoom 0.6
    with dissolve

    show ulya wonder at left:
        zoom 0.6
    with dissolve

    "Юля пересела на мою полку и положила голову мне на плечо."

    u "Ладно. Главное, что сейчас всё хорошо..."
    
    scene black
    with fade

    menu:

        "Может открыть глаза?"

        "Держать закрытыми.":
            $ renpy.pause(2.0, hard=True)

            "Сн-н-н-о-в-а-а тр-р-р-ясё-т-т." with sshake

            jump memory_train_second

        "Открыть.":
            $ rootz += 1
            
            scene black
            with eye_open

            $ _scroll("stars", fade, 5)

            "Что это?"

            "Ладно, просто закрою глаза."
            
            $_hide("stars",None)

            scene black
            with eye_shut

            $ renpy.pause(2.0, hard=True)

            "Сн-н-н-о-в-а-а тр-р-р-ясё-т-т." with sshake

            jump memory_train_second

    


label memory_train_second:

    stop music fadeout 3.0

    play music "audio/High End Party.wav" volume 0.6 fadein 3.0

    scene polyana
    with fade

    show ulya normal at center:
        zoom 0.6
    with dissolve

    u "Ты чего остановился?"

    u "Поднимайся быстрее я уже коврик постелила."

    scene polyana kover
    with fade

    "Поднявшись на холм я присел на коврик."

    "Юля доставала из корзинки всякие вкусности, которые приготовила к сегодняшнему дню."

    "Бутерброды, печенья, тортик и чай в термосах."

    "Юля протянула мне тарелку со сладостями."

    "А потом налила чай в стаканчик и поставила рядом с моей тарелкой."

    u "Приятного аппетита!"

    r "Приятного аппетита."

    "Мы начали кушать, и Юля отрезав кусочек торта и насадив его на вилку, протянула мне."

    u "Открой рот."

    "Я послушавшись, открыл рот."

    "Стянув кусочек торта с вилки, я распробовал его вкус."

    r "Вкусно!"

    "«С радостью, будто бы ребёнок, впервые увидевший радугу.», - заявил я."

    "Мы делились вкусностями друг с другом, пока наши тарелки не стали пустыми."

    "Убрав за собой, мы решили прогуляться по поляне."

    scene polyana
    with fade

    show ulya smile at center:
        zoom 0.6
    with dissolve

    "Вокруг бегали дети, запускающие воздушного змея."

    "А их родители просто лежали и загорали."

    "Парочки, которые прямо как мы, сладко проводят время."

    "Рядом с нами прошёл мужчина, выгуливавший собаку."

    u "Ух ты! А можно погладить вашего пёсика?"

    "Мужчина обернулся, и одобрительно помахал головой."

    hide ulya smile
    with dissolve

    "Юля подбежала к собаке, погладила пару раз за ушами, и провела рукой по спине."

    u "Спасибо!"

    show ulya smile at center:
        zoom 0.6
    with dissolve

    "Юля вернулась ко мне и мы продолжили прогулку."

    show ulya wonder at center:
        zoom 0.6
    with dissolve

    u "Слушай, мне так понравилась собачка, может мы тоже себе заведём?"

    "Умоляющим взглядом смотря на меня, сказала Юля."

    r "Почему бы и нет."

    show ulya smile at center:
        zoom 0.6
    with dissolve

    "На лице Юли появилась улыбка."

    u "Смотри! Пошли сядем."

    "Сказала Юля, показывая пальцем на беседку."

    "Зайдя в беседку мы сели на скамейку."

    "Юля положила голову мне на плечо."

    u "Как же с тобой хорошо..."

    scene black
    with fade

    menu:

        "Может открыть глаза?"

        "Держать закрытыми.":
            $ renpy.pause(2.0, hard=True)

            "Т-рр-р-р-р--р-ря-с-с-ка." with sshake

            jump memory_train_third

        "Открыть.":
            scene black

            if rootz == 1:
                $ _scroll("stars", fade, 5)

                "Снова?"

                "Окей, я просто как и в прошлый раз, закрою глаза."
            else:
                $ _scroll("stars", fade, 5)

                "Что это?"

                "Ладно, просто закрою глаза."

            $_hide("stars",None)

            scene black
            with eye_shut
            
            $ renpy.pause(2.0, hard=True)

            $ rootz += 1

            "Т-рр-р-р-р--р-ря-с-с-ка.." with sshake

            jump memory_train_third

label memory_train_third:

    play music "audio/Forever Lost.wav" volume 0.6 fadein 3.0

    scene funeral
    with fade

    show ulya dress normal at center:
        zoom 0.6
    with dissolve

    u "Рома, не переживай."

    u "Всё будет хорошо, главное не сдаваться."

    "Вытирая слезы, сказала Юля."

    r "Я понимаю..."

    r "Но..."

    u "Всё хорошо, я с тобой."

    "Я заплакал."

    u "Ничего страшного, не скрывай эмоции."

    "Сквозь слезы, говорила Юля, пытаясь меня подбодрить."

    hide ulya dress
    with dissolve

    "Я подошёл к гробу, в котором лежала моя мама."

    "Наклонившись, я поцеловал её хладное тело в лоб."

    "Не найдя в себе сил стоять, я упал на колени и зарыдал."

    "Потеряв настолько близкого человека, я наверное, не найду в себе сил жить дальше."

    "Ко мне подбежала Юля и посмотрела мне в глаза."

    show ulya dress cry at center:
        zoom 0.6
    with dissolve

    u "Пожалуйста..."

    u "Прошу тебя..."

    u "Не плачь..."

    "Юля, захлёбываясь в слезах, умоляла меня найти в себе силы."

    "Думая я осознал. У меня есть ещё один близкий человек ради которого стоит жить."

    hide ulya dress
    with dissolve

    "Юля положила голову мне на плечо."

    u "Я люблю тебя, Рома..."

    "Прошептала мне Юля, и заплакала ещё сильнее."

    r "Я тоже, люблю тебя."

    scene black
    with fade

    stop music fadeout 3.0

    $ renpy.pause(2.0, hard=True)

    "Тр-р-р-р-яск-к-а-а-а-а-а." with sshake

    if rootz == 0:
        jump trueend
    
    if rootz > 0:
        jump bad

label trueend:

    play music "audio/Warmth.wav" volume 0.6 fadein 3.0

    play sound "audio/intrain.wav" loop volume 0.4

    scene black

    show train coupe day
    with eye_open

    $ _scroll("forest_background", None, 8)

    hide train coupe day

    show train coupe day

    pause(0.3)

    show ulya smile at center:
        zoom 0.6
    with dissolve

    u "Просыпайся, мы приехали."

    r "Юля...{w} А у тебя волосы, кажется длиннее стали."

    show ulya normal at center:
        zoom 0.6
    with dissolve

    u "Несешь спросонья всякий бред, неужели так крепко заснул?"

    r "Мне приснился очень реалистичный и красочный сон...{p}Вот только..."

    r "Я уже не помню про что..."

    show ulya wonder at center:
        zoom 0.6
    with dissolve

    u "Что случилось?"

    u "Почему ты плачешь?"

    r "А?{w} Ой."

    stop sound fadeout 10.0

    hide ulya wonder
    with dissolve

    scene forest_background:
        ypos 150

    show train coupe day
    with None

    $ _hide("forest_background", None)

    "Поезд остановился и мы вышли на вокзал."

    scene black
    with fade

    u "Доехали..."

    stop music fadeout 3.0

    jump creditz

    



label bad:

    play music "audio/Dead Planet.wav" volume 0.6 fadein 3.0

    scene shum:
        ypos 150

    show noize:
        ypos 150

    show noise at Glitch(_fps=1., color_range1="000", color_range2="000"):
        ypos 150


    show train coupe night
    with fade

    show ulya normal glitch at center:
        zoom 0.6
    with dissolve
    
    u "Пожалуйста..."

    u "Забудь..."

    u "Меня..."

    u "Не существует..."

    hide ulya normal
    with dissolve

    scene black

    show train coupe night at Glitch(_fps=3.)

    $ _scroll("stars", fade, 5)

    hide train coupe night

    show train coupe night at Glitch(_fps=3.)

    r "Стой!"

    "Всё перед моими глазами исказилось, а Юля исчезла."

    show train corridor night at Glitch(_fps=3.)

    $ _scroll("stars", fade, 5)

    hide train corridor

    show train corridor night at Glitch(_fps=3.)

    "Я выбежал в коридор, однако он тоже искажён."

    if rootz == 2:
        "Почему?"

        "Что случилось?"

        "Я решил вернуться в купе."

        jump ulya_death

    scene black

    show train coupe night
    with eye_open

    $ _scroll("forest_background", None, 1.35)
    
    hide train coupe night

    show train coupe night

    "Какой-то странный сон."

    "Пойду заварю себе лапшу."

    jump creditz



label ulya_death:

    scene funeral
    with fade

    "Похороны?"

    "Я снова в своих воспоминаниях?"

    "Оглядываясь вокруг я нигде не видел Юлю."

    "Опустив взгляд, я увидел памятник на могиле моей мамы."

    "Я присел, чтобы разглядеть его."

    window hide dissolve

    scene black
    with fade

    show text "{color=#fff}Юля{p}19XX-20XX{/color}"

    $ renpy.pause(3.0, hard=True)

    jump creditz

init:
    transform txt_up:
        yalign 5.0
        linear 15.0 yalign -3.5

label creditz:

    stop music

    stop sound

    stop audio

    window hide dissolve

    scene black with dissolve

    show text "{color=#fff}{b}Идея{/b}{p}Onf1r{p}{p}{b}Сценарий{/b}{p}Onf1r{p}{p}{b}Программирование{/b}{p}Onf1r{p}{p}{b}Художники{/b}{p}proch'{p}GregV{p}Alexander Aveysky{p}{p}{b}Музыка и звуки{/b}{p}Jhaeka{p}Osabisi{p}{p}{p}{p}{b}Спасибо за игру!{/b}{/color}" at txt_up

    $ renpy.pause(16.0, hard=True)

    return

