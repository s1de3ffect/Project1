# Вы можете расположить сценарий своей игры в этом файле.
label splashscreen:
    $ renpy.movie_cutscene("films/cutscene.ogv")
    return

# Игра начинается здесь:s
label start:
    
    $ username = renpy.input("Введите ваше имя: ", default = "Саша")
    play music "music/startmusic.mp3" fadein 0.5 fadeout 2.0
    scene schoolpark
    "Три часа дня. Закончились уроки, и я как обычно направлялся домой."
    "Это такой же обычный день как и всегда..."
    "Каждый раз приходишь в школу, надеясь что получишь хорошую оценку"
    "А получаешь только от родителей, когда они узнают что я не взял участия в каком-то ненужном мероприятии"
    "Сняв портфель с плеча, я поставил его на лавочку, чтобы достать воду"
    "Как вдруг..."
    unknown "Хееей!"
    user "..."
    "Это был знакомый женский голос."
    "Но что ей от меня надо?"
    unknown "Еееееееей-й! Постой!"
    unknown "Да остановись ты уже!"
    scene schoolmain with dissolve
    show melissa with dissolve
    melissa "Да что с тобой?!"
    user "..."
    "Мелисса стояла прямо перед мной и смотрела своими яркими зажжёными глазами"
    "Мелисса - моя одноклассница."
    "Но на самом деле мы не очень-то и общяемся"
    melissa "Ты же обещал, что мы пойдем домой вместе!"
    user "Извини, давай не сегодня."
    "Да, я обещал ей это. Но только потому что она мне все уши прожужжала"
    melissa "Ну пожалуйста, мне скучно одной идти..."
    menu: 
        "Принять ее предложение":
            user "*Вздох*"
            user "Хорошо, пошли уже."
            hide melissa
            show melissa_happy
            melissa "УРААА!"
            melissa "[username], я тебе щас такое расскажу!"
        "Отказаться": 
            user "Прости, мне нужно зайти в одно место."
            hide melissa
            show melissa_sad
            "На самом деле мне никуда не надо, просто я хочу пойти домой один."
            melissa "Так поступать некрасиво! Ты говорил пойдешь со мной." 
            hide melissa_sad
            show melissa
            melissa "Я решила. Я пойду с тобой!"
    scene black_bg with fade 
    play sound "soundeffects/steps_ground.mp3" fadeout 2.0 volume 0.8
    play music "soundeffects/birds.mp3"
    scene schoolpark with fade 
    pause 1.5           
    scene sp_side with fade
    show melissa_r with dissolve
    stop sound
    melissa "..."
    user "..."
    melissa "........"
    melissa "А куда мы вообще идём?"
    user "А..."
    user "Насчет этого..."
    user "Я соврал." 
    hide melissa_r
    show melissa_surprised
    melissa "Всмысле?"
    user "На самом деле мне никуда не нужно."
    melissa "Но почему..."
    user "Что?"
    hide melissa_surprised
    show melissa_sad
    melissa "Почему ты соврал мне?"
    "Ну вот и приплыли."
    user "Мне..."
    user "Мне просто не нравится проводить время в компании. {w} Не люблю я эту всю суету."
    user "Вот и сегодня хотелось бы побыть одному."
    hide melissa_sad
    show melissa_r
    melissa "Как я тебя понимаю."
    melissa "Однако, мне в отличии от тебя, нравится проводить время с людьми"
    melissa "Я уже достаточно давно хожу домой сама. {w} И я так подумала..."
    melissa "Что мне не помешал бы кто-то, с кем бы я могла пообщаться по пути домой."
    "Мне как-то не удобно это спрашивать, но всё же."
    user "А почему ты выбрала именно меня? {w} Я ведь не такой общительный как остальные ребята в классе."
    melissa "Я знаю. {w} Но этим я и заинтересовалась." 

    return
