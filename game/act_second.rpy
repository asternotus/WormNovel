default fahrenheit_belief = 0
default monument_belief = 0
default planar_belief = 0

default arguments_debate_round = 0

define left_side = Position(xalign=0.2)
define center_side = Position(xalign=0.5)
define right_side = Position(xalign=0.8)

define arguments = [
    {"title": "Это вопрос совести",
    "text": "Наша совесть будет чиста, если мы попытаемся помочь, даже если не сможем найти его",
    "fahrenheit": 1,
    "monument": -1,
    "planar": 0,
    "fahr_answer": "Согласна. Я бы хотела сделать хоть что-то.",
    "mon_answer": "Смысл за это браться, если ты не уверена в успехе?",
    "plan_answer": "..."},

    {"title": "Спасение жизни важнее приказа",
    "text": "Да, есть риски за нарушение приказа. Но разве место в Протекторате важнее спасённой жизни?",
    "fahrenheit": 1,
    "monument": -1,
    "planar": 0,
    "fahr_answer": "Ты права. Хоть мне и важно быть Стражем, но есть вещи и поважнее.",
    "mon_answer": "Чтобы рисковать нужно понимать как его найти, а у нас нет ничего. Вообще ничего!",
    "plan_answer": "..."},

    {"title": "Оправданный риск, чтобы быть Стражами",
    "text": "Да, есть приказ. Да, мы рискуем нашей карьерой. Но что мы тогда за Стражи, если нам нужно разрешение на то, чтобы кого-то спасти?",
    "fahrenheit": 1,
    "monument": 0,
    "planar": -1,
    "fahr_answer": "И я хочу, чтобы моё имя было оправдано.",
    "mon_answer": "...",
    "plan_answer": "Не будет карьеры, не будет и названия. Если всё что у нас есть - вдохновляющие речи, то это провал."},

    {"title": "Мы все будем несчастны, если не попытаемся",
    "text": "Мы все будем несчастны, от того что не попытались помочь.",
    "fahrenheit": 1,
    "monument": 0,
    "planar": -1,
    "fahr_answer": "Я бы очень хотела избавиться от этого чувства. Именно поэтому и хотелось бы попытаться.",
    "mon_answer": "...",
    "plan_answer": "Невозможно помочь всем. А тем более, переживать о каждом подобном случае."},

    {"title": "Действия без ограничений",
    "text": "Если мы не будем расследовать официально, мы сможем не сдерживать себя в наших действиях и быстрее достигнуть успеха.",
    "fahrenheit": -1,
    "monument": 1,
    "planar": 0,
    "fahr_answer": "Айрин, правила сдерживания существуют не просто так. Они уже ранее приводили к ошибкам.",
    "mon_answer": "Как по мне - звучит неплохо!",
    "plan_answer": "..."},

    {"title": "Доверие Протектората в будущем",
    "text": "Нам никогда не доверят ничего серьёзного, если мы отступим сейчас.",
    "fahrenheit": -1,
    "monument": 1,
    "planar": 0,
    "fahr_answer": "Нет. Нам никогда не доверят ничего серьёзного, если поймут, что нам плевать на официальные запреты.",
    "mon_answer": "Это одна из вещей, из-за которых я хочу согласиться.",
    "plan_answer": "..."},

    {"title": "Вера в команду",
    "text": "Я верю в силу нашей команды, в отличие от Ронина.",
    "fahrenheit": 0,
    "monument": 1,
    "planar": -1,
    "fahr_answer": "...",
    "mon_answer": "Вот такой настрой по мне.",
    "plan_answer": "Если бы вера так работала, осталось бы только поверить, что мальчик найдётся и сам."},

    {"title": "Положим конец бесполезным заданиям",
    "text": "Мы больше не будем мучаться, рассуждая о своей бесполезности, если сделаем это.",
    "fahrenheit": 0,
    "monument": 1,
    "planar": -1,
    "fahr_answer": "...",
    "mon_answer": "Поддерживаю.",
    "plan_answer": "Лучше уж быть бесполезным, чем не иметь плана."},

    {"title": "У нас уже есть зацепки",
    "text": "У нас уже есть зацепки, чтобы добыть информацию. Откинем страхи и другие эмоции, чтобы сделать все правильно.",
    "fahrenheit": -1,
    "monument": 0,
    "planar": 1,
    "fahr_answer": "Это так не работает. Нередко все планы и ломаются от недостатка эмпатии и переживаний.",
    "mon_answer": "...",
    "plan_answer": "Вот это то с чего, действительно, можно было бы и начать."},

    {"title": "Марк может анализировать местность",
    "text": "Пусть Стражи команды Легион лучше в расследованиях, но зато у нас есть Марк, способный анализировать местность.",
    "fahrenheit": -1,
    "monument": 0,
    "planar": 1,
    "fahr_answer": "Способность Марка имеет ограничения по расстоянию. Нужно будет знать хотя бы где искать.",
    "mon_answer": "...",
    "plan_answer": "А это дельная мысль. Со мной мы сможем значительно ускорить поиски."},

    {"title": "СМИ свяжут провал с нами",
    "text": "СМИ уже зафиксировали тот случай в школе, где была я и Алиса. Мы подорвём свою репутацию в обществе, если ничего не сделаем.",
    "fahrenheit": 0,
    "monument": -1,
    "planar": 1,
    "fahr_answer": "...",
    "mon_answer": "Я не против иногда подстраиваться под репортёров. Но не рисковать же всем ради них.",
    "plan_answer": "Да, спорить не буду. Если бы мы справились - было бы выгодно."},

    {"title": "Это важный опыт для нас",
    "text": "Действуя осторожно, даже если мы не найдём Сэмми, мы сможем получить необычайно важный опыт.",
    "fahrenheit": 0,
    "monument": -1,
    "planar": 1,
    "fahr_answer": "...",
    "mon_answer": "Не-не-не. Либо мы организовываемся на успех, либо к чёрту это всё.",
    "plan_answer": "Если сочетать это с нашими дежурствами и не палиться, звучит и вправду как беспроигрышный вариант."},
]

define used_arguments = []

