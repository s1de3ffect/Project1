# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define melissa = Character('Мелисса', color="#c8ffc8")
define user = Character( '[username]', color="#c8ffc8")
define unknown = Character('...', color ="#c8ffc8")

image schoolpark:
    "background/school_park.jpeg"
    zoom 0.9
image schoolmain:
    "background/school_main.jpeg"
    zoom 0.9

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

image melissa:
    "Melissa/melissa_def.png"
    zoom 0.7
image melissa_happy:
    "Melissa/melissa_happy.png"
    xpos 0.5
image melissa_sad:
    "Melissa/melissa_sad.png"
    zoom 0.6

label splashscreen:
    scene black with fade
    pause(0.5)
    $ renpy.movie_cutscene("films/logo.ogv")
    return

# Игра начинается здесь:s
label start:
    
    $ username = renpy.input("Введите ваше имя: ")
    play music "music/startmusic.mp3" fadein (0.5)
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
            "На самом деле мне нужен сєкс"
        
                   

    return
