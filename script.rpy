init python:
  def eyewarp(x):
    return x**1.33
  eye_open = ImageDissolve("eye.png", .8, ramplen=128, reverse=False, time_warp=eyewarp)
  eye_shut = ImageDissolve("eye.png", .8, ramplen=128, reverse=True, time_warp=eyewarp)
image black:
  Solid("#000")
image white:
  Solid("#FFF")

# Определение персонажей игры.
define r = Character('Рома', color="#c8ffc8")
define u = Character('Юля', color="#c8ffc8")
define rau = Character('Рома и Юля', color="#c8ffc8")

init:
    image sky = "images/sky.jpg"
    transform scroll_in(delay = 10.0):
        xpos config.screen_width xzoom 1.0
        linear delay xpos 0
        pause delay
        repeat
    transform scroll_in2(delay = 10.0):
        xpos config.screen_width
        pause delay
        linear delay xpos 0
        repeat
    transform scroll_out(delay = 10.0):
        xpos 0
        linear delay xpos -config.screen_width
        pause delay
        repeat
    transform scroll_out2(delay = 10.0):
        xpos config.screen_width
        pause delay
        xpos 0 xzoom 1.0
        linear delay xpos -config.screen_width
        repeat
    transform left_to_right:
        xalign -1.5
        linear 2.0 xalign 1.5 
        repeat


init python:
    def _scroll(img, effect = None, delay = 10.0):
        renpy.show(img + "1", what = ImageReference(img), at_list = [scroll_in(delay)])
        renpy.show(img + "2", what = ImageReference(img), at_list = [scroll_out(delay)])
        renpy.show(img + "3", what = ImageReference(img), at_list = [scroll_in2(delay)])
        renpy.show(img + "4", what = ImageReference(img), at_list = [scroll_out2(delay)])
        renpy.with_statement(effect)



#Здесь начинается текстовая часть игры
  
label start:

    screen daytime:
        if dt == "Утро":
            add "#8404"
        if dt == "Вечер":
            add "#0484"
        if dt == "Ночь":
            add "#000b"

    stop music

    stop audio

    #$ _scroll("sky", Dissolve(2.0), 15)
    #pause
    
    scene black
    with fade

    "Я вошёл в поезд."

    "Открыл дверь необходимого мне вагона и прошёл дальше."

    #Дневной фон

    scene train corridor
    #with fade

    "Перед моими глазами возник коридор поезда."

    "Спеша к своему месту, я пытался разглядеть всех пассажиров и вид из окна."

    "Довольно редко мне выдаётся возможность сбежать из городской суеты и насладится такой банальной вещью как отдых." 

    "Заглядывая в купе, можно было увидить отдельные мирки."

    "Копошащиеся семьи, которые пытаются быстро разобрать свои вещи."

    "Одиночки, уже залезшие на верхние полки."

    "Плачущие дети и их родители, пытающиеся успокоить своё чадо."

    "Удивительная атмосфера."

    "Разглядывая пассажиров и пейзажи за окном, я и не заметил как подошёл к своему купе."

    "Поставив перед собой небольшой чемодан, я открыл дверь."
    
    #Дневной фон

    show train coupe
    
    "Купе было пустое."

    "Затащив чемодан внутрь, я задвинул дверь и присел."

    "За окном вокзал, но совсем скоро поезд тронется и можно будет увидеть умопомрачительные виды, далёкие деревни и невероятных размеров поля."

    "Озёра, реки или пасущийся скот."
    
    "Каждая картина за окном шедевральна."

    "Встав, я приподнял свою полку и ногой толкнул туда чемодан."

    "Опустив и зафиксировав полку я для верности присел на неё."

    r "Фух!"

    "Достав телефон из кармана брюк, я посмотрел на время.{p}Через две минуты поезд должен тронуться."

    "Телефон я решил выключить."

    "Не хочу во время заслуженного отпуска отвлекаться на чёртову работу."

    "Наверно для этого и создан отпуск."

    "Наслаждаться свободой действий и ничем не встревоженной головой."

    "Поезд тронулся."

    "Оттолкнувшись назад поезд спустя пару секунд двинулся вперёд."

    scene sky at left_to_right:
        ypos 250

    show train coupe

    play audio [ "audio/intrain.wav" ] loop fadeout 5.0 fadein 5.0

    "Чучух-чучух."

    "Звук колёс стучащий по рельсам и пошатывание вагона.{p}Идеальное сочетание."

    "Постепенно за окном, город начинает растворятся, переходя в различные композиции, сменяющиеся ежесекундно."

    "Поезд уже едет пару минут, но я до сих пор один в купе."

    "Надо насладиться возможностью."

    "Я взял упаковку с пастельным бельём, застелил полку и лёг на неё."

    "Стук колёс начинает переростать в колыбельную песенку."

    scene black
    with eye_shut
    $ renpy.pause(1.0, hard=True)

    "Не имея ни малейшего желания сопротивляться этой музыке, в полном умиротворении я задремал."

    "Настолько спокойно на душе и в голове, что даже мысли не появляются."

    "Чучух-чучух..."

    window hide dissolve

    $ renpy.pause(6.0, hard=True)

    window show dissolve

    "Дверь открылась?"

    #Вечерний фон

    scene sky at left_to_right:
        ypos 250

    show train coupe
    with eye_open

    "В купе вошла девушка."

    r "Здравствуйте."

    "С просони сказал я тихим голосом."

    u "Здравствуйте, я Юля."

    r "Я Рома."
    
    $ renpy.pause(1.0, hard=True)

    rau "Приятно познакомиться!"

    "Хех. Одновременно."

    "Я встал, взял полотенце и пошёл в уборную."

    #Вечерний фон
    #Можно придумать анимацию в коридоре

    show train corridor
    #with fade

    "Все купе закрыты."

    "Часы показывали 18:12."

    "И кажется я проспал остановку.{w} Обидно."

    "Я быстро умылся, вытерся и пошёл обратно."

    #Вечерний фон


    scene sky at left_to_right:
        ypos 250

    show train coupe
    #with fade
    u "О вы вернулись, помогите пожалуйста, а то сумка тяжёлая."

    r "Да, сейчас."

    "Я взял её сумку и положил на верхнюю полку, она всё равно пока не занята."
    
    u "Спасибо."

    "Я присел около окна."

    "Вечерние виды завораживают."

    "Юля закончила застилать полку и тоже села рядом с окном."

    u "Вам так нравиться смотреть в окно?"

    r "Можешь на ты.{w} Да нравиться."

    r "Я довольно редко выезжаю за город, так что для меня это всегда в новинку."

    u "А мне как-то скучно смотреть, оно всё однообразное что-ли."

    r "В этом и состоит красота природы."

    ""


    "Желая лечь по удобнее, я повернулся на бок."
    
    
    "И закрыл глаза."

    "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    play audio [ "audio/intrain.wav" ] loop fadeout 5.0 fadein 5.0


    scene sky at left_to_right:
        ypos 250

    show train coupe

    with eye_open
    "Awake"


    stop music
    stop audio
    return