label act_second_ronin_office:

    jump act_second_next_move

    hide background
    hide character

    stop music
    play music basement_music loop volume 0.6
    show act_second_ronin_office_cabinet as background

    play music basement_music loop volume 0.6

    ronin "Войдите."

    hide character

    me "Мы вошли в уже хорошо знакомый мне кабинет Ронина."

    me "Как и обычно, здесь стояла напряжённая атмосфера"
    
    me "Стойкое ощущение ожидания нового выговора или нравоучения."

    show ronin_costume_no_mask_idle as character

    ronin "Я предполагаю, это не просто визит."

    ronin "Что вам нужно?"

    iam "Исчез мальчик из школы, где проходило наше дежурство."
    
    iam "Сэмми Колинз. Тот самый, над которым издевались."

    ronin "Допустим."

    ronin "Хотите поделиться какой-то информацией?"

    iam "Я хочу чтобы мы занялись этим расследованием."

    me "Ронин даже не шевельнулся."

    me "Из-за костюма, который полностью закрывал его тело и лицо, он больше напоминал робота, нежели человека."

    ronin "Молодые люди..."

    ronin "Кажется вы здесь уже достаточно давно, чтобы понимать, что есть группы в Протекторате, специально созданные для подобных целей."

    ronin "Стрелок 4, Контакт 4, Контакт 6 и Эпицентр 7."

    ronin "Среди вас ни одного Умника или Властелина."

    ronin "Думаю, мой ответ очевиден."

    ronin "НЕТ."

    iam "Сэр, мы и Алиса..."

    ronin "Что я говорил про гражданские имена в стенах Протектората?"

    hide character

    me "Его голос звучал с изрядной долей раздражения."

    iam "Сэр, я и Фаренгейт были в тот день на месте незадолго до его исчезновения."

    show ronin_costume_no_mask_idle as character

    ronin "Искра, причастность к ситуации, не меняет ваших способностей, навыков и опыта."

    me "Он произнёс это более мягко чем я ожидала."

    show monument_costume_no_mask_scream as character

    monument "Что, даже моих?"

    monument "На ТОТ случай значит у меня хватало опыта, а сейчас нет?"

    show ronin_costume_no_mask_idle as character

    me "Ронин встал из-за стола, возвышаясь над Девидом."

    ronin "Монумент, мы уже не раз это обсуждали."

    ronin "Если я принял неверное решение в прошлом, это не значит, что мои последующие решения стоит игнорировать."

    ronin "Расследованием займётся команда Легион."

    ronin "В её распоряжении Бор со способностью к химическому восприятию."
    
    ronin "Ланцелот с его манипуляцией эмоциями."

    show planar_costume_no_mask_angry as character

    planar "Алекс?"

    planar "Этот мудила?"

    hide character

    if game_state.act_first_weekend_place == 2:

        me "Что? Алекс в команде Легион?"

        me "Использовал на мне способность под видом психолога."

        me "Использовал на мне способность, когда я была у Марка."

        me "Он же грёбаный психопат."

    else:

        me "Алекс? Это же тот самый псевдопсихолог, который чуть не довёл меня до безумия."

        me "Ясно..."

        me "Так вот что это за хрень была на моём интервью."

        me "Он использовал на мне свою способность."

        me "Стало по-настоящему жутко."

        me "Он же псих."

    me "Последнее что ему можно доверить - это поиск ребёнка."

    show ronin_costume_no_mask_idle as character

    ronin "Планар, ещё раз я услышу что-то подобное в отношении ваших коллег, все объяснения закончатся."

    show fahrenheit_costume_no_mask_confused as character

    fahrenheit "Сэр, в отличие от других Героев и Стражей, у нас есть хоть какие-то зацепки."

    fahrenheit "Мы общались со школьным учителем, который нам доверяет."

    fahrenheit "А Айрин..."

    show ronin_costume_no_mask_idle as character

    me "Ронин резко обернулся к ней всем телом."

    me "К счастью, Алиса мгновенно сообразила, что не так."

    show fahrenheit_costume_no_mask_confused as character

    fahrenheit "А Искра, по факту, прямой свидетель событий."

    show ronin_costume_no_mask_idle as character

    ronin "Я не запрещаю вам делиться информацией со Стражами Легион."

    ronin "Но не более."

    ronin "Мой ответ - НЕТ."

    iam "Сэр..."

    ronin "Повторять не стану! Разгвор окончен!"

    hide character

    me "Ронин оставался непреклонным, а его решение было железным."

    me "Дальше продолжать было бы бессмысленно."

    me "Мы вышли из кабинета и проследовали на базу."

    jump act_second_arguments_conversation

label act_second_arguments_conversation:

    $ arguments_debate_round = 0

    if game_state.fahrenheit_rel < - 1:
        $ fahrenheit_belief = -2
    else:
        $ fahrenheit_belief = 0

    if game_state.monument_rel < - 1:
        $ monument_belief = -2
    else:
        $ monument_belief = 0

    if game_state.planar_rel < - 1:
        $ planar_belief = -2
    else:
        $ planar_belief = 0

    if game_state.act_first_weekend_place == 0:
        $ fahrenheit_belief = 2
    elif game_state.act_first_weekend_place == 1:
        $ monument_belief = 2
    elif game_state.act_first_weekend_place == 2:
        $ planar_belief = 2
    else:
        pass

    hide background
    hide character

    show act_first_protectorate_basement as background

    me "Разочарование и беспомощность ощущались в воздухе."

    me "Монумент, переполненный гневом, ударил кулаком по металлической стене."

    show monument_costume_no_mask_scream as character

    monument "Это просто пиздец!"

    show fahrenheit_costume_no_mask_confused as character

    fahrenheit "По-другому и не скажешь."

    fahrenheit "Но..."

    fahrenheit "Может быть, мы ещё сможем что-то сделать?"

    show planar_costume_no_mask_angry as character

    planar "Ты же слышала Ронина."

    planar "Без объяснений и компромиссов."

    planar "Как всегда, в общем."

    hide character

    me "Алиса вздохнула глубоко, а Дэвид скрыл лицо в ладонях, устало опираясь на стену."

    show monument_costume_no_mask_idle as character

    monument "Я не хочу с этим мириться, но Марк, похоже, прав."

    monument "Ронин ожидает от нас беспрекословного исполнения задач, не давая шагнуть в сторону."

    monument "И потом можно будет хоть до посинения говорить, что мы хотели как лучше."

    monument "Просто повторим судьбу Вектора и всё."

    if game_state.act_first_weekend_place == 1:

        hide character

        me "Я уже знала кто такой Вектор."

        me "Именно он переместил Девида в здание, которое захватил Рестарт."

        me "Позже Девид рассказывал мне, насколько они были дружны."

        me "Только вот Вектор, без получения разрешения, пытался остановить кейпа-подрывника."

        me "Он пошёл один и в процессе погибло четверо гражданских."

        me "Вектору пришлось покинуть Протекторат навсегда."

        me "А я заняла его место в команде."

        me "Думаю Девид не хотел бы, чтобы подобное повторилось вновь."

    if not game_state.act_first_weekend_place == 1:

        iam "Вектора?"

        monument "Наш бывший сокомандник."

        monument "Без получения разрешения пытался остановить кейпа-подрывника."

        monument "Он пошёл один и в процессе погибло четверо гражданских."

        monument "Суперзлодея в итоге поймали."

        monument "А вот Вектору пришлось попрощаться с карьерой в Протекторате."

        hide character

        me "Я не знала как реагировать."

        me "Очевидно тема была достаточно личной для каждого из них."

    show fahrenheit_costume_no_mask_confused as character

    fahrenheit "Каждый день, когда мы не занимаемся тем чем должны, кажется мне всё более тягостным."

    fahrenheit "И вот теперь, когда возникла возможность сделать что-то по-настоящему значимое..."

    fahrenheit "А нас заставляют притворяться, будто ничего не произошло."

    hide character

    me "Я присела рядом с Дэвидом, чувствуя тяжесть момента."

    me "Тишина в комнате становилась почти осязаемой."

    me "Готова ли я согласиться с Ронином?"

    me "Нет, это не вариант."

    me "Возможно, есть и моя немалая вина в том, что произошло."

    me "В моей голове мелькают альтернативные сценарии того дня, каждый из которых ведёт к разным исходам."

    if game_state.attack_teen:

        me "Стоило ли мне бить того подростка?"

        me "Может слова имели бы больший вес и не настолько бы накалили обстановку?"

    if not game_state.attack_teen:

        me "Я пыталась запугать подростка, но ничего не вышло в итоге."

        me "Стоило ли действовать более решительно?"

    me "А после появления Резонанса..."

    me "В моей памяти возникла фигура кейпа в белом костюме."

    me "Мысли плавно переключились на воспоминание о встречи с Резонансом в больнице."

    if game_state.hospital_use_power:

        me "Я вспомнила о сделке в больнице, которую он мне предложил."

        me "Я бы не стала себе врать, что это волнует меня меньше, чем пропавший ребёнок."

        me "Права ли Софи?"

        me "Станет ли необратимой ошибкой моя попытка договориться с суперзлодеями?"

        me "Или же эта та возможность, которая когда-то подарит Нэнси надежду?"

        me "А может быть ему может быть что-то известно о пропавшем?"

        me "Ведь Резонанс применил силу, чтобы дать мальчику сбежать от его мучителей."
        
        me "Шанс на получение информации кажется мне крошечным, но именно он всё-таки не нулевой."

    if not game_state.hospital_use_power:

        me "Я вспомнила о ситуации в больнице, где я оказалась максимально беспомощной."

        me "Не смогла дать злодеям отпор, только потому что нарушила бы правила, ибо была не в костюме."

        me "И вот сейчас, мы также боимся нарушить правила, когда пропавший мальчик может нуждаться в нашей помощи."

    me "Если я смогу убедить других взяться за это расследование, у нас появится возможность изменить ход событий."

    me "Каждый переживает, что максимум героизма от нас - это только цветные костюмы."

    me "Я должна найти аргументы."
    
    me "Достаточно убедительные, чтобы мотивровать ребят действовать."

    me "Действовать, несмотря на запрет Ронина и страх потерять своё место в Протекторате."

    show fahrenheit_costume_no_mask_confused as character

    me "Алиса."

    show monument_costume_no_mask_idle as character

    me "Девид."

    show planar_costume_no_mask_angry as character

    me "Марк."

    hide character

    me "Все такие разные."

    me "Сложно будет убедить вас всех."

    me "Но я обязана попытаться!"

    jump act_second_arguments_debate_prepare

