# Сценарий игры
label splashscreen:
    $ renpy.movie_cutscene("films/cutscene.ogv")
    return

# Игра начинается здесь:
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
    "Стоит ли мне обращать на это внимание? {w} Кому я вообще сдался?"
    unknown "Еееееееей-й! Постой!"
    unknown "Да остановись ты уже!"

    scene schoolmain with dissolve
    show melissa with dissolve

    melissa "Да что с тобой?!"
    user "..."
    "Мелисса стояла прямо перед мной и смотрела своими яркими зажжёными солнцем зелёными глазами."
    "Мелисса - моя одноклассница."
    "Но не смотря на это, мы не очень-то и общяемся"
    melissa "Ты же обещал, что мы пойдем домой вместе!"
    user "Извини. Но давай не сегодня."
    "Да, я обещал ей это. {w} Но только потому что она мне все уши прожужжала, стояла над душой каждую перемену и оборачивалась во время уроков смотря мне в глаза, кажый раз напоминая об этом."
    melissa "Ну пожалуйста, мне скучно одной идти..."

    menu: 
        "Принять ее предложение":
            $ acceptGoHome = True # переменная для отображения опциональной фразы
            user "*Вздох*"
            user "Хорошо, пошли уже."

            hide melissa
            show melissa_happy

            melissa "УРААА!"
            melissa "[username], я так рада что хоть кто-нибудь составит мне компанию!"
        "Отказаться": 
            $ acceptGoHome = False # переменная для отображения опциональной фразы
            user "Прости, мне нужно было зайти в одно место после школы."
            "Мне нужно постараться отмазаться любыми способами!"

            hide melissa
            show melissa_sad

            "На самом деле мне никуда не надо, просто я хочу пойти домой один."
            melissa "Так поступать некрасиво! Ты говорил пойдешь со мной." 

            hide melissa_sad
            show melissa
            
            melissa "Знаешь что? Я последую за тобой куда бы ты не пошёл!"
            melissa "Ты обещал, а обещания сдерживать нада! {w} Не убежишь ты за просто так."
            "Блестяще! Она ещё и посоизвольничать решила... {w} Ладно, придется потерпеть, лучшее уже и её не растраивать и себе на будущее нервы сохранить."

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
    "Чёрт, и сразу же самый прекрасный вопрос! {w} Мне тяжело врать, скажу ей как есть."
    user "Насчет этого..."
    user "Я соврал." 

    hide melissa_r
    show melissa_surprised

    melissa "Всмысле, как это соврал?"
    user "На самом деле мне никуда не нужно."
    "Сейчайс ещё рассказывать начнёт, что она мне противна. Нужно же мне быть таким прямолинейным..."
    melissa "Но почему..."
    user "Что?"
    "Ну вот, сейчайс начнётся..."

    hide melissa_surprised
    show melissa_sad

    melissa "Почему ты соврал мне?"
    "Вот и приплыли."
    user "Ну... {w} Мне..."
    user "Мне просто не нравится проводить время в компании. {w} Не люблю я эту всю суету."
    user "Вот и сегодня хотелось бы побыть одному."

    hide melissa_sad
    show melissa_r

    melissa "Как я тебя понимаю."
    melissa "Однако, мне в отличии от тебя, нравится проводить время с людьми."
    melissa "Я уже давненько хожу домой сама. {w} И я так подумала..."
    melissa "Что мне не помешал бы кто-то, с кем бы я могла пообщаться по пути домой."
    "Это как раз то, чего я болся. Только не говорите что она так каждый день за мной ходить будет..."

    hide melissa_r
    show melissa_smile

    melissa "И я совсем случайно заметила, что ты возвращаешься домой той же дорогой, что и я."
    "Мне как-то не удобно это спрашивать, но всё же."

    hide melissa_smile
    show melissa_r

    user "А почему ты выбрала именно меня? {w} Я ведь не такой общительный как остальные ребята в классе. А по этой дороге, уверен, ещё много кто возвращается к себе домой."
    melissa "Да я знаю. {w} Но этим я и заинтересовалась."
    melissa "Знаешь, говорят что тихие люди очень глубокие и интересные в общении. {w} А ещё у них есть много {i}секретов{/i}))"
    "Она что, прямо сейчайс призналась, что я ей нужен только ради моих тайн? Нужно задать ей резкий вопрос!"
    user "Так ты хочешь чтобы я тебе все свои секреты рассказывал?"
    "Блин, та чего же она всё таки хочет, подозрительная какая-то... {w} Сейчайс всё узнаю!"
    melissa "Ха-ха-ха-ха... {w} Да нет же, глупыш. {w} Я же тебе сказала — просто стало как-то скучно возвращаться со школы одной."
    #-------------------------------------------------------------------------
    #scene road_to_house with fade
    melissa "Более того, мы же одноклассники! И почти совсем не общаемся, странно ведь!"

    hide melissa_r
    show melissa_smile

    melissa "Ну а мне хотелось бы дружить со всеми, кого я знаю."

    hide melissa_smile
    show melissa_r
    
    melissa "Ты ещё и сидишь всё время грустный в классе. {w} Может у тебя что-то случилось?"
    "Неужели на меня кто-то и вправду обращает внимание в школе. Мало того это ещё и одноклассница."
    user "Ммм... {w} Уверен, что ничего не произошло, всё как и обычно."
    melissa "Понятненько. {w} Знаешь..."

    hide melissa_r
    show melissa_shy

    melissa "Ты только не подумай что я странная! {w} Я же не такая, правда?"
    "Не такая? {w} Первый раз с ней говорю, а она сразу про всякие секреты спрашивает, конечно странная, ещё как!"
    melissa "Я ведь просто люблю пообщаться! Хочу дружить со всеми!"
    melissa "Знаю, может я иногда перебарщиваю с разговорами, или спрашиваю личные вещи. Прости если сказала что-то не то."
    "Чёрт! {w} Она совсем не такая как я. И даже так, мне тяжело признавать это, но... {w} Она довольна милая..."

    hide melissa_shy
    show melissa_r

    user "Нелегко тебе наверное. Нужно уделять время всем друзьям, помнить даты их рождения, помнить кому что нравится, а что нет."
    melissa "А... {w} Ты знаешь... {w} Хоть я и общительная, но друзей у меня немного."
    melissa "Похоже многим не нравятся такие активные люди как я. {w} А может они уже нашли достаточно друзей, и не хотят иметь ещё больше."
    user "Может и так."
    "Ёлки-палки, складывается впечатление что разговаривает только она."
    "Нужно бы и мне что-то спросить, что-ли..."
    user "Кстати,{w} а вот чем ты обычно занимаешься, когда приходишь домой?"
    
    hide melissa_r
    show melissa_surprised

    melissa "Я? {w} Нуу... {w} Я... {w} Я отцу по дому помогаю! Он у меня работящий, но мало что успевает довести до конца."
    melissa "Вот..."
    user "А мама? Ты ведь и ей наверное помогаешь, не так ли?"
    "Похоже она как и все девочки, старается делать все дела по дому и помогать всем со всем."

    hide melissa_surprised
    show melissa_worry

    melissa "Мама? {w} Ах да, точно! {w} Ты прав! Я и ей помогаю, конечно!"
    "Что это бы.."
    # ТУТ БУДЕТ ПРИКОЛЬНО ДОБАВИТЬ АВТОПЕРЕКЛЮЧЕНИЯ ТЕКСТА НА СЛЕДУЮЩИЙ, ТИПА ОНА СБИЛА НАС С МЫСЛЕЙ

    #scene mc_house with fade

    hide melissa_surprised
    show melissa

    melissa "О-о! {w} Смотри! Похоже это твой дом!"
    melissa "Да! {w} Точно! {w} Здесь я не могу ошибаться!"
    "Да она шутит! Мало того что странно себя ведёт, так ещё и знает лучше меня где мой же дом!!"

    hide melissa
    show melissa_shy

    melissa "Знаешь, я и не думала, что ты захочешь со мной заговорить..."

    if acceptGoHome == True:
        "Зная себя, я тоже не мог бы подумать, что пообщаюсь с кем-то. {w} В особенности с такой чудачкой."
        "Но проще было уже смириться."
    else:
        "Она мне и выбора не дала. Как я мог с ней не заговорить если она в любом случае пошла бы за мной и заговорила бы."
        "Лучше уж так, чем потом слушать её недовольство на счёт меня завтра и всю неделю вперёд."
        "Нужно же уметь такой приставучей быть!"

    "Даже так, лучше ответить не задевая её"
    user "Правду говоря, я тоже так не думал."
    user "Ладно, я тогда пойду наверное... {w} Уже темнеет."

    hide melissa_shy
    show melissa_r

    melissa "Да, ты прав! {w} Тогда я тоже пойду!"
    melissa "Спасибо тебе за прогулку! {w} Очень надеюсь что мы ещё не раз поговорим!!"

    scene melissa_waves_scene with fade

    "Мелисса помахав рукой быстрым шагом ушла в сторону остановки. {w} Наверное ей нужно проехаться на трамвае, прежде чем она будет дома."

    return
