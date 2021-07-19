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
define a = Character('Алексей', color="#c8ffc8")
define u = Character('Юля', color="#c8ffc8")

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
    
    stop music

    #$ _scroll("sky", Dissolve(2.0), 15)
    #pause

    

    
    
    
    scene black
    with fade
    "Я вошёл в поезд."
    scene train corridor
    #with fade
    "Перед глазами появился старый добрый коридор."
    "Копошащиеся семьи, которые пытаются быстро разобрать свои вещи."
    "Одиночки, уже успевшие застелить своё место."
    "Плачущие дети и их родители, пытающиеся успокоить чадо."
    "Особенная атмосфера."
    "Разглядывая пассажиров, я и не заметил как подошёл к своему купе."
    "Поставив перед собой небольшой чемодан, я открыл дверь."
    scene train coupe
    #with fade
    "К моему удивлению купе было пустое."
    "Затащив чемодан внутрь, я задвинул дверь в исходное положение."
    "Приподняв свою нижнюю полку, я ногой толкнул туда чемодан."
    a "Фух!"
    "Опустив полку, с небольшого прыжка я присел на неё для лучшей фиксации."
    "Открыв пакет с постельным бельём, я не смеша застелил полку и прилёг."
    "Достав телефон из кармана брюк, я его сразу же выключил."
    "Не хочу во время заслуженного месяца отпуска отвлекаться на чёртову работу."
    "Наверно для этого и создан отпуск."
    "Желая лечь по удобнее, я повернулся на бок."
    scene black
    with eye_shut
    $ renpy.pause(1.0, hard=True)
    "И закрыл глаза."

    "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    play audio [ "intrain.mp3" ] loop fadeout 5.0 fadein 5.0


    scene train
    with eye_open
    "Awake"


    stop music
    stop audio
    return