label act_second_arguments_debate_prepare:
    hide background
    hide character

    stop music
    show act_first_protectorate_basement as background

    play music strange_music loop volume 0.6

    $ used_arguments = []

    if fahrenheit_belief > 0:
        show fahrenheit_costume_no_mask_idle at left_side as fahr_character
    elif fahrenheit_belief == 0:
        show fahrenheit_costume_no_mask_confused at left_side as fahr_character
    elif fahrenheit_belief < 0:
        show fahrenheit_costume_no_mask_angry at left_side as fahr_character

    if monument_belief > 0:
        show monument_costume_no_mask_smile at center_side as mon_character
    elif monument_belief == 0:
        show monument_costume_no_mask_idle at center_side as mon_character
    elif monument_belief < 0:
        show monument_costume_no_mask_scream at center_side as mon_character

    if planar_belief > 0:
        show planar_costume_no_mask_smile at right_side as plan_character
    elif planar_belief == 0:
        show planar_costume_no_mask_idle at right_side as plan_character
    elif planar_belief < 0:
        show planar_costume_no_mask_angry at right_side as plan_character

    jump act_second_arguments_debate

label act_second_arguments_debate:

    $ choice_yalign = 0.1

    if arguments_debate_round == 5:
        jump act_second_next_move
    else:
        $ arguments_debate_round += 1

    $ available_arguments = [arg for arg in arguments if arg not in used_arguments]
    $ random_arguments = renpy.random.sample(available_arguments, 2)

    # Добавляем оба предложенных аргумента в список использованных, еще до выбора
    $ used_arguments.extend(random_arguments)

    $ selected_argument = None

    $ first_argument_title = random_arguments[0]["title"]
    $ second_argument_title = random_arguments[1]["title"]

    $ first_argument_text = random_arguments[0]["text"]
    $ second_argument_text = random_arguments[1]["text"]

    menu:
        "[first_argument_title]":
            $ selected_argument = random_arguments[0]
            me "[first_argument_text]"
        "[second_argument_title]":
            $ selected_argument = random_arguments[1]
            me "[second_argument_text]"
    
    $ fahrenheit_belief += selected_argument["fahrenheit"]
    $ monument_belief += selected_argument["monument"]
    $ planar_belief += selected_argument["planar"]

    if fahrenheit_belief > 0:
        show fahrenheit_costume_no_mask_idle at left_side as fahr_character
    elif fahrenheit_belief == 0:
        show fahrenheit_costume_no_mask_confused at left_side as fahr_character
    elif fahrenheit_belief < 0:
        show fahrenheit_costume_no_mask_angry at left_side as fahr_character

    if monument_belief > 0:
        show monument_costume_no_mask_smile at center_side as mon_character
    elif monument_belief == 0:
        show monument_costume_no_mask_idle at center_side as mon_character
    elif monument_belief < 0:
        show monument_costume_no_mask_scream at center_side as mon_character

    if planar_belief > 0:
        show planar_costume_no_mask_smile at right_side as plan_character
    elif planar_belief == 0:
        show planar_costume_no_mask_idle at right_side as plan_character
    elif planar_belief < 0:
        show planar_costume_no_mask_angry at right_side as plan_character
    
    $ fahr_answer = selected_argument["fahr_answer"]
    fahrenheit "[fahr_answer]"

    $ mon_answer = selected_argument["mon_answer"]
    monument "[mon_answer]"

    $ plan_answer = selected_argument["plan_answer"]
    planar "[plan_answer]"

    jump act_second_arguments_debate

label act_second_next_move:

    show act_first_protectorate_basement as background

    $ choice_yalign = 0.5

    if fahrenheit_belief >= 0:

        $ game_state.fahrenheit_is_ready = True

        fahrenheit "К чёрту, я хочу это сделать и мне плевать на этот запрет."

        fahrenheit "Ты меня убедила."

        fahrenheit "Айрин, я с тобой."

    else:

        $ game_state.fahrenheit_is_ready = False

        fahrenheit "Айрин, я правда понимаю насколько для тебя это важно."

        fahrenheit "Но мы не можем просто так нарушить запрет."

        fahrenheit "Кроме того, у команды Легион есть все шансы справиться."

        fahrenheit "Пожалуйста не злись, но я не могу."

        hide fahr_character

    if monument_belief >= 0:

        $ game_state.monument_is_ready = True

        monument "К чёрту Ронина, я хочу это сделать и мне плевать на этот запрет."

    else:

        $ game_state.monument_is_ready = False

        monument "Хотел бы я верить, что нам хватит решительности найти парня, ни смотря ни на что."

        monument "Но не могу."

        monument "Мы рискуем не только распадом команды, но и позорным поражением."

        monument "Извините, но я не готов."

        hide mon_character

    
    if planar_belief >= 0:

        $ game_state.planar_is_ready = True

        planar "Если мы будем придерживаться чёткого и проработанного плана - я согласен."

    else:

        $ game_state.planar_is_ready = False

        planar "Всё что у нас есть сейчас - это эмоции."

        planar "А значит, мы обречены на провал."

        planar "Сори, я пас."

        hide mon_character


    if game_state.fahrenheit_is_ready or game_state.monument_is_ready or game_state.planar_is_ready:

        me "Я старалась как могла."

        me "Теперь остались только те, кто реально готов действовать."

        me "Главная задача - оправдать возложенные на меня ожидания."

        hide fahr_character
        hide mon_character
        hide plan_character

        iam "Итак..."

        iam "Нам нужно подумать с чего начать."

    if game_state.fahrenheit_is_ready:

        show fahrenheit_costume_no_mask_idle as character

        fahrenheit "Думаю не сложно будет узнать домашний адрес Сэмми."

        fahrenheit "Поговорить с родителями и придумать причину, чтобы обыскать его комнату."

        fahrenheit "Вероятно, там будет немало подсказок."

        if not game_state.monument_is_ready:

            fahrenheit "Также можно разузнать что-нибудь у учителя из той школы."

            fahrenheit "Думаю он сможет нам помочь с тем, чтобы найти тех подонков из школы, которые издевались над Сэмми."

        if not game_state.planar_is_ready:

            fahrenheit "А ещё было бы неплохо исследовать местность вокруг школы."


    if game_state.monument_is_ready:

        show monument_costume_no_mask_idle as character

        monument "Мистер Террел - учитель из школы."

        monument "Мы с ним общались и он была крайне настроен на сотрудничество с нами."

        monument "Мы сможем распросить его про Сэмми, а также про тех хулиганов."

        monument "Думаю, звучит неплохо для отправной точки."

        if not game_state.fahrenheit_is_ready:

            monument "Также мы можем узнать домашний адрес Сэмми."

            monument "Поговорить с его родителями и, возможно, обнаружить что-то важное в его комнате."

        if not game_state.planar_is_ready:

            monument "А ещё было бы неплохо исследовать местность вокруг школы."

    if game_state.planar_is_ready:

        show planar_costume_no_mask_idle as character

        planar "Исследовать территорию вокруг школы."

        planar "Там мальчика видели в последний раз."

        planar "Предполагаю, мы сможем найти что-то полезное."

        if not game_state.fahrenheit_is_ready:

            planar "Также можно разузнать что-нибудь у учителя из той школы."

            planar "Думаю он сможет дать дополнительную информацию и адреса, как пропавшего, так и тех кто над ним издевался."

        if not game_state.monument_is_ready:

            planar "А ещё было бы неплохо наведаться к родителям Сэмми."

            planar "Мы сможем немало узнать о его жизни и это может быть важной зацепкой."
            
    if not game_state.fahrenheit_is_ready and not game_state.monument_is_ready and not game_state.planar_is_ready:

        me "Я осталась одна."

        me "Не ожидала, что меня никто не поддержит, но я могу их понять."

        me "Теперь это только моё дело и я ответственна только за свои решения."

        me "Я достала листок бумаги и принялась делать заметки."

        me "Номер один - школьный учитель Мистер Террел."

        me "Думаю он пойдёт на сотрудничество."
        
        me "Он сможет рассказать как о Сэмми, так и о тех ублюдках, которые над ним издевались."

        me "Номер два - дом Сэмми, я могу найти там ценные улики, а также узнать информацию от его родителей."

        me "Адрес будет не так сложно найти."

        me "Номер три - исследовать территорию вокруг школы."

        me "Здесь не придётся ни с кем общаться, но зато есть шанас найти полезные зацепки."

    hide character

    me "Все идеи имеют смысл."

    me "Вот только время поджимает."

    me "Чем раньше прибыть на место - тем меньше вероятность, что там уже окажется команда Легион."

    me "Кроме того, я всё ещё не могу забывать о предложении Резонанса."

    me "Если попытаюсь встретиться с ним, я не только рискую быть обнаруженной..."

    me "Я также рискую упустить возможность попасть в одно из мест, необходимых для полного расследования."

    me "Итак..."

    me "Главное помнить, что у меня не хватит времени на все четыре варианта."

    me "Одним придётся пожертвовать."

    if not game_state.fahrenheit_is_ready and not game_state.monument_is_ready and not game_state.planar_is_ready:

        me "Кроме того, мы можем разделиться в наших поисках, но вариант встречи с Резонансом будет доступен только мне."

    me "Пришло время выбирать!"

    jump act_second_select_irene_order

    return

label act_second_select_irene_order:

    show act_first_protectorate_basement as background

    if game_state.fahrenheit_is_ready or game_state.monument_is_ready or game_state.planar_is_ready:

        if game_state.fahrenheit_is_ready:

            show fahrenheit_costume_no_mask_idle as character

            fahrenheit "Я буду у мистера Террела."

            fahrenheit "Постараюсь узнать адрес того хулигана."

        if game_state.monument_is_ready:

            show monument_costume_no_mask_idle as character

            monument "Я буду у родителей пацана."

            monument "Я сообщу тебе адрес, как найду."

        if game_state.planar_is_ready:

            show planar_costume_no_mask_idle as character

            planar "Я исследую территорию школы."

            planar "Постараюсь найти как можно больше зацепок."

        me "Надо подумать, куда же мне отправиться первым делом..."

        menu:
            "Встретиться с учителем":

                $ game_state.actual_investigation_labels.clear()
                $ game_state.actual_investigation_labels.append("act_second_teacher")

                iam "Первым делом я пойду к учителю."

            "Встретиться с родителями Сэмми у него дома":

                $ game_state.actual_investigation_labels.clear()
                $ game_state.actual_investigation_labels.append("act_second_sammy_home")

                iam "Я отправлюсь домой к Сэмми."

                iam "Уверена, его родителям есть, что сообщить."

            "Исследовать территорию школы":

                $ game_state.actual_investigation_labels.clear()
                $ game_state.actual_investigation_labels.append("act_second_school_territory")

                iam "Я осмотрю территорию школы."

                iam "И окрестности."

            "Исследовать западную часть города (не упоминать про Резонанса)":

                $ game_state.actual_investigation_labels.clear()
                $ game_state.actual_investigation_labels.append("act_second_resonance_deal")

                iam "Я отправлюсь в заданую часть города."

                if game_state.fahrenheit_is_ready:

                    show fahrenheit_costume_no_mask_confused as character

                    fahrenheit "Исследовать западные районы? Ты сошла с ума?"

                    fahrenheit "Там же люди Коллектора."

                if game_state.monument_is_ready:

                    show monument_costume_no_mask_scream as character

                    monument "Нам не разрешены дежурства в западных районах."

                    monument "Это же охуеть как опасно!"

                    monument "Для чего туда идти?"

                if game_state.planar_is_ready:

                    show monument_costume_no_mask_idle as character

                    planar "Да уж, вообще не звучит как что-то, что мне нравится."

                    planar "Ты уверена, что готова пойти туда?"

                hide character

                iam "Знаю-знаю, но я не могу исключать причастность Резонанса."

                iam "Я понимаю на что иду и буду действовать аккуратно."

                iam "Всё чего прошу - довериться мне!"

                me "Мне жаль, что я не могу сказать истинную цель этого этапа плана."

                me "По крайней мере сейчас."

    else:

        me "Надо подумать, куда же мне отправиться первым делом..."

        menu:
            "Встретиться с учителем":

                $ game_state.actual_investigation_labels.clear()
                $ game_state.actual_investigation_labels.append("act_second_teacher")

                me "Первым делом я пойду к учителю."

            "Встретиться с родителями Сэмми у него дома":

                $ game_state.actual_investigation_labels.clear()
                $ game_state.actual_investigation_labels.append("act_second_sammy_home")

                me "Я отправлюсь домой к Сэмми."

                me "Уверена, его родителям есть, что сообщить."

            "Исследовать территорию школы":

                $ game_state.actual_investigation_labels.clear()
                $ game_state.actual_investigation_labels.append("act_second_school_territory")

                me "Я осмотрю территорию школы."

                me "И окрестности."

            "Найти Резонанса":

                $ game_state.actual_investigation_labels.clear()
                $ game_state.actual_investigation_labels.append("act_second_resonance_deal")

                me "Я отправлюсь в заданую часть города."

    hide character

    me "Решение принято."

    me "Куда идти дальше - разберусь по ходу."

    me "Я понимаю, что стоит на карте."

    me "Я могу потерять статус, лишиться прибыли от службы, а также попасть в реальную опасность."

    me "Но почему-то ощущение, что я делаю всё правильно, не покидает меня."

    me "Моё первое настоящее задание в качестве Стража."

    me "И я сделаю всё что в моих силах!"

    $ renpy.jump(game_state.actual_investigation_labels[-1])

label act_second_teacher:

    me "Мы пришли к учителю."

    $ teacher_check = "act_second_teacher" in game_state.actual_investigation_labels
    $ sammy_home_check = "act_second_sammy_home" in game_state.actual_investigation_labels
    $ school_check = "act_second_school_territory" in game_state.actual_investigation_labels
    $ resonance_deal_check = "act_second_resonance_deal" in game_state.actual_investigation_labels
    $ investigation_completed = len(game_state.actual_investigation_labels) >= 3

    menu:

        "Встретиться с родителями Сэмми у него дома" if not sammy_home_check:

            $ game_state.actual_investigation_labels.append("act_second_sammy_home")

            me "Теперь я отправлюсь домой к Сэмми."

            me "Уверена, его родителям есть, что сообщить."

        "Исследовать территорию школы" if not school_home_check:

            $ game_state.actual_investigation_labels.append("act_second_school_territory")

            me "Теперь я осмотрю территорию школы."

            me "И окрестности."

        "Найти Резонанса" if not resonance_deal_check:

            $ game_state.actual_investigation_labels.append("act_second_resonance_deal")

            me "Теперь я отправлюсь в заданую часть города."

        "Вернуться в Протекторат" if investigation_completed:

            me "Нужно вернуться обратно в Протекторат и проанализировать всё, что удалось узнать."

    $ renpy.jump(game_state.actual_investigation_labels[-1])

    return

label act_second_sammy_home:

    me "Я поднялась по ступенькам к передней двери дома, где жил Сэмми."
    
    me "Воздух был пропитан запахом влажной земли и свежести после закончившегося недавно дождя."
    
    me "Я нажала пальцем на звонок, после чего раздался продолжительный неприятный звук."
    
    me "Мне пришлось приложить немало моральных усилий, чтобы попасть сюда как можно раньше."

    me "Позвонила по номеру и представилась журналисткой, которая собирает информацию от родителей пропавших детей."

    me "Я осознавала, что информация об этом звонке рано или поздно попадёт в Протекторат."

    me "Кроме того, я вообще не ожидала, что родители согласятся так просто."

    me "Однако, вместо обилия вопросов, они практически сразу назвали мне время и адрес."

    me "Мне пришлось отправиться к ним в гражданской одежде, что также могла поставить под угрозу раскрытие моей личности."

    me "Но я успокаивала себя тем, что если сделать всё правильно - это будет идеальный план."

    nobody_sammy_father "Да? Кто там?"
    
    me "Спокойный и мягкий мужской голос раздался по ту сторону двери."

    iam "Меня зовут Энджел Стэф, я с телевидения."

    iam "Мы договаривались с вами о встрече по телефону."

    me "Дверь передо мной распахнулась."

    me "Я увидела перед собой мужчину средних лет в зелёной рубашке и старых потёртых джинсах."

    iam "Добрый день, мистер Коллинз, я полагаю?"

    sammy_father "Очень рад видеть вас, мис Стэф."

    sammy_father "Можете называть меня Билл."

    sammy_father "Прошу, проходите!"
    
    me "С некоторой неуверенностью, отец Сэмми отошёл в сторону, приглашая меня внутрь."

    me "Переступив порог, я ощутила смену атмосферы"
    
    me "Прохлада улицы сменилась на домашний и тёплый уют дома."
    
    me "Пахло выпечкой."

    me "Из кухни раздавались звуки, которые сложно было неузнать."

    me "Популярное шоу \"Мой Шедевр\"."

    me "Редко смотрела такое, особенно сама."

    me "Другое дело - поугарать с Виктором и Нэнси от карикатурных персонажей на экране."

    sammy_father "Дорогая, у нас гости!"

    sammy_mother "Ой, прекрасно. Заходите, я жду!"

    me "Мы вошли в небольшую кухню."

    me "Внимание Миссис Колинз было приковано к телевизору."

    me "Пока я раздумывала с чего начать, отец Сэмми сделал приготовил для меня кофе."

    me "Довольно неплохой."

    sammy_father "Должен признать, вы довольно молоды для репортёра."

    iam "Вы не первый человек от которого я это слышу."

    sammy_father "О господи, надеюсь я ничем вас не обидел?"

    iam "Конечно же нет, это даже забавно!"

    me "Притворяюсь как могу."

    me "Надо было выбирать карьеру в театре."

    me "Тоже костюмы и также нужно играть на публику."

    iam "Я пришла, как вы уже могли догадаться, поговорить о пропаже Сэмми."

    sammy_mother "Ох, вы даже себе не представляете."

    sammy_mother "Времена стали такими, что никто не застрахован от несчастья."

    sammy_mother "Нам так пусто без него дома."

    me "Отец осторожно кивнул, в подтверждение её слов."

    iam "Я уже успела поговорить с учителями и некоторыми его сверстниками."

    iam "У него ведь были проблемы в школе, не так ли?"

    sammy_mother "У всех детей в этом возрасте бывают проблемы, к сожалению."

    sammy_mother "Вы кстати записываете, то что мы говорим?"

    iam "Нет, что вы, это просто вопрос."

    sammy_mother "Я бы предпочла, чтобы вы записывали, чтобы мои слова были переданы точно, без каких-либо изменений."

    me "Неужели так важно? Не зря я видимо захватила ручку и блакном."

    me "Я достала свой \"инвентарь журналиста\" и записала туда всё о чём мы говорили."

    iam "Так всё-таки? Он же рассказывал вам о травле в школе?"

    me "Мистер Коллинз как-то странно посмотрел на свою жену, а затем вновь повернулся ко мне."

    sammy_father "Да, конечно! Но без каких либо подробностей."

    sammy_father "Дело в том, что он чудесный ребёнок, даже слишком."

    sammy_father "Он не только добрый, но ещё и смышлённый."

    sammy_mother "Мы старались не нарушать его личное пространство."

    sammy_mother "Всегда боялись, что он закроется."

    sammy_mother "Но сейчас, мы бы всё отдали, лишь бы он снова был рядом."

    sammy_father "Осталось только найти того, кто в этом виноват."

    sammy_father "Даже не знаю, что я готов с ним сделать."
    
    iam "Да, я понимаю, но разве он не вёл себя странно?"

    iam "Думаю, если ребёнок подвергается ежедневной травле, вряд ли он сможет вести себя как обычно."

    me "Отец Сэмми вновь переводил взгляд то на меня, то на миссис Колинз."

    sammy_mother "Я хочу чтобы все знали."

    sammy_mother "Как бы странно не вёл себя наш сын, я принимаю его любым."

    sammy_mother "Я...я..."

    me "Внезапно она ударилась в слёзы."

    me "Мистер Коллинз осторожно обнял её."

    me "Их реакция была объяснима, но, увы, никакой конкретики."

    me "Так я не получу нужную мне информацию."

    me "Если только..."

    me "Попасть в комнату Сэмми."

    me "Предметы и личные вещи могут стать важными подсказками."

    me "Вот только, как родители отреагируют на это?"

    me "Спросить напрямую?"

    me "Это может значительно ограничить мне возможности для поиска."

    me "Отвлечь их?"

    me "Рискованно."

    me "Потребовать на правах стража Протектората, раскрыв свою реальную личность?"

    me "Последнее звучит уже крайне безумно, но может такова и есть цена за информацию?"

    me "Ох, нужно решаться."

    menu:
        "Спросить напрямую":

            iam "Мне нужно осмотреть комнату Сэмми, это определённо поможет расследованию."

            sammy_mother "Каким образом?"

            iam "Его вещи, обстановка, это может..."

            sammy_father "Что мы скажем полиции, если они прибудут с обыском?"

            sammy_father "Нам придётся сообщить, что мы пустили репортёра раньше."

            sammy_mother "К тому же, у вас ведь нет собой камеры."

            sammy_mother "Значит и заснять ничего не получится."
            
            me "Что?"

            me "Полиции до сих пор не было?"

            me "Они ждут Стражей из команды Легион."

            me "Или...что-то ещё."

            iam "Я не буду ни к чему прикасаться, только посмотрю."

            iam "Обещаю!"

            me "Они в очередной раз переглянулись."

            sammy_father "Хорошо мисс Стиф, но мы будем присутствовать."

            sammy_mother "И безусловно мы дадим вам полную свободу действий, когда будет съёмочная группа."

            sammy_mother "Но не сейчас!"

            me "Это максимально странно."

            me "Но, делать нечего."

            me "Я кивнула и родители Сэмми отправились вместе со мной в комнату на втором этаже."

        "Придумать обман":

            iam "Не хочу вас задерживать, но у меня есть ещё несколько вопросов."

            sammy_father "Ну что вы, мы никуда не спешим."

            sammy_father "Верно, Дженни?"

            sammy_mother "Абсолютно."

            me "Она даже повернулась в мою сторону."

            me "Её взгляд всецело был прикован к телевизору."

            me "Я сконцентрировалась."

            me "Был ещё один телевизор на первом этаже и тоже включён."

            iam "Сэмми наверное тоже любит смотреть что-нибудь?"

            sammy_father "О да, мы постоянно раньше смотрели что-нибудь вместе."

            sammy_father "Собирались у меня и смотрели всё поряд, от новостей до стэндапов."

            me "Забавные, наверное, развлечения для двенадцатилетнего подростка."

            me "Выходит второй телевизор в комнате мистера Коллинза."

            me "Методом исключения, комната Сэмми на втором этаже."

            iam "Я хотела бы продолжить, только мне нужно вспользоваться уборной, если вы не против."

            sammy_father "Без проблем, я могу проводить..."

            iam "Прошу прощения, есть некоторые психологические моменты."

            iam "Просто, подскажите направление."

            sammy_father "Ой, да, понимаю, конечно!"

            sammy_father "На первом этаже, прямо направо и прямо до коричневой двери."

            me "Я кивнула и вышла из кухни, иммитируя затихающие шаги."

            me "Мне пришлось разуться, а затем сконцентрироваться, чтобы максимально бесшумно подняться по лестнице."

            me "Что-то странное было в родителях мальчика или же мне только так показалось."

            me "В любом случае, я была готова действовать."

        "Доказать им, что я Страж Протектората":

            iam "Мне нужно осмотреть комнату Сэмми, это определённо поможет расследованию."

            sammy_mother "Каким образом?"

            iam "Его вещи, обстановка, это может..."

            sammy_father "Что мы скажем полиции, если они прибудут с обыском?"

            sammy_father "Нам придётся сообщить, что мы пустили репортёра раньше."

            sammy_mother "К тому же, у вас ведь нет собой камеры."

            sammy_mother "Значит и заснять ничего не получится."
            
            me "Что?"

            me "Полиции до сих пор не было?"

            me "Они ждут Стражей из команды Легион."

            me "Или...что-то ещё."

            iam "Знаете, мистер и миссис Коллинз, я обязана тщательно осмотреть все возможные места."

            sammy_father "На каких основаниях?"

            iam "На основе..."

            iam "Стража Протектората!"

            me "Сначала они были явно шокированы."

            me "Однако шок практически мгновенно сменился на гнев."

            sammy_mother "Ну да, конечно. Страж Протектората, без костюма, прямо у нас дома."

            sammy_father "Ты кто вообще такая?"

            sammy_father "Решила, что можешь нас дурачить?"

            me "Они уже сделали шаг ко мне."

            me "Но я была готова."

            me "Погас свет..."

            me "Во всём доме, кроме места, где находилась я."

            me "Теперь мистер и миссис Колинз видели электрический згусток в моей руке."

            me "Как только они отступили, я вернула электроэнергию обратно."

            me "Они были напуганы."

            me "Что ж, а чего я ещё добивалась?"

            iam "Вы будете сидеть здесь и даже не вздумайте мне помешать."

            me "Они судорожно кивнули."

            me "Я вышла из кухни."

            me "Не успела я и дойти до конца лестницы, как услышала звук телешоу."

            me "Передо мной дверь, в комнату мальчика."

            me "Явно это был не лучший способ сюда попасть."

            me "Остаётся только надеяться, что всё это было не зря."   

    me "Я в комнате Сэмми."

    me "Признаться, я ожидала увидеть гораздо больший бардак в комнате подростка."

    me "Это конечно было сложно назвать идеальным порядком, но меня не покидало странное ощущение..."

    me "Каждая вещь в этой комнате словно была на своём месте."

    me "Книги в алфавитном порядке."

    me "Игрушки, которые, по всей видимости, никто не трогал уже лет 8 - строго от маленьких к большим."

    me "Даже вещи, разбросанные на полу, создавали впечатление системности..."

    me "Простыни к простыням, футболки к футболкам, коробки к коробкам."

    me "Зачем маленькому мальчику сортировать вещи?"

    me "Здесь явно нужно всё тщательно осмотреть."

    me "Вот только с чего бы начать..."

    me "На столе был точно такой же принцип организации, как и во всей комнате."

    me "Ручки к ручкам, карандаши к карандашам, листки бумаги сложенные в стопки."

    me "Последние особенно привлекли моё внимание."

    me "Я взяла в руки стопку."

    me "На каждом листке было по одному рисунку."

    me "Хорошим художником Сэмми было назвать сложно."

    me "Это были бы обычные детские рисунки, если бы ни одно НО."

    me "\"Дорога из школы домой\" - очень схематично, но всё же, Сэмми указал очень точный путь."

    me "В последнее время, мы с командой много работали с картами и я могла без труда узнавать улицы по очертаниям."

    me "Чёрт возьми, тут даже были наброски дорожных знаков."

    me "Также здесь Сэмми нарисовал себя, с сумкой в руках, внутри которой обозначены книги и тетради, а также очень странный разноцветный круглый предмет."

    me "Следующий рисунок."

    me "\"Школа\" - я вспоминала план, который описывал мистер Террел."

    me "Рисунок вновь идеально соответствовал ему, вплоть до расположения уборных."

    me "Сэмми нарисовал себя на заднем дворе школы, а в его сумка всё также книги, тетради и опять разноцветный круг."

    me "\"Дом\" - идеальная схема комнат."

    me "Я без труда нашла своё местоположение на рисунке."

    me "Тут была отображена практически каждая вещь, даже саме незначительные, почти также, как они расположены сейчас."

    me "Слева шкаф, в центре - письменный стол, справа кровать..."

    me "И тут, я увидела, что под кроватью нарисован ящик или сундук, внутри которого уже закомый мне разноцветный круглый предмет."

    me "Я залезла под кровать и, игнорируя создаваемый мною шум, вытащила оттуда сундук."

    me "Открыть его не составляло проблем, но, очевидно, Сэмми вряд ли хотел, чтобы он попал в чужие руки."

    me "Внутри не было ничего, кроме цветного колейдоскопа."

    sammy_father "Что вы здесь делаете?"

    me "Я резко обернулась, едва скрывая панику."

    me "Передо мной стоял мистер Коллинз на лице которого отпечаталась ярость."

    me "Я едва успел"

    sammy_father "Вы, кажется, забыли предоставить нам своё удостоверение журналиста."

    me "Он приблизился ко мне достаточно близко."

    sammy_father "Самое время его показать, девочка."

    sammy_father "Кажется у вас большие проблемы."

    me "Я бросилась к выходу, но мистер Коллинз легко схватил меня за руку."

    me "Из такой хватки просто так и не выберишься."

    sammy_father "Не переживайте, сейчас дождёмся полиции, а они разберутся."

    me "Я услышала как на первом этаже кто-то снял телефонную трубку и принялся набирать номер."

    me "Если дождусь полиции, огребу проблемы и поставлю расследование под угрозу."

    me "Попробую применить силу - они поймут, что я Страж."

    me "Дерьмо, а не выбор."

    me "Но нужно решать и как можно быстрее!"

    menu:

        "Дожидаться полиции":
            
            me "Пришлось подчиниться."

            me "Я не была готова использовать Силу против обычных людей."

            sammy_father "Дорогая, вызывай полицию!"

            sammy_mother "Сейчас! Осталось четыре минуты и мы узнаем кто выиграл."

            sammy_father "Посмотрим в записи, нужно вызвать сейчас."

            sammy_mother "Я никуда отсюда не пойду! Сам иди."

            sammy_father "Я и так еле решился отойти."

            me "Вдруг меня осенило."

            iam "Так вот оно что."

            iam "Мне сразу дали согласие, забыли спросить удостоверение, а ещё..."

            iam "Вы не знаете ни единого факта о жизни своего сына."

            sammy_father "Что ты несёшь?"

            iam "То что, вся ваша жизнь вертится вокруг конченых шоу с телевизора."

            iam "На Сэмми же вам глубоко плевать."

            iam "Небось были счастливы, что к вам заявился потенциальный человек, чтобы снять про вас репортаж."

            me "Удар."

            me "Боль."

            me "Он отвесил мне пощёчину."

            sammy_father "Ты не представляешь через что мы прошли."

            iam "Да уж представляю, к сожалению."

            iam "Когда боль настолько сильна, что тебе сложно есть, спать и вообще думать о чём либо другом."

            iam "Хочется хоть что-то сделать, даже когда все законы мира против тебя."

            iam "А твой любимый человек, навсегда потерян."

            me "Звук апплодисментов."

            me "Объвили победителя шоу."

            me "Мистер Колинз поднёс свободную руку у уху, стараясь услышать каждое слово ведущего."

            me "Мне ещё более стало мерзко."

            me "Но, тем не менее, я хотя бы смогла сдержаться."

            me "Раздался звонок в дверь."

            sammy_father "Пойдёшь со мной и без глупостей!"

            me "Он всё ещё крепко держал меня за руку и чуть ли не потащил вниз по лестнице вниз..."

            me "А затем, открыл входную дверь."

            me "На пороге стоял страж, одетый в рыцарские доспехи."

            me "Я без труда узнала его меч."

            me "Тот самый, который я видела в день своего первого интервью с фейковым психологом."

            lancelot "Добрый день, мистер Коллинз."

            lancelot "Меня зовут Ланцелот. Я из Протектората."

            me "ЭТО АЛЕКС???"

            sammy_father "Документы!"

            me "Голос отца Сэмми звучал грубо с ноткой безумия."

            me "Алекс показал ему удостоверение."

            sammy_father "Прошу прощения. Мы тут поймали мошенницу."

            alex "Прекрасная работа, мистер Коллинз."

            alex "Прошу передайте её мне, а я уже со всем разберусь."

            sammy_father "Дело в том, что полиция..."

            alex "Разве я не ясно выразился?"

            alex "ПЕРЕДАЙТЕ ЕЁ МНЕ!"

            alex "СЕЙЧАС!"

            me "Хватка мгновенно ослабла."

            me "На лице мистера Коллинза был страх."

            sammy_father "Да, конечно, всё что угодно для доблестного героя Протектората."

            alex "Прекрасно."

            alex "Если не хотите серьёзных последствий за домогательство, то я вам рекомендую, закрыться в своей комнате вместе с женой."

            alex "Я сообщу, как закончу расследование."

            me "Без лишних слов, семейство Коллинзов, словно послушные куклы, проследовали в дальнюю комнату на первой этаже."

            me "Дверь захлопнулась."

            alex "Подскажешь мне, где его комната?"

            iam "Чья?"

            alex "Пропавшего пиздюка, разумеется."

            me "Я, не отойдя от произошедшего, показала ему на дверь комнаты второго этажа."

            me "Он прошёл мимо меня, направляясь туда."

            iam "Мне нужно ждать, я так полагаю?"

            alex "Нет, конечно!"

            iam "Ты дашь мне уйти?"

            alex "Ага."

            me "Он открыл дверь в комнату Сэмми и скрылся за ней."

            me "Ничего не понимаю."

            me "В нормальной ситуации - он делает хрень, зато сейчас, когда мог меня сдать, решил ничего не делать."

            me "Ну да ладно."

            me "Не лучшее время думать об этом."

            me "Я открыла дверь и со всех ног пустилась подальше от этого места."

        "Использовать Силу, чтобы освободиться":

            sammy_father "Дорогая, вызывай полицию!"

            sammy_mother "Сейчас! Осталось четыре минуты и мы узнаем кто выиграл."

            sammy_father "Посмотрим в записи, нужно вызвать сейчас."

            sammy_mother "Я никуда отсюда не пойду! Сам иди."

            sammy_father "Я и так еле решился отойти."

            me "Вдруг меня осенило."

            iam "Так вот оно что."

            iam "Мне сразу дали согласие, забыли спросить удостоверение, а ещё..."

            iam "Вы не знаете ни единого факта о жизни своего сына."

            sammy_father "Что ты несёшь?"

            iam "То что, вся ваша жизнь вертится вокруг конченых шоу с телевизора."

            iam "На Сэмми же вам глубоко плевать."

            iam "Небось были счастливы, что к вам заявился потенциальный человек, чтобы снять про вас репортаж."

            me "Он только собирался замахнуться, но я легко погасила свет во всём доме."

            sammy_mother "ПРОКЛЯТЬЕ!"

            sammy_mother "КАКОГО ЧЁРТА???"

            sammy_mother "Эдгар! Сделай что-то с электричеством."

            sammy_mother "СРОЧНО!"

            me "Но в этот же момент мистер Коллинз получил мощный удар от моего импульса."

            me "Толчок заставил его отпустить мою руку, после чего я безприпятственно выбежала из комнаты, устремившись вниз по лестнице."

            me "Я уже была морально готова расчистить себе путь, применив испульс и против матери Сэмми."

            me "Вот только, она отчаянно пыталась вернуться к просмотру, маниакально дёргая рубильник."

            me "Я оказалась на улице."

            me "Гнев закипал во мне."

            menu:

                "Привести оба телевизора в негодность":

                    me "Я вернула электричество в дом."

                    me "Я ощущала его в ламочках, бытовой технике, а также в телевизорах."

                    me "Моих способностей вплоне хватало, чтобы сделать всё без риска взрыва."

                    me "Нагружая, отдельные микросхемы, я сделала всё необходимое, для невозможности передачи сигналов."

                    me "Семья Коллинзов ещё не скоро вернётся к просмотру телешоу."

                    me "Может хоть немного протрезвеют головой и подумают о сыне."

                    me "Не хотелось бы дождаться момента, когда они выбегут, чтобы разобраться со мной."

                    me "Я со всех ног пустилась подальше от этого места."

                "Просто уйти":

                    me "Однако я понимала, что не стоит ухудшать положение в уже и так дерьмовой ситуации."

                    me "Я со всех ног пустилась подальше от этого места."

    me "Да уж, не удивлена, что Сэмми стал жертвой травли, когда его родителям абсолютно наплевать на его судьбу."

    me "Всё что мне удалось найти - это..."

    # Тут текстом будет список ключевых улик, которые удалось найти

    me "Необходимо продолжать, а не сидеть на месте."

    me "А для этого, нужно определиться, куда идти дальше..."

    $ teacher_check = "act_second_teacher" in game_state.actual_investigation_labels
    $ sammy_home_check = "act_second_sammy_home" in game_state.actual_investigation_labels
    $ school_check = "act_second_school_territory" in game_state.actual_investigation_labels
    $ resonance_deal_check = "act_second_resonance_deal" in game_state.actual_investigation_labels
    $ investigation_completed = len(game_state.actual_investigation_labels) >= 3

    menu:

        "Встретиться с учителем" if not teacher_check:

            $ game_state.actual_investigation_labels.append("act_second_teacher")

            me "Теперь я пойду к учителю."

        "Исследовать территорию школы" if not school_home_check:

            $ game_state.actual_investigation_labels.append("act_second_school_territory")

            me "Теперь я осмотрю территорию школы."

            me "И окрестности."

        "Найти Резонанса" if not resonance_deal_check:

            $ game_state.actual_investigation_labels.append("act_second_resonance_deal")

            me "Теперь я отправлюсь в заданую часть города."

        "Вернуться в Протекторат" if investigation_completed:

            me "Нужно вернуться обратно в Протекторат и проанализировать всё, что удалось узнать."

    $ renpy.jump(game_state.actual_investigation_labels[-1])

    return

label act_second_school_territory:

    me "Мы пришли в школу."

    $ teacher_check = "act_second_teacher" in game_state.actual_investigation_labels
    $ sammy_home_check = "act_second_sammy_home" in game_state.actual_investigation_labels
    $ school_check = "act_second_school_territory" in game_state.actual_investigation_labels
    $ resonance_deal_check = "act_second_resonance_deal" in game_state.actual_investigation_labels
    $ investigation_completed = len(game_state.actual_investigation_labels) >= 3

    menu:

        "Встретиться с учителем" if not teacher_check:

            $ game_state.actual_investigation_labels.append("act_second_teacher")

            me "Теперь я пойду к учителю."

        "Встретиться с родителями Сэмми у него дома" if not sammy_home_check:

            $ game_state.actual_investigation_labels.append("act_second_sammy_home")

            me "Теперь я отправлюсь домой к Сэмми."

            me "Уверена, его родителям есть, что сообщить."

        "Найти Резонанса" if not resonance_deal_check:

            $ game_state.actual_investigation_labels.append("act_second_resonance_deal")

            me "Теперь я отправлюсь в заданую часть города."

        "Вернуться в Протекторат" if investigation_completed:

            me "Нужно вернуться обратно в Протекторат и проанализировать всё, что удалось узнать."

    $ renpy.jump(game_state.actual_investigation_labels[-1])

    return

label act_second_resonance_deal:

    me "Я добралась до западной части города."

    $ teacher_check = "act_second_teacher" in game_state.actual_investigation_labels
    $ sammy_home_check = "act_second_sammy_home" in game_state.actual_investigation_labels
    $ school_check = "act_second_school_territory" in game_state.actual_investigation_labels
    $ resonance_deal_check = "act_second_resonance_deal" in game_state.actual_investigation_labels
    $ investigation_completed = len(game_state.actual_investigation_labels) >= 3

    menu:

        "Встретиться с учителем" if not teacher_check:

            $ game_state.actual_investigation_labels.append("act_second_teacher")

            me "Теперь я пойду к учителю."

        "Встретиться с родителями Сэмми у него дома" if not sammy_home_check:

            $ game_state.actual_investigation_labels.append("act_second_sammy_home")

            me "Теперь я отправлюсь домой к Сэмми."

            me "Уверена, его родителям есть, что сообщить."

        "Исследовать территорию школы" if not school_home_check:

            $ game_state.actual_investigation_labels.append("act_second_school_territory")

            me "Теперь я осмотрю территорию школы."

            me "И окрестности."

        "Вернуться в Протекторат" if investigation_completed:

            me "Нужно вернуться обратно в Протекторат и проанализировать всё, что удалось узнать."

    $ renpy.jump(game_state.actual_investigation_labels[-1])

    return