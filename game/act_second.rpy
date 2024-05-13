default fahrenheit_belief = 0
default monument_belief = 0
default planar_belief = 0

default arguments_debate_round = 0

define left_side = Position(xalign=0.2)
define center_side = Position(xalign=0.5)
define right_side = Position(xalign=0.8)

define vector = Character("Вектор", what_font="gui/fonts/comic.ttf", what_size=35, what_color="#FFFFFF", what_outlines=[(2, "#740000", 0, 0)], who_color="#FFFFFF", who_outlines=[(2, "#740000", 0, 0)])
define collector = Character("Коллектор", what_font="gui/fonts/comic.ttf", what_size=35, what_color="#FFFFFF", what_outlines=[(2, "#4A4A4A", 0, 0)], who_color="#FFFFFF", who_outlines=[(2, "#4A4A4A", 0, 0)])
define resonance_voice = Character("Голос Резонанса", what_font="gui/fonts/comic.ttf", what_size=35, what_color="#FFFFFF", what_outlines=[(2, "#000000", 0, 0)], who_color="#FFFFFF", who_outlines=[(2, "#000000", 0, 0)])
define buran = Character("Буран", what_font="gui/fonts/comic.ttf", what_size=35, what_color="#FFFFFF", what_outlines=[(2, "#7800A3", 0, 0)], who_color="#FFFFFF", who_outlines=[(2, "#7800A3", 0, 0)])

define nobody_sammy_father = Character("???", what_font="gui/fonts/comic.ttf", what_size=35, what_color="#FFFFFF", what_outlines=[(2, "#0056c0", 0, 0)], who_color="#FFFFFF", who_outlines=[(2, "#0056c0", 0, 0)])
define sammy_father = Character("Мистер Коллинз", what_font="gui/fonts/comic.ttf", what_size=35, what_color="#FFFFFF", what_outlines=[(2, "#0056c0", 0, 0)], who_color="#FFFFFF", who_outlines=[(2, "#0056c0", 0, 0)])
define sammy_mother = Character("Миссис Коллинз", what_font="gui/fonts/comic.ttf", what_size=35, what_color="#FFFFFF", what_outlines=[(2, "#A40000", 0, 0)], who_color="#FFFFFF", who_outlines=[(2, "#A40000", 0, 0)])

define tv_host = Character("Ведущий", what_font="gui/fonts/comic.ttf", what_size=35, what_color="#FFFFFF",what_outlines=[(2, "#000000", 0, 0)], who_color="#FFFFFF",who_outlines=[(2, "#3700ae", 0, 0)])

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
    "fahr_answer": "Айрин, правила сдерживания существуют не просто так. Их нарушения уже ранее приводили к ошибкам.",
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
    "text": "У нас уже есть зацепки, чтобы добыть информацию. Откинем страхи и сомнения, чтобы сделать все правильно.",
    "fahrenheit": -1,
    "monument": 0,
    "planar": 1,
    "fahr_answer": "Это так не работает. План не может быть хорошим, если не учитывает эмоции и переживания.",
    "mon_answer": "...",
    "plan_answer": "Вот это то, с чего действительно можно было бы и начать."},

    {"title": "Марк может анализировать местность",
    "text": "Пусть Стражи команды Легион лучше в расследованиях, но зато у нас есть Марк, способный анализировать местность.",
    "fahrenheit": -1,
    "monument": 0,
    "planar": 1,
    "fahr_answer": "Способность Марка имеет ограничения по расстоянию. Нужно будет знать хотя бы где искать.",
    "mon_answer": "...",
    "plan_answer": "А это дельная мысль. Я могу значительно ускорить поиски."},

    {"title": "СМИ свяжут провал с нами",
    "text": "СМИ уже зафиксировали тот случай в школе, где была я и Алиса. Мы подорвём свою репутацию в обществе, если ничего не сделаем.",
    "fahrenheit": 0,
    "monument": -1,
    "planar": 1,
    "fahr_answer": "...",
    "mon_answer": "Я не против иногда подстраиваться под репортёров. Но не рисковать же всем ради них.",
    "plan_answer": "Да, спорить не буду. Если справимся - это было бы выгодно."},

    {"title": "Это важный опыт для нас",
    "text": "Действуя осторожно, даже если мы не найдём Сэмми, мы сможем получить необычайно важный опыт.",
    "fahrenheit": 0,
    "monument": -1,
    "planar": 1,
    "fahr_answer": "...",
    "mon_answer": "Не-не-не. Либо мы настраиваемся на успех, либо к чёрту это всё.",
    "plan_answer": "Если сочетать это с нашими дежурствами и не палиться, звучит и вправду как беспроигрышный вариант."},
]

define used_arguments = []

transform swirl:
    linear 0.01 zoom 3.0  # Поворот на 360 градусов и увеличение в 2 раза за 10 секунд
    linear 0.01 zoom 1.0    # Возврат к исходному состоянию
    repeat

transform reset:
    zoom 1.0  # Устанавливает стандартный масштаб
    rotate 0  # Устанавливает стандартный угол поворота
    xalign 0.5  # Горизонтальное выравнивание по центру
    yalign 0.5  # Вертикальное выравнивание по центру

label act_second_ronin_office:

    hide background
    hide character

    stop music
    play music basement_music loop volume 0.6
    show act_second_ronin_office_cabinet as background

    # jump act_second_arguments_conversation
    # jump act_second_arguments_debate_prepare
    # jump act_second_arguments_debate
    # jump act_second_next_move
    # jump act_second_resonance_deal
    # jump act_second_resonance_defend
    # jump act_second_legion_defend
    # jump act_second_resonance_walking
    # jump act_second_legion_walking
    # jump act_second_sammy_home_with_alice
    jump act_second_sammy_home_alone
    # jump act_second_teacher
    # jump act_second_teacher_gregor_house
    # jump act_second_teacher_gregor_forest
    # jump act_second_school_territory
    # jump act_second_wards_basement_after_investigation
    # jump act_second_night_base
    # jump act_second_night_base_battle
    # jump act_second_night_base_after_battle
    # jump act_second_ronin_cabinet_after_investigation
    # jump act_second_irene_career
    # jump act second_new_clue

    ronin "Войдите."

    hide character

    play sound door_open volume 1.0 channel "backsounds_channel"

    me "Мы вошли в уже хорошо знакомый мне кабинет Ронина."

    me "Как и обычно, здесь стояла напряжённая атмосфера."
    
    me "В памяти всплывали бесконечные выговоры или нравоучения."

    show ronin_costume_no_mask_idle as character

    ronin "Я предполагаю, это не просто визит."

    ronin "Что вам нужно?"

    iam "Разве вы не слышали о том, что произошло около школы №12?"

    show monument_costume_no_mask_idle as character

    monument "Потенциальная угроза класса S."

    show fahrenheit_costume_no_mask_confused as character

    fahrenheit "Исчез мальчик из школы, где проходило наше дежурство."

    hide character
    
    iam "Сэмми Колинз."

    show ronin_costume_no_mask_idle as character

    ronin "Допустим."

    ronin "Хотите поделиться какой-то информацией?"

    iam "Я хочу чтобы мы занялись этим расследованием."

    me "Ронин даже не шевельнулся."

    me "Из-за костюма, который полностью закрывал его тело и лицо, он больше напоминал бездушную машину, нежели человека."

    ronin "Молодые люди..."

    ronin "Кажется вы здесь уже достаточно давно, чтобы понимать, что есть группы в Протекторате, специально созданные для подобных целей."

    ronin "Среди вас..."

    ronin "Стрелок 4, Контакт 4, Контакт 6 и Эпицентр 7."

    ronin "Среди вас ни одного Умника или Властелина."

    ronin "Думаю, мой ответ очевиден."

    ronin "НЕТ!"

    iam "Сэр, я и Алиса..."

    ronin "Что я говорил про гражданские имена в стенах Протектората?"

    me "В его голосе начало звучать раздражение."

    iam "Сэр, я и Фаренгейт были в тот день на месте незадолго до исчезновения подростка."

    iam "Он единственный из школьников, кто пропал в тот день."

    iam "Это же явно связанные друг с другом события."

    hide character

    me "Ронин ответил не сразу."

    me "Он отошел к окну и на некоторое время, словно, погрузился в размышления."

    show ronin_costume_no_mask_idle as character

    ronin "Искра, причастность к ситуации не меняет ваших способностей, навыков и опыта."

    me "Он произнёс это более мягко, чем я ожидала."

    show monument_costume_no_mask_scream as character

    monument "Что, даже моего?"

    monument "Когда мы должны были обезвредить Рестарта, значит, у меня хватало опыта, а сейчас нет?"

    if game_state.act_first_weekend_place != 1:

        me "Что?"

        me "Разве Монумент участвовал в захвате Рестарта?"

        me "Я отчётливо помню, что за поимку были ответственны Титан и Азимут."

        me "Даже в кабинете, когда я пришла сюда в первый раз, на полке была соответствующая фотография."

        me "Жаль у меня не было времени достаточно пообщаться с Девидом, чтобы узнать в чём же тут дело."

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

    ronin "Планар, ещё раз я услышу использование гражданских имён, все объяснения закончатся."

    show fahrenheit_costume_no_mask_confused as character

    fahrenheit "Сэр, в отличие от других Героев и Стражей, у нас есть хоть какие-то зацепки."

    fahrenheit "Мы общались со школьным учителем, который нам доверяет."

    fahrenheit "А Айрин..."

    show ronin_costume_no_mask_idle as character

    ronin "ДА ВЫ ИЗДЕВАЕТЕСЬ!"

    show fahrenheit_costume_no_mask_confused as character

    fahrenheit "Простите..."

    fahrenheit "А Искра, по факту, прямой свидетель событий."

    show ronin_costume_no_mask_idle as character

    ronin "Я не запрещаю вам делиться информацией со Стражами Легион."

    ronin "Но не более."

    ronin "Мой ответ - НЕТ!"

    iam "Сэр..."

    ronin "Повторять не стану! Разговор окончен!"

    hide character

    me "Ронин оставался непреклонным, а его решение было железным."

    me "Дальше продолжать было бы бессмысленно."
    
    play sound door_open volume 1.0 channel "backsounds_channel"

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

    play sound door_close volume 1.0 channel "backsounds_channel"

    me "Разочарование и беспомощность витали в воздухе."

    # ЗВУК - УДАР ПО СТАЛИ

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

    planar "Как и всегда, в общем."

    hide character

    play sound sigh_female volume 1.0 channel "backsounds_channel"

    me "Алиса глубоко вздохнула, а Дэвид устало опёрся о стену, скрыв лицо в ладонях."

    show monument_costume_no_mask_idle as character

    monument "Я не хочу с этим мириться, но Марк, похоже, прав."

    monument "Ронин ожидает от нас беспрекословного исполнения задач, не давая шагнуть в сторону."

    monument "Если сделаем по своему, потом хоть до посинения будем доказывать, что хотели как лучше."

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
        
        hide character

        iam "Вектора?"

        show monument_costume_no_mask_idle as character

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

    fahrenheit "И вот теперь, когда появилась возможность сделать что-то по-настоящему значимое..."

    fahrenheit "Нас заставляют притворяться, будто мы не имеем к этому отношения."

    hide character

    me "Я присела рядом с Дэвидом, чувствуя тяжесть момента."

    me "Тишина в комнате становилась почти осязаемой."

    me "Готова ли я согласиться с Ронином?"

    me "Нет, это не вариант."

    me "Возможно, в произошедшем есть и моя вина."

    me "Может Сэмми сбежал и попал в беду потому, что я приняла неверные решения?"

    me "В моей голове мелькают альтернативные сценарии того дня, и каждый из них ведёт к разным исходам."

    if game_state.attack_teen:

        me "Стоило ли мне бить того подростка?"

        me "Может убеждение имело бы больший вес и не настолько бы накалило обстановку?"

    if not game_state.attack_teen:

        me "Я пыталась запугать подростка, но ничего не вышло в итоге."

        me "Стоило ли действовать более решительно?"

    me "А после появления Резонанса..."

    me "Точно! Резонанс!"

    me "В моей памяти возникла фигура кейпа в белом костюме."

    me "Мысли плавно переключились на воспоминание о встречи с Резонансом в больнице."

    if game_state.hospital_use_power:

        me "Я вспомнила о сделке, которую он мне предложил."

        me "Я совру, если скажу, что это волнует меня меньше, чем пропавший ребёнок."

        me "Права ли Софи?"

        me "Станет ли непоправимой ошибкой моя попытка договориться с суперзлодеями?"

        me "Или же это та возможность, которая подарит надежду на выздоровление Нэнси?"

        me "А может ему что-то известно о пропавшем?"

        me "Ведь Резонанс применил Силу, чтобы дать мальчику сбежать от его мучителей."
        
        me "Шанс что-то узнать от суперзлодея кажется мне крошечным, но всё-таки не нулевым."

    if not game_state.hospital_use_power:

        me "Я вспомнила о ситуации, где я оказалась максимально беспомощной."

        me "Не смогла дать злодеям отпор, только потому что нарушила бы правила, ибо была не в костюме."

        me "И вот сейчас, мы также боимся нарушить правила, когда пропавший мальчик может нуждаться в нашей помощи."

    me "Если я смогу убедить других взяться за это расследование, у нас появится возможность изменить ход событий."

    me "Возможно, это наш шанс совершить что-то более героическое, чем просто носить цветные костюмы."

    me "Я должна найти аргументы."
    
    me "Достаточно убедительные, чтобы мотивировать ребят действовать."

    me "Действовать, несмотря на запрет Ронина и страх потерять своё место в Протекторате."

    show fahrenheit_costume_no_mask_confused as character

    me "Алиса."

    show monument_costume_no_mask_idle as character

    me "Девид."

    show planar_costume_no_mask_angry as character

    me "Марк."

    hide character

    me "Все такие разные."

    me "Сложно будет убедить всех."

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

        play sound footsteps_walking volume 1.0 channel "backsounds_channel"

    if monument_belief >= 0:

        $ game_state.monument_is_ready = True

        monument "К чёрту Ронина, я хочу это сделать и мне плевать на этот запрет."

    else:

        $ game_state.monument_is_ready = False

        monument "Хотел бы я верить, что нам хватит решительности найти парня..."

        monument "Справиться с кейпом класса S, ни смотря ни на что."

        monument "Но не могу."

        monument "Мы рискуем не только распадом команды, но и позорным поражением."

        monument "Извините, но я не готов."

        hide mon_character

        play sound footsteps_walking volume 1.0 channel "backsounds_channel"

    
    if planar_belief >= 0:

        $ game_state.planar_is_ready = True

        planar "Если мы будем придерживаться чёткого и проработанного плана - я согласен."

    else:

        $ game_state.planar_is_ready = False

        planar "Всё что у нас есть сейчас - это эмоции."

        planar "А значит, мы обречены на провал."

        planar "Сори, я пас."

        hide plan_character

        play sound footsteps_walking volume 1.0 channel "backsounds_channel"


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

        fahrenheit "Вероятно, мы найдём там немало подсказок."

        if not game_state.monument_is_ready:

            fahrenheit "Также можно разузнать что-нибудь у учителя из той школы."

            fahrenheit "Думаю он сможет нам помочь с тем, чтобы найти тех подонков из школы, которые издевались над Сэмми."

        if not game_state.planar_is_ready:

            fahrenheit "А ещё было бы неплохо исследовать местность вокруг школы."

    if game_state.monument_is_ready:

        show monument_costume_no_mask_idle as character

        monument "Мистер Террел - школьный учитель."

        monument "Ты и Алиса с ним уже общались, он может быть настроен на сотрудничество с нами."

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

            planar "Думаю он сможет дать дополнительную информацию и адреса как пропавшего, так и тех кто над ним издевался."

        if not game_state.monument_is_ready:

            planar "А ещё было бы неплохо наведаться к родителям Сэмми."

            planar "Мы сможем немало узнать о его жизни и это может быть важной зацепкой."
            
    if not game_state.fahrenheit_is_ready and not game_state.monument_is_ready and not game_state.planar_is_ready:

        me "Я осталась одна."

        me "Не ожидала, что меня никто не поддержит, но я могу их понять."

        me "Теперь это только моё дело и я ответственна только за свои решения."

        me "Я достала листок бумаги и принялась делать заметки."

        me "Номер один - дом Сэмми, я могу найти там ценные улики, а также узнать информацию от его родителей."
        
        me "Адрес будет не так сложно найти."

        me "Номер два - школьный учитель Мистер Террел."

        me "Думаю он пойдёт на сотрудничество."
        
        me "Он сможет рассказать как о Сэмми, так и о тех ублюдках, которые над ним издевались."

        me "Узнаем, что там произошло между подростками."

        me "Номер три - исследовать закрытую территорию рядом со школой."

        me "Если проникнуть внутрь, в то место, где аномалия, есть шанас найти полезные зацепки."

    hide character

    me "Итак..."

    me "Дом Сэмми, в школу к мистеру Теллеру, а затем попытаться попасть на закрытую территорию."

    me "Отлично."

    me "Вот только одна деталь."

    me "Стоит ли включать в мой план поиск Резонанаса?"

    me "Софи недвусмысленно намекала, чем могут закончится сделки с суперзлодеями."

    me "Но всё же, это может быть важно не только для меня, не только для расследования, но и для Ненси."

    me "Я должна сейчас решить, стоит ли ввязываться во всё это."

    menu:

        "Спланировать встречу с Резонансом":

            $ game_state.resonance_deal_agree = True

            me "Так или иначе, мне нужны деньги, чтобы содержать Ненси."

            me "Если дела в Протекторате пойдут так и дальше - я вряд ли смогу получать достаточно средств, чтобы платить за её лечение."

            me "Кроме того, если Резонанс говорил правду, отказ от сделки может стать приговором не только для меня, но и для больницы."

            me "Я обаязана пойти на эту встречу."

            if game_state.fahrenheit_is_ready or game_state.monument_is_ready or game_state.planar_is_ready:

                me "Только вот будь я одна, мне бы не пришлось ничего никому объяснять."

                me "Сейчас же, придётся выкручиваться."

                iam "Поняла."

                iam "Дом Сэмми, мистер Теллер и закрытая территория."

                iam "Только первым делом, я отправлюсь в западную часть города."

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

                    show planar_costume_no_mask_idle as character

                    planar "Да уж, вообще не звучит как что-то, что мне нравится."

                    planar "Ты уверена, что готова пойти туда?"

                hide character

                iam "Знаю-знаю, но я не могу исключать причастность Резонанса."

                iam "Я понимаю на что иду и буду действовать аккуратно."

                iam "Всё чего прошу - довериться мне!"

                me "Мне жаль, что я не могу рассказать об истинной этого этапа плана."

                me "По крайней мере сейчас."

                if game_state.fahrenheit_is_ready:

                    show fahrenheit_costume_no_mask_confused as character

                    fahrenheit "Я просто не могу отпустить тебя туда одну."

                    iam "То что я делаю - это ещё более грубое нарушение правил и только я возьму на себя эту ответственность."

                    fahrenheit "Айрин..."

                    iam "Я всё сказала!"

                    hide character

                    me "Это было странно."

                    me "Примерно так с нами и разговаривал Ронин."

                    me "Может ему также есть что скрывать, как и мне сейчас?"

                    show fahrenheit_costume_no_mask_confused as character

                    fahrenheit "Будь по твоему, только не забывай про осторожность."

                    iam "Обещаю."

                if game_state.monument_is_ready:

                    show monument_costume_no_mask_idle as character

                    monument "Отговаривать тебя бессмысленно? Может мне стоит пойти с тобой?"

                    iam "Девид, я справлюсь."

                    iam "Если мы все сразу пропадём из зоны видимости, Ронин что-то заподозрит."

                    monument "Хорошо, как знаешь."

                if game_state.planar_is_ready:

                    show planar_costume_no_mask_idle as character

                    planar "Это безумие."

                    planar "Полное."

                    planar "Но зная твоё упрямство, не вижу смысла тратить силы, чтобы переубеждать."

                    planar "В любом случае, будь готова связаться с Протекторатом в случае критической опасности."

                    iam "Хорошо, Марк, я учту."

        "Проигнорировать предложение Резонанса":

            $ game_state.resonance_deal_agree = False

            me "Софи безусловно права."

            me "Кто знает, что он задумал и что со мной сделают на вражеской территории."

            me "Может быть это вообще какая-то хитрость, чтобы получить важные сведения как от члена Протектората."

            me "Я не забыла, что суперзлодеи угрожали мне последствиями."

            me "Но, ведь я для того и вступила в Стражи, чтобы противостоять таким обстоятельствамю"

            iam "Поняла."

            iam "Дом Сэмми, мистер Теллер и закрытая территория."

    hide character

    me "Решение принято."

    me "Я могу потерять статус, быть уволенной, а также попасть в реальную опасность."

    me "Но почему-то ощущение, что я делаю всё правильно, не покидает меня."

    me "Моё первое настоящее задание в качестве Стража."

    me "И я сделаю всё что в моих силах!"

    if game_state.resonance_deal_agree:

        jump act_second_resonance_deal

    if not game_state.resonance_deal_agree:

        if game_state.fahrenheit_is_ready:

            jump act_second_sammy_home_with_alice

        if not game_state.fahrenheit_is_ready:

            jump act_second_sammy_home_alone

    return

label act_second_resonance_deal:

    hide background
    hide character

    stop music
    play music west_city_music loop volume 0.6
    show act_second_west_city_initial_street as background

    me "Я добралась до западной части города."

    me "Вся служба нашей команды Стражей проходила в чётко очерченных районах."

    me "Выходные я, в основном, проводила у себя - в Нижнем Городе."

    me "Поэтому я уже и забыла, что вообще здесь происходит."

    me "Людей на улицах значительно меньше, чем в местах где я обычно бываю."

    me "Странным мне показалось не их количество, а то, как они сторонятся друг друга."

    me "Я осознавала, что они смотрят на меня, пытаясь понять, что Страж Протектората мог забыть в таком месте?"

    me "Я не знала точно, куда именно мне идти."

    me "Рассчитывала, что злодеи сами меня найдут."

    me "Так и случилось."

    play sound whiz volume 0.6 channel "backsounds_channel"

    me "Раздался знакомый высокочастотный звук."

    show resonance_costume_mask_idle as character

    resonance "Приветствую."

    resonance "Я понимаю, что воздействие моей способности может доставлять дискомфорт."

    resonance "Тем не менее, искренне рад тебя видеть."

    iam "Понятия шантаж и \"искренне рад видеть\" - не очень сочетаются друг с другом."

    resonance "Айрин, последнее чего бы мне хотелось, это тебя задеть."

    resonance "Воспринимай это как взаимовыгодное предложение."

    iam "А обязательно называть меня по имени?"

    resonance "Мне казалось так звучит более эмпатично."

    iam "Эмпатично - это когда оба собеседника знают имена друг друга."

    me "Он наклонил голову и, казалось, о чём-то задумался."

    me "А затем протянул мне руку."

    resonance "Эрик."

    resonance "Приятно познакомиться."

    me "Что? Вот так просто?"

    me "Должна признать, он меня ошарашил."

    me "Хотя он мог назвать вообще любое случайное имя..."

    me "Что-то мне подсказывало, что он не врёт."

    play sound hugging volume 0.8 channel "backsounds_channel"

    me "Я протянула руку в ответ."

    iam "И куда теперь?"

    resonance "В \"Falcon Bright\". Местное заведение."

    me "Страж Протектората на встрече с суперзлодеем в дневное время суток."

    me "Почему бы не сделать ситуацию ещё более абсурдной?"

    iam "Приглашаешь на ужин?"

    resonance "Я не против, но, думаю, будут дела гораздо интересней."

    me "Не успела я задать логичный вопрос \"как мы собираемся пройти вот так вместе, рискуя быть замеченными\"?"

    me "Резонанс схватил меня за руку и я испытала целый спектр неведомых ранее ощущений."

    show act_second_west_city_initial_street as background at swirl

    $ play_whiz()

    me "Окружение стремительно менялось и искажалось."

    me "Я ощущала огромное количество объектов, работающих на электричестве, пролетающих вокруг меня."

    me "Мой мозг предательски пытался собрать информацию о каждой мимолётной искре."

    me "От этого у меня сильно заболела голова."

    show act_second_falcon_bright_bar as background at reset

    stop sound channel "backsounds_channel"

    me "Буквально через несколько секунд мы оказались внутри какого-то потрёпанного заведения с немногочисленными посетителями."

    hide character

    me "Стены \"Falcon Bright\" были выкрашены в тёмно-коричневые тона, тусклые лампы подчёркивали контуры старой мебели."

    me "Слабый древесный запах смешивался с ароматами спиртных напитков и дыма от сигар."

    me "Здесь явно требовался капитальный ремонт, чтобы это место можно было назвать рестораном."

    me "Я обратила внимание на людей."

    me "Казалось, их абсолютно не интересует происходящее, как будто подобное случается регулярно."

    show resonance_costume_mask_idle as character

    me "Резонанс жестом поприветствовал бармена, который ответил ему тем же."

    play sound footsteps_walking volume 1.0 channel "backsounds_channel"

    me "Затем мы проследовали к двери в подсобку."

    hide character

    show act_second_falcon_bright_door as background

    me "Длинный коридор вёл к закрытому помещению, где, судя по звукам, находилось минимум четыре человека."

    play sound knock volume 1.0 channel "backsounds_channel"

    me "Резонанс постучал в дверь в каком-то определённом ритме, после чего она отворилась."

    play sound door_open volume 1.0 channel "backsounds_channel"

    me "К нам вышел парень чуть ниже меня."

    me "Чёрный костюм с изображением стрелок, направленных в разные стороны."

    me "Красные линзы."

    me "Моему удивлению не было предела, ведь я мгновенно поняла кто это."

    me "Это был Вектор."

    show vector_mask_half_opened_idle as character

    vector "Ох, ничего себе!"

    show vector_mask_half_opened_smile as character

    vector "Это у нас пополнение?"

    vector "Тяжело быть подчинённым Ронина."

    vector "Одно не верное движение и тебя вышвыривают."

    iam "Что ты вообще тут делаешь?"

    iam "Ты же был Стражем?"

    vector "Ну да."

    vector "Как и ты."

    iam "Я и сейчас Страж."

    vector "Аааа..."

    vector "А сюда просто на чай заскочила?"

    iam "Я выполняю свою работу."

    vector "А, хорошо, держу в курсе, перед тобой суперзлодей."

    vector "Внутри суперзлодеи."

    vector "А ещё один суперзлодей слева от тебя."

    vector "Будешь выполнять работу?"

    show resonance_costume_mask_idle as character

    resonance "Хватит."

    resonance "У нас нет времени наслаждаться твоим искромётным юмором."
    
    resonance "Мы пришли к боссу."

    hide character

    me "Вектор, сохраняя на своём лице ехидную насмешку, молча направился к двери."

    me "Бесит он."

    me "И, справедливости ради, думаю, что это взаимно."
    
    play sound door_open volume 1.0 channel "backsounds_channel"

    me "Вектор открыл дверь и с нарочитой вальяжностью пропустил нас вперёд."

    show act_second_falcon_bright_collectors_room as background

    play sound door_close volume 1.0 channel "backsounds_channel"

    me "Это было небольшое помещение."

    me "Его освещали лишь несколько старых лампочек."

    me "У дальней стены сидели несколько человек в костюмах."

    me "Один из них в белом, почти таком же как у Резонанса."

    me "Справа от него - девушка в коротком платье и с форфоровой маской на лице."

    me "Открытые руки были почти полностью покрыты татуировками."

    me "Из всех присутствующих я смогла узнать только Вакуум, которая восседала в центре."

    me "А затем..."

    me "Я увидела его."

    show collector_costume_mask_idle as character

    stop music

    me "Массивный мужчина в сером плаще, белой рубашке с галстуком."

    me "Его можно было бы принять за гражданского."

    me "Если бы не одно но..."

    me "Маска хищной птицы, полностью скрывающая лицо."

    me "Коллектор."

    play music collector_music loop volume 0.6

    me "Я заметила, что перчатка у него только одна - на левой руке."

    me "Правая была оголённой."

    show collector_costume_mask_idle as character

    play sound footsteps_running volume 1.0 channel "backsounds_channel"

    me "Не успела я и осознать почему, как Коллектор молниеносным движением сократил расстояние со мной до минимума."

    me "А затем легко прикоснулся голой рукой к моей щеке."

    me "Я была в полной уверенности, что открытых участков в костюме Стража быть не должно."

    me "Ёбаный Джефф и его идеи."

    hide character

    play sound hit_miss volume 1.0 channel "backsounds_channel"

    me "Не прошло и секунды, как Коллектор отпрыгнул на несколько метров назад."

    play sound short_electricity volume 3.0 channel "backsounds_channel"

    me "Я собрала электричество и с ужасом обнаружила, что с моей силой что-то не так."

    me "Я всё ещё могла контролировать электроэнергию, но перестала понимать её форму и мощность."

    iam "Что ты сделал со мной?"

    show collector_costume_mask_idle as character

    collector "Добавил нашему разговору мотивации."

    iam "Вы думаете, что я не справлюсь с вами всеми?"

    collector "Нет, я не думаю, что ты справишься с нами всеми."

    me "Дурацкая была провокация с моей стороны."

    me "Даже Вакуум смогла в одиночку одолеть меня в тот раз в больнице."

    me "Не говоря уже о Резонансе и прочих членах группировки."

    play sound short_electricity volume 3.0 channel "backsounds_channel"
    
    me "Я попыталась вернуть электричество на место..."

    play sound breaking_glass volume 2.0 channel "backsounds_channel"
    
    me "Только вот переборщила с напряжением из-за чего часть лампочек замигала, а одна из них и вовсе лопнула."

    iam "Что ты со мной сделал?"

    collector "У тебя очень интересным образом работает мозг."

    collector "Не стоит переживать."

    collector "Я верну тебе этот навык как только ты выполнишь свою часть договора."

    collector "Кроме того, мои люди и дальше будут обеспечивать сохранность больницы и также выделять деньги на лечение твоей подруги."

    iam "Но мне нужно будет сделать какую-то очень стрёмную вещь, верно?"

    collector "Я бы так не сказал."

    collector "Мне нужна простая информация об одном герое."

    collector "Имя и фамилия - не более."

    iam "Если ты про Ронина, я понятия не имею о его гражданской личности."

    me "Он едва слышно рассмеялся."

    collector "Нам не интересен бывший японский приступник, который решил поиграть в героя."

    iam "Что блять?"

    collector "Это не имеет никакого отношения к делу."

    collector "Меня интересует кое-кто другой."

    collector "Тот кто называет себя Азимутом."

    iam "Зачем вам нужна его личность?"

    collector "Ты ожидаешь, что я отвечу на этот вопрос?"

    iam "Нет."

    collector "Но всё же спросила..."

    collector "И мне не сложно ответить."

    collector "Скажи мне, зачем существует СКП?"

    iam "Организация, которая регулирует деятельность супергероев на территории США."

    iam "Основным принципом Протектората является подчинение человеческому правительству."

    me "Я отчеканила это достаточно легко, так как это то, что любой Страж обязан знать наизусть."

    me "Естественный страх обычных граждан, что люди со сверхспособностями будут использовать свои Силы, чтобы захватить власть."

    me "Достаточно острая тема в обществе."

    collector "А если скажу, что есть подозрение, что гражданская личность Азимута - это один из тайных сотрудников СКП."

    me "Это уж слишком."

    iam "Долго думали над такой невероятной легендой?"

    collector "Я сказал тебе правду. Верить или нет - твоё дело."

    collector "Как только ты предоставишь информацию его личности..."

    collector "Ты получишь назад свой навык, а мои люди будут обеспечивать больницу всем необходимым."

    collector "Обеспечивать сколько потребуется."

    me "Я злобно посмотрела на Резонанса."

    iam "Это что угодно, но только не переговоры."

    show resonance_costume_mask_idle as character

    resonance "Не поддавайся эмоциям, мы обсудим это."

    show collector_costume_mask_idle as character

    collector "Вот и прекрасно."

    collector "Условия ясны."

    collector "А сейчас я вынужден заняться своими делами."

    hide character

    play sound footsteps_walking volume 1.0 channel "backsounds_channel"

    iam "Стойте, у меня есть ещё один вопрос!"

    show collector_costume_mask_idle as character

    me "Коллектор вновь обернулся в мою сторону."

    collector "Говори."

    iam "В городе случилось что-то странное."

    iam "Территорию рядом со школой №12 оцепили из-за какой-то \"аномалии\"."

    iam "Кроме того, пропал ребёнок."

    collector "Мне известно об этом."

    collector "Такое случается, но паника преувеличена."

    iam "В смысле преувеличена? Пропал ребёнок. Нужно что-то сделать."

    resonance_voice "Айрин, что ты делаешь?"

    me "Это было странно..."

    me "Я слышала голос Резонанса словно у себя в голове."

    collector "Прости, девочка, но мы не поисковая бригада."

    collector "Это уже твоя работа."

    iam "Я понимаю, но если здесь замешан кейп угрозы класса S, это коснётся не только Протектората."

    collector "Если у меня будут доказательства, что угроза действительно реальна..."

    collector "Мы займёмся этим и без приглашения Протектората."

    collector "А теперь, я прошу оставить нас."

    hide character

    play sound footsteps_walking volume 1.0 channel "backsounds_channel"

    me "Вектор открыл дверь, и мы с Резонансом покинули логово Коллектора, а затем и сам бар."

    stop music

    play sound door_close volume 1.0 channel "backsounds_channel"

    play music basement_music loop volume 0.6
    show act_second_west_city_initial_street as background

    me "Мы вышли через чёрный ход на безлюдную улицу."

    me "Я пыталась идти как можно быстрее, чтобы оторваться от Резонанса."

    show resonance_costume_mask_idle as character

    resonance "Подожди, послушай."

    hide character

    me "Я не собиралась останавливаться, но он был быстрее."

    iam "Ты подставил меня."

    iam "Пиздец как подставил."

    show resonance_costume_mask_idle as character

    resonance "Неужели было более удачное решение для того, чтобы защитить больницу и дорогого тебе человека?"

    iam "Может было, а может и нет."

    iam "Плевать."

    iam "Ты хоть осознаёшь, что он от меня требует?"

    iam "Подставить героя Протектората."

    iam "Меня вышвырнут к чертям собачьим."

    resonance "То есть, даже если ты достоверно узнаешь, что Азимут нарушает один из главных постулатов вашей организации, ты всё ещё захочешь там оставаться?"

    me "Вопрос был, безусловно, хорошим."

    me "Я даже не искала на него ответ, потому что поверить в это было невозможно."

    me "Азимут участвовал в поимке неисчислимого количества суперзлодеев."

    me "И тут я вспомнила историю про Рестарта."

    me "Чёрт. Неужели это может быть правдой?"

    resonance "Я искренне считал, что эта сделка будет лучшим решением."

    resonance "А мотивация босса, как мне казалось, должна быть тебе близка."

    iam "Только в том случае, если сказанное - правда."

    resonance "Сделанного уже не изменить."

    resonance "Я не могу заставлять тебя действовать, но ты сама понимаешь, что стоит на карте."

    me "Я собиралась с мыслями, чтобы сказать всё, что я о нём думаю."

    stop music

    me "Но наша беседа прервалась..."

    hide character

    play music legion_battle_music loop volume 0.6

    play sound hugging volume 0.8 channel "backsounds_channel"

    me "В мгновение ока Резонанс оказался за моей спиной и крепко схватил меня, закрыв мне рот рукой."

    play sound long_electricity volume 1.0 channel "backsounds_channel"

    me "Я быстро извлекла электричество из всего что находилось неподалёку."

    me "Вот только управление давалось мне гораздо сложнее чем раньше."

    me "Резонанс легко увернулся от каждого импульса, не ослабляя свою хватку."

    me "В этот момент, я увидела, что мы на этой улице не одни."

    show legion_angry as character_left at left_side
    show legion_angry as character at center_side
    show legion_angry as character_right at right_side

    legion "Что это ты делаешь?"

    me "Три тела Легион стояли перед нами, держа перед собой свои алебарды."

    hide character_left
    hide character_right

    show resonance_costume_mask_idle as character

    resonance "Удерживаю вашего Стража, которая пыталась совать нос не в свои дела."

    show legion_idle as character

    legion "Пришла в одиночку в западный город?"

    show legion_angry as character

    legion "Ты меня за идиотку держишь?"

    show resonance_costume_mask_idle as character

    resonance "Что уж поделать, ваши Стражи хотят геройствовать и ловить суперзлодеев."

    show legion_angry as character_left at left_side
    show legion_angry as character at center_side
    show legion_angry as character_right at right_side

    legion "Отпустил её сейчас же или я не буду сдерживаться!"

    me "Эту фразу произнесло каждое из тел Легион, что звучало более устрашающе."

    hide character_left
    hide character_right

    show resonance_costume_mask_idle as character

    resonance "С радостью, как только вы отойдёте на расстояние, которое не вызывает у меня дискомфорт."

    hide character

    me "Два тела Легион распределились по улице так, чтобы окружить Резонанса."

    me "Она была готова атаковать в любой момент"

    me "Не успела я и обдумать происходящее, как в голове прозвучал голос..."

    resonance_voice "Не беспокойся."
    
    resonance_voice "Я не причиню тебе вреда."

    resonance_voice "Сейчас нужно убедить её отступить."

    resonance_voice "Как только она отойдёт, я отпущу тебя и скроюсь."

    resonance_voice "Скажешь ей, что пыталась меня поймать и угодила в ловушку."

    resonance_voice "Получишь выговор, но вряд ли последствия будут серьёзными."

    resonance_voice "Мы оба останемся в выигрыше."

    show legion_angry as character

    legion "Я даю тебе десять секунд, чтобы ты её отпустил."

    show resonance_costume_mask_idle as character

    resonance "Как только каждое из ваших тел отойдёт на двадцать шагов."

    show legion_surprised as character

    me "Я заметила как тела Легион синхронно переминались с ноги на ногу."

    me "Словно у неё не было понимания как действовать дальше."

    me "Кроме того, она упорно смотрела на меня, словно ожидая, что я начну действовать."

    me "Что же мне делать?"

    me "Я могу крикнуть, что суперзлодеи что-то сделали с моей Силой."

    me "Это практически правда."

    me "Вполне возможно, это заставит её отступить, как Резонанс и требует."

    me "План имеет смысл."

    me "А что если..."

    me "Если я просто помогу Легион захватить Резонанса?"

    me "Да, электричество будет контроллировать сложнее, но Резонанс не будет ожидать от меня атаки."

    me "И после этого, мы с Легион будем иметь преимущество в бою."

    me "Я смогу получить награду за задержание."

    me "Обставить это как собственную продуманную операцию."

    me "Легион, Ронин и остальные герои будут относиться ко мне гораздо серьёзней."
    
    me "Вот только, будет ли это правильно?"

    me "Времени совсем немного."

    me "Мне нужно срочно выбрать что делать."

    menu:

        "Заставить Легион отступить":

            iam "Легион."

            iam "Они что-то сделали с моей силой."

            iam "Прошу вас..."

            iam "Сделайте как он хочет."

            me "Я увидела разгневанное лицо Легион."

            me "И что-то мне подсказывало, что этот гнев был направлен в мою сторону."

            me "Каждое из тел Легион начали медленно отступать."

            me "Шаг за шагом."

            resonance_voice "Это был правильный выбор."

            resonance_voice "Ещё увидимся."

            me "Резонанс отпустил меня, а затем раздался характерный звук его способности."

            me "Легион ринулась вперёд, стараясь успеть метнуть оружие в суперзлодея."

            me "Но она отошла слишком далеко, чтобы иметь хоть какие-то шансы на успех."

            me "В следующую же секунду Резонанс исчез."

            me "Два тела Легион помчались дальше по улице."

            me "А одно из её тело, осталось рядом со мной."

            show legion_angry as character

            legion "Это было безответственно, Искра."

            legion "Ты нарушила правила, подвергла себя опаности и создала ситуацию, в которой я, как герой Протектората, показала слабость."

            iam "Простите, я просто была готова схватить его."

            iam "Но не догадывалась, что окажусь в ловушке."

            hide character

            me "Она ничего не ответила мне, а лишь развернулась и жестом указала мне идти за ней."

            jump act_second_resonance_defend

        "Атаковать Резонанса":

            me "Что бы ни случилось, если я выполню свой долг Стража и помогу поймать суперзлодея - все ошибки будут мне прощены."

            me "Кто знает, возможно я смогу добиться определённых условий для больницы и содержания Ненси у Протектората."

            me "Да, Коллектор не отдаст мне мой навык, но я постараюсь развить его вновь."

            me "Зато суперзлодей в плену может стать отлиным рычагом давления."

            play sound long_electricity volume 1.0 channel "backsounds_channel"

            me "Я собрала огромное количество электричества из всего что было вокруг."

            me "В домах один за другим гас свет."

            resonance_voice "Что ты делаешь?"

            me "В следующую секунду, я сформировала импульс, который оказался достаточно быстрым, чтобы застать Резонанса врасплох."

            me "Я освободилась от его хватки, а он отлетел на несколько метров и упал на землю."

            resonance_voice "Это была ошибка!"

            me "Ужасный звук в моей голове."

            me "Я едва держалась на ногах, но изо всех сил старалась создавать электрические барьеры, не давая Резонансу сбежать."

            me "Все тела Легион мгновенно приблизились к суперзлодею."

            play sound hit_success volume 1.0 channel "backsounds_channel"

            me "Последовал сильный удар рукояткой алебарды."

            stop music

            me "Стало тихо."

            me "Резонанс лежал в отключке недалеко от нас."

            show legion_idle as character

            legion "Не буду спрашивать тебя какого чёрта ты тут забыла."

            legion "Главное, что ты проявила себя как боец."

            iam "Благодарю, для меня это очень важно."

            me "Теперь уже не знаю, так ли это."

            hide character

            play sound footsteps_walking volume 1.0 channel "backsounds_channel"

            me "Легион взвалила суперзлодея на плечо и вместе мы с ней устремились прочь из западной части города."

            jump act_second_legion_defend

    return

label act_second_resonance_defend:

    jump act_second_resonance_walking

    return

label act_second_legion_defend:

    jump act_second_legion_walking

    return

label act_second_resonance_walking:

    hide character
    hide background

    me "Мы долго шли по улица западного города."

    me "Я не решалась сказать что-либо, боясь сделать только хуже."

    show act_second_bridge as background at reset

    me "Когда мы добрались до моста, который вёл в центр, Легион повернулась ко мне."

    show legion_surprised as character

    legion "Я могу тебя понять, ты хотела себя проявить."

    legion "И всё же - это не поведение Стража."

    iam "Я понимаю."

    legion "Хорошо если так."

    legion "Но это не защитит тебя от последствий."

    legion "Я не буду докладывать об этом происшествии, но только если того не потребует ситуация."

    legion "Постарайся в ближайшее время не совершать ничего, что привлекает внимание."

    legion "Иначе, прошу меня простить."

    me "Я молча кивнула."

    hide character

    $ play_running()

    me "Легион развернулась и быстрым шагом пошла дальше."

    me "Я же осталась на месте, словно ощущение неудачи стало слишком тяжёлой ношей в данный момент."

    me "Я окинула взглядом вид с моста."

    me "Ясное небо, река, вдалеке парк..."

    stop music

    me "Стоп."

    play music creepy_music loop volume 0.6

    me "Мой взгляд приковал железный купол."

    me "Который был мне хорошо знаком."

    play sound sigh_female volume 1.0 channel "backsounds_channel"

    me "Дыхание стало прерывистым."

    me "Всё тело задрожало."

    me "Я хотела отвести взгляд, броситься прочь..."

    me "Вот только, это проклятое место словно парализовало меня."

    show resonance_costume_mask_idle as character

    resonance "Ты в порядке?"

    play music basement_music loop volume 0.6

    me "Резонанс возник словно из ниоткуда."

    me "Он хотел подойти ближе, но я подняла руку перед собой, преграждая ему путь."

    hide character

    me "Резонанс сделал шаг назад и терпеливо ждал."

    me "Я глубоко вдохнула воздух в грудь, а затем медленно начала выдыхать"

    me "Прямо как в курсе по медитации, который я смотрела полгода назад."

    play sound sigh_female volume 1.0 channel "backsounds_channel"

    me "Ещё несколько дыхательных циклов и мне действительно удалось более-менее прийти в себя."

    show resonance_costume_mask_idle as character

    me "Затем я повернулась к Резонансу."

    iam "Как ты здесь оказался?"

    resonance "Очевидно было, что Легион выберет именно этот путь через мост."

    resonance "Я просто дождался момента."

    resonance "Хотел сказать спасибо, за то что подыграла мне."

    resonance "Иначе это могло бы плохо кончиться, как минимум для меня."

    hide character

    me "Я ничего не ответила."

    me "Больше всего, мне бы хотелось убраться отсюда, как можно раньше."

    show resonance_costume_mask_idle as character

    resonance "Неужели ты знаешь, что скрывает этот купол?"

    iam "Знаю."

    iam "Здесь произошёл мой триггер."

    me "Мне не нужно было видеть его лицо под маской."

    me "И так была уверена, что он поражён."

    me "Тема купола была под запретом."

    me "Я, как и многие другие, дала письменное обязательство никогда не раскрывать подробности изоляции бывшего детского приюта."

    hide character
    show act_second_bridge_down as background

    me "Я села на колени, чтобы не смотреть на купол."

    show resonance_costume_mask_idle as character

    resonance "Полагаю, что спрашивать о твоём триггере бессмысленно?"

    iam "Бессмысленно."

    iam "Ты всё правильно понял."

    resonance "Ну что ж..."
    
    resonance "Мне уйти или посидеть с тобой?"

    me "Я пожала плечами, честно говоря, у меня абсолютно не было сил принимать хоть какое-то решение."

    hide character

    me "Он присел рядом, заняв примерно такую же позу, как и я."

    me "Раз уж ситуация позволяла, я решила спросить."

    iam "Эрик, почему ты связался с Коллектором?"

    iam "Всё говорит о том, что ты неплохой парень."

    iam "С твоими пособностями, ты бы построил отличную карьеру в Протекторате."

    show resonance_costume_mask_idle as character

    resonance "Как это у тебя понятия \"отличная карьера\" и \"неплохой парень\" связаны?"

    iam "Только не надо мне затирать, что Протекторат прогнил и быть в подчинении у Коллектора, который держит город в страхе, несёт в себе благие намерения."

    resonance "Про благие намерения не скажу, методы Коллектора такие какие они есть."

    resonance "Но ты верно сказала..."

    resonance "Протекторат - прогнил!"

    iam "А ничего что герои Протектората сражаются с Губителями, рискуя своими жизнями?"

    resonance "Ты хоть приблизительно представляешь себе что такое Губитель?"

    resonance "Всем становится наплевать: кто ты и чем ты занимался."

    resonance "Ударные группы формируются из всех подряд: геров, злодеев, бродяг..."

    resonance "Это не вопрос карьеры или статуса."

    resonance "Это вопрос выживания!"

    iam "Хочешь сказать, что ты сражался с Губителем?"

    me "Резонанс покачал головой."

    resonance "Я нет, а вот Вектор..."

    iam "Вектор? Он же тогда был Стражем."

    resonance "Нет."

    resonance "В Стражи он попал позже и ему намекнули молчать о своём участии."

    resonance "Он спас много гражданских и нсколько героев, которые пытались бежать от Левиафана."

    resonance "В том числе и Ронина."

    iam "Что?"

    iam "Об этом говорил Коллектор?"

    resonance "Да, Вектор - не подарок."

    resonance "Он хотел лучшего положения в Протекторате."

    resonance "И давил на Ронина, зная его секрет."

    resonance "До тех пор, пока Ронин не решил его подставить."

    iam "Это всё, разумеется, тебе известно с его слов?"

    resonance "Не только."

    resonance "Если вести тесное сотрудничество с другими кейпами и использовать связи, подтвердить правдивость таких событий не так уж и сложно."

    iam "То есть, кроме слухов, никаких доказательств нет?"

    resonance "Хочешь проверить?"

    resonance "Упомяни что-то из сказанного при Ронине."

    resonance "Посмотришь на его реакцию."

    me "Очень сложно было представить у Ронина хоть какую-то реакцию кроме: стандартный тон или командный тон."

    iam "Допустим, Протекторат не идеален."

    iam "Допустим, среди героев есть мудаки."

    iam "Но я решила, что смогу лично от себя сделать всё, чтобы мир стал хоть немного лучше."

    iam "Почему же ты не попробовал также?"

    iam "Зачем тебе Коллектор?"

    resonance "Ты правда хочешь узнать?"

    iam "Да, я хочу."

    me "Он подвинулся ближе ко мне."

    resonance "Хорошо."

    play music resonance_back_music loop volume 0.6
    hide character

    me "Затем Резонанс одёрнул рукав своего пиджака."

    show act_second_resonance_story_hand as background

    me "Вдоль правой руки я увидела несколько глубоких шрамов от порезов."

    iam "Откуда они у тебя?"

    resonance "Я был младше тебя на несколько лет."

    resonance "В моей семье - это означает, что я уже стал взрослым."

    resonance "А это значит..."

    resonance "Отец решил серьёзно заняться моим воспитанием."

    resonance "Ведь наша фамилия достаточно широко известна в узких кругах."

    me "Резонанс показал пальцем на конкретный шрам."

    resonance "Этот я получил, когда я взял вилку в правую руку, а нож в левую."

    resonance "А этот - когда поставил бокал с вином на стол, не сделав первый глоток."

    me "Он продолжал показывать."

    show act_second_resonance_story_piano_home as background

    resonance "А этот - когда сфальшивил свою партию на фортепиано."

    resonance "Этот был самый болезненный."

    resonance "Я не хотел играть на клавишах, но был обязан."

    resonance "Более того, отец мечтал о публичном выступлении своего старшего сына."

    resonance "Был ли я готов?"

    resonance "Мне казалось, что да."

    resonance "Ведь я часами только и делал, что повторял такт за тактом доставшуюся мне партию."

    show act_second_resonance_story_piano_calm as background

    resonance "Начался концерт."

    resonance "Первое время я чувствовал себя прекрасно."

    resonance "Мои пальцы работали словно на автопилоте."

    resonance "Я слишком поверил в себя и ближе ко второй части ускорил темп."

    show act_second_resonance_story_piano_scared as background

    resonance "Это была роковая ошибка."

    resonance "В середине композиции, правая рука начала болеть."

    resonance "Я сдерживался из последних сил, но этого было недостаточно."

    resonance "Рука практически анемела, а в музыке уже слышалась очевидная фальшь."

    show act_second_resonance_story_piano_fist as background

    resonance "Я перестал думать. Просто от ярости, злобы и обиды изо всех сил ударил едва ощущаемой рукой по инструменту."

    resonance "На этом для меня концерты закончились."

    resonance "А дома ждала расправа."

    show act_second_resonance_story_father_high as background

    iam "Твой отец?"

    iam "Он сделал что-то ещё более ужасное?"

    resonance "Мои крики были слышны по всему дому."

    resonance "Я не думаю, что он и вправду хотел меня убить, но его жестокость не знала предела."

    resonance "Сложно вспомнить все подробности того дня."

    resonance "Несколько раз я терял сознание."

    resonance "Но один момент я не забуду никогда."

    show act_second_resonance_story_boy_scared as background

    resonance "Он загнал меня в угол."

    resonance "А затем вернулся со старым топором."

    resonance "Я никогда не ощущал себя в более беспомощном положении."

    resonance "Неизвестно, готов ли он был осуществить задуманное или же хотел смертельно напугать меня."

    resonance "Но в этот момент реальность передо мной померкла."

    resonance "Я видел всякое, то что сложно описать словами."

    iam "Тогда случился твой триггер?"

    me "Резонанс кивнул."

    resonance "Я мгновенно понял как сопротивляться."

    resonance "Отец был обезоружен звуком, который я усиливал и искажал в его голове."

    show act_second_resonance_story_street as background

    resonance "Это дало мне время, чтобы освободиться и убраться из дома куда подальше."

    resonance "Но как только я открыл дверь."

    resonance "Прямо на пороге нашего дома лежал сосед - мистер Бревис."

    resonance "Он только что пришёл в себя, а затем воздух вокруг него окрасился в фиолетовый цвет, и сильным поток помог ему подняться."

    iam "Фиолетовый воздух? Неужели это Буран?"

    show buran_idle as character

    me "Буран - член Протектората."

    me "Он был популярен в нашем городе, однако, в один момент, он исчез из города."

    resonance "Как только он увидел меня, соседского мальчика с ранами, порезами и следами от верёвок - он пришёл в настоящий ужас."

    resonance "Он обнял меня и сказал..."

    show buran_scared as character

    buran "О Господи, скажи что ты ничего не видел?"

    resonance "Я...я не понимаю..."

    buran "Пацан, послушай, это тайна моей личности."

    buran "Ты не должен никому рассказывать никому, ты понял?"

    resonance "Да сэр, я понял."

    buran "Ещё раз, никому!"

    buran "Повтори ещё раз: \"Я никому не скажу!\""

    resonance "Я никому не скажу!"

    buran "Проклятье. Этого не достаточно."
    
    buran "Поклянись!"

    hide character

    show act_second_bridge as background

    show resonance_costume_mask_idle as character

    resonance "Я ничего ему не ответил."

    resonance "Мистер Бревис часто прогуливался у нашего дома."

    resonance "Без всяких сомнений - он слышал мои крики, когда отец избивал меня снова и снова."

    resonance "Ему ни только не было дела тогда."

    resonance "Даже когда он увидел меня в таком состоянии, когда у него была сила и возможность остановить мой кошмар..."

    resonance "Всё чего он хотел, чтобы я сохранил тайну его личности, как Кейпа Протектората."

    play music basement_music loop volume 0.6

    hide character

    me "Мы некоторое время молчали."

    me "Кажется, Резонанс хотел дать мне прочувствовать его ситуацию."

    iam "Я помню Бурана, но что с ним случилось потом?"

    show resonance_costume_mask_idle as character

    resonance "Ненависть к Протекторату оказалось достаточно сильной, чтобы я даже задумался применить свои способности, как член этой организации."

    resonance "Тем не менее, Буран был ненавистен мне в гораздо большей степени, чем мой отец-психопат."

    resonance "Встретившись с Коллектором, я получил от него помощь."

    resonance "Компромат на Бурана."

    resonance "Всем героям стало известно, что этот подонок хранит у себя записи с незаконной порнографией."

    resonance "Если верять слухам - разбирательство было жёсткое, однако в сеть, каким-то чудом, ничего не утекло."

    iam "И после этого ты остался должен Коллектору?"

    me "Резонанс замотал головой."

    resonance "Отнюдь нет."

    resonance "Он ничего не требовал от меня."

    resonance "Это была моя инициатива присоединиться."

    resonance "Я хотел справедливости, и он дал её мне."

    iam "Это ужасно."

    resonance "Ну что? Хочешь ещё быть доблестным кейпом Протектората?"

    iam "Да, Эрик, я хочу."

    iam "То, что произошло с тобой - чудовищно."

    iam "Буран, если всё было так, просто конченое животное."

    iam "Но это ничего не меняет."

    iam "Я тоже хочу справедливости, но достигать её путём, для которого не требуется разрушить чью-то жизнь."

    hide character

    me "Резонанс встал и слегка привёл в порядок свой костюм."

    show resonance_costume_mask_idle as character

    resonance "Время вышло."

    resonance "Уведоми героев, что тебе \"удалось сбежать\"."

    resonance "Но послушай..."

    resonance "Оставь попытки поиска мальчика."

    iam "Что? Почему?"

    resonance "Это слишком опасно."

    iam "Ты меня недооцениваешь."

    resonance "Дело не в том, что это опасно для тебя"

    resonance "Может случится что-то ужасное, если ты или кто-либо другой вмешается."

    me "Не могла поверить своим ушам."

    iam "Что тебе известно, Эрик?"

    iam "Скажи мне всё, прошу тебя!" 

    resonance "Я не знаю где мальчик."

    resonance "Это правда."

    resonance "Но я не могу сказать то, что мне известно."

    resonance "Слишком многое стоит на карте."

    resonance "Только, если ситуация зайдёт слишком далеко."

    resonance "Это гораздо ценней наших с тобой жизней."

    iam "Я не понимаю."

    resonance "Просто забудь про это."

    resonance "Прошу тебя."

    me "Его тело и пространство вокруг слегка исказились."

    resonance "До встречи, Айрин!"

    hide character

    play sound whiz volume 0.6 channel "backsounds_channel"

    me "Резонанс исчез в то же мгновение."

    me "Я была настолько шокирована, что даже не успела попытаться его остановить."

    me "О какой опасности он говорит?"

    me "Что же случилось с Сэмми?"

    me "В любом случае, не стоит терять время."

    me "Я должна продолжить расследование."

    me "Теперь, настало время нанести визит родителям Сэмми."

    if game_state.fahrenheit_is_ready:

        jump act_second_sammy_home_with_alice

    if not game_state.fahrenheit_is_ready:

        jump act_second_sammy_home_alone

    return

label act_second_legion_walking:

    hide character
    hide background

    show act_second_west_city_initial_street as background

    play music basement_music loop volume 0.6

    $ play_walking()

    me "Мы с Легион шли молча."

    me "Её рост легко позволял тащить Резонанса, который по прежнему оставался без сознания."

    me "Остальных её тел не было видно."

    me "Видимо она, как и обычно, отправила их патрулировать другие части города."

    me "Всё-таки у неё идеальная способность для этих целей."

    me "Я уже погрузилась в свои мысли."

    me "Верный ли выбор я сделала, учитывая мою ситуацию?"

    me "Теперь Коллектор вряд ли согласится следовать сделке."

    me "Мне придётся долго объяснять, что я делала в Западном Городе."

    me "И, конечно, Легион может захотеть присматривать за мной, что будет мешать вести расследование."

    me "С другой стороны..."

    me "Я помогла обезвредить суперзлодея."

    me "Разве это не то, чем и должен заниматься Страж?"

    show legion_idle as character

    legion "Ты хорошо потрудилась, Айрин."

    legion "Можешь собой гордится."

    iam "Спасибо, я и правда старалась."

    iam "Только мои усилия здесь были минимальными."

    legion "Смеёшься? Ты действовала очень даже профессионально для Стража."

    legion "Когда я начинала, была далеко не такой отчаянной, чтобы забраться в логово к опасной группировке суперзлодеев."

    hide character

    me "Вот как она это видит."

    me "Я ощущала тотальную неловкость."

    me "Возникло острое желание как-то увести разговор с этой темы."

    iam "Легион, можно вопрос?"

    show legion_idle as character

    legion "Конечно. Всё что угодно!"

    iam "Как именно ты получила свою способность?"

    show legion_surprised as character

    me "Я поняла насколько грубым был вопрос, только после того как озвучила его."

    me "Ведь я сама совершенно не готова была делиться таким личным с кем попало."

    iam "Прости, я не хотела..."

    show legion_idle as character

    legion "Да расслабься."

    legion "Дело не в том, что мне сложно рассказать."

    legion "Дело в том, что у меня нет прошлого."

    iam "В каком смысле?"

    legion "Скажи мне, Айрин, ты когда-то пыталась в доме найти конфеты, когда родители запрещали тебе есть сладкое?"

    iam "Конечно."

    legion "А делаешь ли ты так теперь?"

    iam "Эммм... нет."

    me "Я решительно не понимала, что она имеет ввиду."

    legion "Значит ли это, что та Айрин и сегодняшняя Айрин - два разных человека?"

    iam "Это просто я в прошлом."

    legion "А как бы ты себя чувствовала, если бы одновременно чувствовала себя собой сейчас, собой в прошлом и ваши желания сливались во что-то единое?"

    iam "Разве это возможно представить?"

    $ play_body_rustle()

    hide character

    me "В этот раз Легион остановилась и повернулась ко мне."

    show legion_idle as character

    legion "Я - это история пяти девочек."

    legion "Разные имена, судьбы, увлечения, желания."

    hide character

    show act_second_legion_story_five_girls as background

    legion "Девочки жили своими обычными жизни."

    legion "Кристи была сосредоточена на учёбе, Элин писала стихи под музыку."

    legion "Кэтрин мечтала стать дизайнером, а Стэйси - писать рассказы."

    legion "Сьюзи и вовсе готовилась к замужеству в столь раннем возрасте."

    legion "Но всё изменилось."

    legion "Каждую из нас вытащили из привычной зоны комфорта."

    show act_second_legion_story_lab as background

    legion "Чудовищный человек, лицо которого было скрыто за отвратительной маской и его сообщники."

    legion "Безумный учёный."

    legion "Каждый день он измерял наши показатели, что-то записывал в свой блокнот."

    legion "Нам приходилось длительное время находиться без одежды."

    legion "Хотя он явно не испытывал никакого интереса к нашим телам."

    legion "Мы для него были только объектами для исследований."

    iam "Это ужасно. Что же он хотел с вами сделать?"

    legion "Искал способ искусственно вызвать у нас триггер."

    legion "Понять, каким образом можно создавать кейпов."

    legion "После ежедневной проверки начинался настоящий ад."

    show act_second_legion_story_lab_experiments as background

    legion "Нас били, кололи какие-то препараты, подносили раскалённые лезвия близко к телу."

    legion "Несколько раз появлялась возможность сбежать, но это оказывалось лишь уловкой."

    legion "Всё нужно было, чтобы дать надежду на освобождение, а затем забрать её и жестоко наказать нас за неудачную попытку."

    legion "Так проходили многие дни."

    legion "Личность и собственное Я перестали иметь какое-либо значение."

    legion "Каждая из нас стала смесью страха, боли, унижения и отчаяния."

    show act_second_legion_story_lab as background

    legion "И в какой-то момент произошло то, чего ждал наш мучитель."

    legion "Триггер, который сделал нас едиными."

    legion "Больше не было смысла в том, чтобы говорить Мы, потому что не было никаких \"Мы\"."

    show legion_idle as character

    legion "В этот момент появилась Я."

    legion "Слаженные действия всех пяти моих тел позволили воспользоваться удачным моментам и сбежать из этого проклятого места."

    legion "Позже, я назвала себя Легион."

    legion "Я помню историю каждой девушки, которая дала жизнь моей личности."

    legion "Но это их прошлое, но не моё."

    legion "Они расстворились во мне, но при этом не являются мной."

    legion "Хочу просто верить, что стать героем Протектората и принести пользу человечеству это то, что сделает меня окончательно целой."

    show act_second_west_city_initial_street as background

    me "Я не могла отвести взгляд."

    me "Легион улыбнулась, а затем жестом показала, что нам следует идти дальше."

    hide character

    $ play_walking()

    me "Осознать, кто находится передо мной, что чувствует Легион каждую секунду своего существования, было непосильной задачей."

    show legion_idle as character

    legion "Видишь, я только сильнее тебя пригрузила."

    iam "Нет-нет, это удивительно."

    iam "Я стараюсь понять."

    legion "Повторюсь - не парься!"

    legion "Лучше расскажи, как ты напоролась на Резонанса."

    legion "Пыталась что-то разузнать?"

    hide character

    me "Эх, всё-равно вернулись к тому, с чего начинали."

    iam "Я смогла получить информацию о группировке Коллектора."

    iam "Теперь я знаю где находится тайное место их встречи."

    me "Легион подозрительно посмотрела на меня."

    show legion_idle as character

    legion "Ты про \"Falcon Bright\"?"

    iam "Вы знали?"

    legion "Ещё бы. Это известный факт в Протекторате."

    me "Этого я точно не ожидала."

    iam "Если это известно, то почему Коллектора и его банду до сих пор не накрыли?"

    iam "Это просто бар, он даже толком и не защищён."

    show legion_surprised as character

    legion "А зачем?"

    legion "Что будет дальше?"

    iam "Я не понимаю."

    legion "Вот накроем мы их, поймаем не всех."

    legion "Оставшиеся сунутся на нашу территорию и появятся в других районах города."

    iam "Но сейчас же они не появляются в других районах?"

    iam "Значит не могут?"

    me "Я заметила выражение неловкости на её лице."

    me "Кажется я задала вопрос, который, по её мнению, должен быть очевидным, но при этом ответ не должен быть произнесён вслух."

    show legion_idle as character

    legion "Если они сделают это без повода, тогда мы будем давать отпор."

    legion "Безусловно, если Протекторат объединит силы, то будет сильнее в прямом боестолкновении."

    legion "Но представь, что начнётся."

    legion "Война за территории."

    legion "Будут гибнуть гражданские, пострадают кейпы с обоих сторон."

    legion "В городе начнётся хаос."

    legion "Протекторат перестанет быть синонимом порядка."

    iam "Вы хотите сказать, что есть какой-то негласный договор, между героями и злодеями?"

    legion "Это не просто негласный договор."

    legion "Это рациональность."

    legion "В таком противостоянии глобально проиграют все."

    legion "Это единственный оптимальный вариант."

    hide character

    me "Не могла поверить своим ушам."

    me "Теперь понятно, почему нам дают дежурить в строго определённых местах."

    me "В голове не укладывается."

    iam "Если всё так и есть, тогда зачем пленить Резонанса?"

    show legion_angry as character

    legion "Он ведь напал на тебя, угрожал, держал в заложниках."

    legion "Резонанс первым перешёл черту, а значит, даже с точки зрения понятий Коллектора, мы поступили справедливо."

    hide character

    me "Я замерла."

    me "Легион вступила в бой только потому, что была свято уверена в угрожающей мне опасности."

    me "Суперзлодеи быстро выяснят, как всё было на самом деле."

    me "И, исходя из слов Легион, захотят освободить члена своей группировки."

    me "Надо немедленно всё рассказать, как бы ужасно я не выглядела."

    me "Ведь последствия могут быть куда серьёзней."

    me "Но только я хотела открыть рот, как поняла..."

    me "Моей карьере в Протекторате может настать конец."

    me "Более того, Легион может привлечь меня за пособничество суперзлоедям."

    me "Я уже потеряла возможность продолжить сделку с Коллектором, так ещё и, в лучшем случае, лишусь возможности получать деньги за свою работу."

    show legion_surprised as character

    legion "Эй, ты чего замерла?"

    legion "Всё впорядке?"

    me "Она остановилась и пристально смотрела на меня."

    me "Нужно было срочно решать, что говорить."

    menu:

        "Сказать Легион всю правду":

            iam "Легион, прошу меня выслушать."

            show legion_idle as character

            legion "Да чего ты так нервничаешь? Стресс после столкновения - это нормально."

            iam "Нет, Резонанс не держал меня в плену и не похищал."

            show legion_surprised as character

            legion "Что ты имеешь ввиду?"

            iam "Я сама пришла сюда..."

            iam "Чтобы заключить сделку с Коллектором."

            show legion_angry as character

            me "Выражение неудомения пропало с её лица."

            me "Теперь она разгневнно смотрела на меня."

            legion "Вот как? Ну продолжай."

            iam "Я встретила Резонанса в больнице, когда навещала свой подругу в коме."

            iam "Там я узнала от него, что группировка Коллектора крышует больницу, не позволяя переоборудовать её под другое здание."

            iam "Он предложил прийти в Западный Город и переговорить с его боссом."

            iam "Я понимаю, что мне не стоило этого делать."

            iam "Но тогда казалось, что у меня нет другого выбора."

            iam "Простите."

            show legion_angry as character

            legion "Айрин."

            legion "Ты сейчас осознаёшь, что именно ты мне говоришь?"

            iam "Да, абсолютно."

            me "Её правая рука сжалась в кулаке."

            $ play_fall_down()

            me "Она опустила тело Резонанса прямо на землю."

            show legion_surprised as character

            legion "Вот что..."

            legion "Я могу тебя понять, но ты даже не представляешь, какой опасности могла нас подвергнуть, если уже не подвергла."

            iam "Я не знала, что всё устроено именно так."

            legion "Незнание, не защитит нас от последствий."

            legion "Я не буду докладывать о твоём поступке, но только если ситуация не зайдёт слишком далеко."

            legion "В противном случае, прошу меня простить."

            iam "Я понимаю."

            legion "Постарайся в ближайшее время не совершать ничего, что привлекает внимание."

            legion "Иначе уже никто не сможет тебя защитить."

            hide character

            $ play_running()

            me "Она развернулась и быстрым шагом пошла дальше."

            me "Теперь ставки повысились."

            show act_second_near_city_street as background

            $ play_walking()

            me "Я шла около двадцати минут, прежде чем добраться до центральной площади."

            me "Теперь, когда я увидела последствия своих действий, моя решительность улетучилась."

            me "Нужно действовать максимально осторожно и не привлекать внимание, чтобы найти Сэмми и сохранить свой статус Стража."

            me "Надеюсь, у меня получится."

        "Скрыть правду от Легион":

            iam "Нет, ничего."

            iam "Просто задумалась о том, что они могут захотеть отомстить и могут придумать любой повод."

            show legion_idle as character

            legion "А, я бы не беспокоилась на твоём месте."

            legion "Если они сделают это в данной ситуации, у нас будет полное право действовать в полную силу."

            legion "Уверена, что они сами осознают последствия."

            hide character

            me "Остаётся только надеяться, что это действительно не станет поводом."

            me "Уж очень не хочется сталкиваться с последствиями моего решения."

            show act_second_near_city_street as background

            me "Дорога заняла по меньшей мере минут двадцать."

            me "Мы добрались до центральной площади."

            show legion_idle as character

            legion "Дальше я пойду сама."

            legion "Я, очевидно, понимаю, что тебя не должно было быть в Западном Городе."

            legion "Но, без тебя, я бы, возможно, не справилась."

            legion "Ты поступила как настоящий герой Протектората."

            legion "Если тебе нужна хоть какая-то помощь, только скажи!"

            me "Решение незамедлительно пришло в голову."

            iam "Это же ваша команда занимается расследованием пропавшего мальчика?"

            legion "Да, тебе что-то известно?"

            iam "Пока ещё нет. Вот только Ронин запретил нашей команде каким-либо образом принимать участие в его поиске."

            iam "Думаю вам известно, что я дежурила в школе в тот день, когда он пропал."

            iam "Для меня очень важно его найти, это личное."

            me "Она достаточно долго обдумывала ответ."

            show legion_surprised as character

            legion "Вообще, недопустимо оспаривать или вмешиваться в решения других руководителей Стражей."

            legion "Я не могу дать тебе официальное добро."

            show legion_idle as character

            legion "Но я могу пообещать, что в любом случае буду готова тебя прекрыть."

            legion "Надеюсь такая услуга устроит?"

            iam "Вполне. Спасибо большое."

            legion "Пожалуйста, Айрин."

            legion "И будь осторожна."

            hide character

            $ play_running()

            me "Она развернулась и быстрым шагом пошла дальше."

            me "Было сложно выкинуть из головы, что я могу стать причиной серьёзного противостояния злодеев и героев Протектората."

            me "Но хотя бы в расследовании у меня появился ценный союзник."

            me "Я и мечтать не могла о такой поддержке, после того, как Ронин отказал мне."

    me "А сейчас, нужно успеть заскочить домой к родителям Сэмми."

    me "Возможно, именно там я найду первую подсказку к тому, что мне делать дальше."

    if game_state.fahrenheit_is_ready:

        jump act_second_sammy_home_with_alice

    if not game_state.fahrenheit_is_ready:

        jump act_second_sammy_home_alone

    return

label act_second_sammy_home_with_alice:

    hide character
    hide background

    show act_second_sammy_house_entrance as background

    play music west_city_music loop volume 0.6

    $ game_state.resonance_deal_agree = False

    $ play_walking()

    me "Мы с Алисой поднимались по ступенькам к дверям дома, где жили родители Сэмми."

    me "Мы понимали, что просто так войти в дом и начать расспрашивать о Сэмми не получится."

    me "Найти номер телефона родителей Сэмми не представляло особого труда."

    me "Другое дело, как именно заинтересовать их и сделать готовыми говорить с нами."

    me "Представиться сотрудниками полиции или тем более кейпами Протектората было плохим вариантом."

    me "Родители Сэмми легко могли бы проверить эту информацию, с помощью одного телефонного звонка."

    me "Это привело бы не только к концу нашего расследования, но и нашей карьеры."

    me "Поэтому, я решила представить нас как репортёров, которые хотят снять сюжет."

    me "Люди склонны в большей степени доверять репортёрам и журналистам, особенно в такой трагической ситуации."

    me "И это сработало."

    me "Мистер Коллинз без каких-либо дополнительных вопросов назвал свой адрес и время, в которое мы можем приехать."

    me "Я даже не ожидала, что выбить получить будет так просто."

    $ play_doorbell()

    me "Я нажала пальцем на звонок, после чего раздался продолжительный неприятный звук."

    nobody_sammy_father "Да? Кто там?"
    
    me "Спокойный и мягкий мужской голос раздался по ту сторону двери."

    iam "Меня зовут Энджел Стэф."

    iam "Со мной Сьюзан Доусон - моя коллега."

    iam "Мы договаривались с вами о встрече по телефону."

    $ play_door_open()

    me "Дверь распахнулась."

    show sammy_father_idle as character

    iam "Добрый день, мистер Коллинз, я полагаю?"

    sammy_father "Очень рад видеть вас."

    sammy_father "Можете называть меня Билл."

    sammy_father "Прошу, проходите!"

    hide character

    me "Голос мистера Коллинза звучал невозмутимо и даже слишком беззаботно, несмотря на обстоятельства."
    
    me "С некоторой неуверенностью, отец Сэмми отошёл в сторону, приглашая нас внутрь."

    show act_second_sammy_house_hall as background

    $ play_door_close()

    me "Переступив порог, я сразу ощутила смену атмосферы."
    
    me "Прохлада подъезда сменилась на домашний уют."
    
    me "Пахло выпечкой."

    me "Но в этом уюте чувствовалась какая-то искусственность."
    
    me "Будто каждый элемент интерьера был тщательно расставлен для создания определенного впечатления."

    me "Из кухни раздавались звуки, которые сложно было не узнать."

    me "Популярное и, на мой взгляд, посредственное шоу \"Мой Шедевр\"."

    me "Участники должны были приготовить блюда за ограниченное время из ограниченного количества продуктов."

    me "Это всё сопровождалось дешёвыми постановочными скандалами и неадекватным поведением участников."

    me "Иногда было весело посмеяться с абсурдности происходящего вместе с Виктором и Нэнси."

    me "Но я ни за что бы не согласилась смотреть это одной на полном серьёзе."

    me "Видимо во всём этом Коллинзы находят в этом для себя какое-то утешение и способ держать себя в руках."

    show sammy_father_idle as character

    sammy_father "Дорогая, у нас гости!"

    me "Однако, никто не ответил."

    $ play_walking()

    me "Мы прошли дальше."

    hide character

    show act_second_sammy_house_kitchen as background

    me "Передо мной открылась небольшая кухня."

    me "Мистер Коллинз жестом пригласил присесть за стол."

    me "Затем он направился к кофемашине."

    me "Пока он возился с ней, я обратила внимание на миссис Колинз."

    me "Всё это время она продолжала увлеченно следить за кулинарным шоу по телевизору."

    me "На экране участник с энтузиазмом взбивал шоколадный крем."
    
    me "Мне показалось, что миссис Коллинз едва заметно подражала его движениям."

    me "Раздался громкий звук кофемашины."

    me "Миссис Коллинз, не отрывая взгляда от телевизора, взяла в руки пульт и прибавила громкость."
    
    me "Это действие показалось мне каким-то слишком механическим."

    me "Через несколько минут Мистер Коллинз поставил перед нами наполненные чашки и присел за рядом."

    play sound sip volume 2.0 channel "backsounds_channel"

    me "Мы с Алисой мгновенно осушили чашки."

    show fahrenheit_shorts_gloves_idle as character

    fahrenheit "Прекрасный кофе."

    fahrenheit "Спасибо."

    hide character

    show sammy_father_idle as character

    sammy_father "Должен признать, вы выглядите довольно молодо для того, чтобы работать на телевидении."

    sammy_father "Вы уже ранее снимали сюжеты о таких случаях, как наш?"

    iam "Вы не первый, кто удивляется моему возрасту, но вы сами сможете убедиться в моём профессионализме."

    iam "Особенно когда нанчутся съёмки."

    show sammy_father_sad as character

    sammy_father "Да конечно, надеюсь я никак не задел вас своим вопросом?"
    
    sammy_father "Мы просто первый раз имеем дело с репортёрами."

    iam "Ничего страшного, это нормально."

    me "На самом деле это показалось мне странным."

    me "Он не известна ли какая-то новая информация об их сыне, доводилось ли репортёрам общаться с кем-то ранее."

    me "Не уверена, но думаю - это первое, чтобы я спросила в подобной ситуации."

    show fahrenheit_shorts_gloves_idle as character

    fahrenheit "Как вы уже могли догадаться, мы здесь, чтобы поговорить о пропаже Сэмми."

    hide character

    show sammy_father_sad as character

    sammy_father "Да, конечно. Мы с женой очень обеспокоены."
    
    sammy_father "Мы хотим, чтобы о случае узнали как можно больше людей."
    
    iam "Соболезную вам, я даже боюсь представить каково вам приходится сейчас."

    sammy_father "Спасибо за ваше сочувствие. Каждый день без Сэмми - это испытание для нас."

    iam "Я понимаю. Можете рассказать, когда вы впервые обнаружили пропажу Сэмми?"

    sammy_father "Конечно, только я бы попросил вас записывать всё что я скажу."

    sammy_father "Не хочу, чтобы что-то было упущено в последствии."

    hide character

    me "Чёрт, вот где я прокололась."

    me "Наверняка опытный репортёр, записывал бы каждую деталь."

    me "К счастью, у меня были с собой блокнот и ручка, которые я мгновенно извлекла из своей сумки."

    show sammy_father_sad as character

    sammy_father "Это произошло в прошлую пятницу."
    
    sammy_father "Сэмми ушёл в школу, и мы даже не подозревали, что что-то может случиться."
    
    sammy_father "Он просто не вернулся домой после занятий."

    sammy_father "Он всегда возвращался домой вовремя."

    sammy_father "Ни минуты лишней не задерживался в школе."

    iam "Кажется, я знаю почему."

    iam "Я уже успела поговорить с учителем и некоторыми его сверстниками."

    iam "Мне сказали, что он подвергался травле со стороны старшеклассников."

    show sammy_father_angry as character

    sammy_father "Что?"

    sammy_father "Но это... это не может быть правдой."
    
    sammy_father "Сэмми никогда не говорил нам о травле."

    show sammy_father_sad as character

    sammy_father "Возможно, он не хотел нас беспокоить."

    iam "Это понятно. Родители часто узнают последними. Старшеклассники могут быть очень жестокими."

    iam "Может быть вы заметили что-то необычное в его личных вещах?"
    
    sammy_father "Сейчас важно, чтобы его комната и всё что находится в ней оставалось не тронутым."

    sammy_father "Мы бы предпочли дождаться профессионалов, которые снимут всё на камеру, чтобы люди знали, что мы ничего не скрываем."

    hide character

    me "Я попыталась скрыть своё удивление."
    
    me "Почему так много внимания уделяется тому, чтобы всё фиксировалось на камеру?"
    
    me "Почему не начать сразу активно искать любую информацию, которая могла бы помочь."

    show sammy_mother_idle as character

    sammy_mother "Я хочу чтобы все знали."

    sammy_mother "Как бы странно не вёл себя наш сын, я принимаю его любым."

    sammy_mother "Я...я..."

    hide character

    play sound crying_female volume 1.0 channel "backsounds_channel"

    me "Внезапно она ударилась в слёзы."

    me "Мистер Коллинз осторожно обнял её."

    me "Даже в этот момент она не отводила взгляда от телевизора."

    me "С родителями явно было что-то не так."

    me "Словно они пытались скрыть что-то очень важное."

    me "Мне необходимо попасть в комнату Сэмми."

    me "Только вот они ни за что меня не пустят, даже если я попрошу."

    me "Нужен план."

    play sound long_electricity loop volume 0.2 channel "backsounds_channel"

    me "Я постаралась сконцентрироваться на электроприборах в доме."

    if game_state.resonance_deal_agree:

        stop sound channel "backsounds_channel"

        me "Проклятье."

        me "Я могла ощущать общее напряжение, но никакой информации о форме."

        me "Так я ничего не добьюсь."

        me "Что ж, придётся искать комнату самостоятельно."

    if not game_state.resonance_deal_agree:

        me "Был ещё один телевизор на первом этаже и тоже включён."

        me "В чём прикол оставлять его так, когда в комнате никого нет?"

        me "Ещё один  телевизор - на втором этаже и выключен."

        me "Похоже, что это та комната, что мне нужна."

        stop sound channel "backsounds_channel"

    me "Я написала на блокноте: \"Отвлеки их!\"."

    me "Алиса едва заметно кивнула мне, а затем опустила голову на скрещённые руки."

    me "Выглядело так, будто в её голове родился какой-то план."

    me "Словно она тщательно обдумывает каждый шаг."

    me "В какой-то момент, она резко подорвалась со стула."

    show fahrenheit_shorts_gloves_idle as character

    fahrenheit "Я бы хотела обсудить завтрашнюю съёмку."

    fahrenheit "Репортаж появится на центральном канале, но сейчас мне нужно уточнить все детали."

    me "Глаза мистера Коллинза расширились от восторга."

    me "Его жена первый раз оторвалась от телевизора и встала рядом с мужем."

    show sammy_father_idle as character

    sammy_father "Это потрясающе!"

    show sammy_father_idle as character

    sammy_mother "Задавайте любые вопросы, мы готовы уделить вам хоть весь день."

    hide character

    me "Что?"

    me "Реакция родителей ужаснула меня."

    me "Нужно попасть в комнату и выяснить всё как можно быстрее."

    iam "Вы не возражаете, если я воспользуюсь уборной, пока с вами беседует моя коллега?"

    show sammy_father_idle as character

    sammy_father "Да, конечно!"

    hide character

    me "Он даже не уточнил, куда именно идти."

    me "Они с женой вновь повернулись к Алисе и начали что-то воодушевлённо рассказывать."

    show act_second_sammy_house_hall as background

    me "В этот момент я уже была за пределами кухни."

    me "Моё внимание привлекла лестница, ведущая на второй этаж."

    me "Даже отсюда я легко могла заметить дверь, к внешняя сторона которой была усеяна наклейками, которые шли в упаковках от жвачек."

    me "Кажется, мне нужна эта комната."

    $ play_walking()

    me "Я осторожно поднялась наверх и аккуратно вошла внутрь комнаты Сэмми."

    $ play_door_open()

    play music sammy_parents_music loop volume 0.6

    show act_second_sammy_house_room as background

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

    me "На столе всё было также организовано, как и в других частях комнаты."

    me "Ручки к ручкам, карандаши к карандашам, листки бумаги сложенные в стопки."

    me "Последние особенно привлекли моё внимание."

    play sound hugging volume 0.8 channel "backsounds_channel"

    me "Я взяла в руки стопку."

    me "На каждом листке было по одному рисунку."

    me "Хорошим художником Сэмми было назвать сложно."

    play sound paper_wrap volume 5.0 channel "backsounds_channel"

    me "Это были бы обычные детские рисунки, если бы не одно НО."

    me "\"Дорога из школы домой\" - очень схематично, но всё же, Сэмми указал очень точный путь."

    me "В последнее время, мы с командой много работали с картами и я могла без труда узнавать улицы по очертаниям."

    me "Чёрт возьми, тут даже были наброски дорожных знаков."

    me "Также здесь Сэмми нарисовал себя, с сумкой в руках, внутри которой обозначены книги и тетради, а также очень странный разноцветный круглый предмет."

    play sound paper_wrap volume 5.0 channel "backsounds_channel"

    me "Следующий рисунок."

    me "\"Школа\" - я вспоминала план, который описывал мистер Террел."

    me "Рисунок вновь идеально соответствовал ему, вплоть до расположения уборных."

    me "Сэмми нарисовал себя на заднем дворе школы, а в его сумке всё также книги, тетради и опять разноцветный круг."

    play sound paper_wrap volume 5.0 channel "backsounds_channel"

    me "\"Дом\" - идеальная схема комнат."

    me "Я без труда нашла место где стою сейчас."

    me "Тут была отображена практически каждая вещь, даже самые незначительные, почти также, как они расположены сейчас."

    me "Справа шкаф, в центре - письменный стол, слева кровать..."

    me "И тут, я увидела, что под кроватью нарисован ящик или сундук, внутри которого уже закомый мне разноцветный круглый предмет."

    # ЗВУК ТЯГАНИЯ

    me "Я залезла под кровать и, игнорируя создаваемый мною шум, вытащила оттуда сундук."

    $ play_door_open()

    me "Открыть его не составляло проблем, но, очевидно, Сэмми вряд ли хотел, чтобы он попал в чужие руки."

    me "Внутри не было ничего, кроме цветного колейдоскопа."

    me "Очевидно, это был тот самый круглый предмет, который я видела на рисунках."

    me "Я посмотрела в него, покрутила несколько раз."

    me "Ничего не обычного, вот только..."

    me "Он явно представлял что-то крайне важное, для маленького Сэмми."

    me "Я не была уверена, что могу забрать его с собой."
    
    me "Если я не справлюсь, то забрав его, смогу навредить дальнейшему расследованию."

    me "Пока эти размышления крутились в моей голове, я продолжила осматривать рисунки."

    play music creepy_music loop volume 0.6

    me "И тут я нашла то, что действительно меня напугало."

    me "Я без труда опознала на нескольких рисунках комнату Сэмми."

    me "Он изображал себя сидящим рядом с кроватью, обхватившим колени руками."

    me "На дверях был изображён непропорционально огромный железный замок."

    me "На рисунках также были родители Сэмми, которым он старался дорисовать даже самые мелкие отличительные черты."

    me "На всех рисунках, без исключения, мистер и миссис Колинз были прикованы к экрану телевизора."

    me "Ни одного изображения, где они бы были рядом с Сэмми."

    play sound sigh_female volume 1.0 channel "backsounds_channel"

    me "Жесть."

    me "Боже мой..."

    me "Они что запирали его в комнате?"

    play sound paper_wrap volume 5.0 channel "backsounds_channel"

    me "Наконец-то я обнаружила единственный рисунок, который говорит хоть а какой-то заботе к мальчику."

    me "Пожилой человек, который кладёт руку ему на плечо и протягивает тот самый калейдоскоп."

    me "Дедушка?"

    me "Я продолжила листать рисунки дальше."

    me "Он очевидно жил в этом доме и проводил немало времени с подростком."

    me "А потом..."

    play sound paper_wrap volume 5.0 channel "backsounds_channel"

    me "Я нашла рисунок его могилы."

    me "Боже..."

    me "Теперь понятно, почему эта вещь так для него важна."

    me "И судя по всему, он всегда носил её с собой."

    me "Но в этот раз, калейдоскоп остался в его тайнике."

    me "Не знаю, было ли это правильно, но я не могла удержаться от того, чтобы изучить всё это позже."

    me "Калейдоскоп, несколько рисунков и записи Сэмми, оказались у меня в сумке."

    show act_second_sammy_house_hall as background

    $ play_walking()

    stop music

    me "Я осторожно открыла дверь, спустилась вниз и проследовала на кухню."

    me "Я слышала, что родители до сих пор, с огромным вовлечением беседуют с Алисой."

    play music west_city_music loop volume 0.6

    show act_second_sammy_house_kitchen as background

    show sammy_father_idle as character

    sammy_father "А эта мне досталась всего за 4 доллара, настоящее сокровище."

    sammy_mother "Прекрасная съёмка и актёрская игра."

    sammy_father "Если вы не сильно спешите, могли бы устроить совместный просмотр."

    fahrenheit "Ой, даже не знаю, у нас так много работы, ведь нужно подготовиться к завтрашним съёмкам."

    show sammy_mother_smile as character

    sammy_mother "Боже мой, уже завтра?"

    show sammy_father_idle as character

    sammy_father "Нам нужно хорошенько прибраться!"

    sammy_mother "Конечно милый, только узнаю кто победил и начнём."

    hide character

    me "Коллинзы прильнули к телевизору."

    me "Словно в какой-то момент забыли о том, что я стою рядом."

    me "Выпуск шоу подходил к концу."

    tv_host "Мы закончили подсчёт баллов."

    tv_host "Пять долгих недель вы сражались друг с другом за главный приз \"Моего Шедевра\"."

    me "Так, это уже выходит за рамки."

    me "В лучшем случае - им плевать на сына."

    me "В худшем - они как-то замешаны в его пропаже."

    me "Меня переполняла ярость."

    tv_host "Через несколько секунд, станет известен победитель..."

    me "Но что я могу сделать?"

    me "Я даже не имею возможности сообщить обо всём этом кому-то из героев."

    me "Остаётся просто уйти и надеяться найти дополнительные улики."

    stop music

    me "Или же...?"

    tv_host "И победителем становится..."

    menu:

        "Просто уйти":

            play music west_city_music loop volume 0.6

            tv_host "Джерри Фостер - наш чемпион."

            me "Из телевизора раздались оглушительные аплодисменты."

            me "Миссис Коллинз взвизгнула и подскочила на стуле."

            sammy_father "А мы ведь были уверены, что он вылетет."

            me "Я приложила все усилия, чтобы успокоиться."

            me "Как бы сильно я не злилась, я не могу позволить себе действовать радикально."

            me "Несколько глубоких вдохов и я смогла прийти в норму."

            iam "Я вспомнила, что нужно быть в офисе до часа дня."

            iam "Извините, ещё очень много работы."

            fahrenheit "Да, конечно, прошу нас простить."

            show sammy_father_idle as character

            sammy_father "Перестаньте. Всё в порядке!"

            show sammy_mother_idle as character

            sammy_mother "Будем ждать вас завтра."

            me "Миссис Коллинз всё ещё не отрывалась от шоу, хотя сейчас там показывали только титры."

            iam "Тогда, до свидания и хорошего дня!"

            sammy_father "До встречи, безумно рад был поговорить с вами!"

            show sammy_mother_smile as character

            sammy_mother "До завтра!"

            hide character

            show act_second_sammy_house_street as background

            play music basement_music loop volume 0.6

            $ play_walking()

            me "Мы покинули этот дом, жители которого вызывали у меня тошноту."

            fahrenheit "Ты тоже в ахуе?"

            iam "В полнейшем."

            iam "Но их поведение - это ещё не всё."

            fahrenheit "Что ты имеешь ввиду?"

            me "Я извлекла из сумки рисунки, где была изображена запертая дверь в комнату Сэмми."

            fahrenheit "О господи, что за жесть?"

            iam "Я об этом же."

            iam "Они больные на голову."

            iam "И, вероятно, могут быть замешаны."

            fahrenheit "Мне очень жаль Сэмми."

            fahrenheit "Мы должны что-то сделать."

            iam "К сожалению, время ограничено."

            iam "Нужно успеть попасть к учителю, раньше чем там окажется команда Легион."

            iam "Иначе, маловероятно что он поделится с нами какой-то существенной информацией."

            fahrenheit "Давай я попробую поговорить с соседями, чтобы узнать больше, а ты поспеши к мистеру Террелу."

            me "Эта идея показалась мне максимально разумной в данной ситуации."

            iam "Спасибо, Алиса."

            iam "Правда спасибо."

            me "Она улыбнулась мне своей фирменной улыбкой, от которой на душе стало теплее."

            me "Она убежала обратно в дом."

            me "Я же двинулась вперёд, подальше от этого места."

        "Использовать Силу и надавить на родителей":

            play music disturbing_music loop volume 0.6

            me "Свет в доме погас."

            me "Телевизоры, лампочки и прочая техника прекратили свою работу."

            sammy_mother "Проклятье! На таком моменте!"

            me "Как только родители повернулись в мою сторону, они оба вскрикнули и отстранились назад."

            me "Я стояла перед ними, а вокруг меня вращались электрические сферы."

            sammy_father "Я видел тебя по телевизору."

            sammy_father "Ты из Стражей."

            sammy_father "Решила нас обмануть."

            iam "Теперь поговорим на чистоту."

            iam "Почему на двери вашего сына висел замок."

            sammy_father "Я добъюсь того, чтобы тебя вышвырнули..."

            me "Электрический импульс полетел в коллекцию видеокасет."

            me "Они разлетелись по всей комнате."

            me "Некоторые из них сломались пополам от сильного удара о стену."

            me "Это мгновенно прервало уверенную речь мистера Коллинза."

            me "Теперь в их глазах я наблюдала неподдельный человеческий страх."

            iam "Вы никому ничего не сообщите."

            iam "Если я узнаю, что вы пытались рассказать об этом случае, найти вас не составит большого труда."

            me "Я достала из сумки рисунок, где на двери в комнату Сэмми стоял огромный замок."

            iam "А теперь отвечайте на вопросы или я не буду сдерживаться."

            sammy_father "С-с-сэмми, убегал из дома."

            iam "Да ладно, и вы решили об этом не говорить?"

            sammy_mother "Он был очень расстроен смертью своего дедушки."

            sammy_mother "И убегал в тайне от нас на кладбище, чтобы навестить его могилу."

            sammy_father "Что мы ещё могли сделать?"

            iam "Даже не знаю..."

            iam "Может быть навестить могилу вместе с ним?"

            iam "Может быть поговорить с ребёнком о том, что такое смерть?"

            iam "А не сидеть на диване и смотреть мусорные телепередачи?"

            sammy_mother "Мой отец - дедушка Сэмми, считал нас ужасными родителями."

            sammy_mother "Он не давал нам возможность воспитывать сына и проводить с ним время."

            iam "А может он просто был прав?"

            me "Я видела как Коллинзы дрожат в то время как я возвышалась над ними, окружённая электричеством."

            me "Кажется, вряд ли они скажут что-либо ещё."

            me "Говорят ли они правду?"

            me "Или же просто стараются не выдать свою причастность к пропаже мальчика?"

            me "К сожалению, сейчас я не смогу узнать больше."

            me "Я вернула электричество в каждый электроприбор в доме."

            me "А затем покинула дом Коллинзов."
            
            iam "Прости, они ужасны!"

            fahrenheit "Я понимаю..."

            fahrenheit "Это и правда кошмар."

            fahrenheit "Но я приняла решение встать на твою сторону и заниматься расследованием..."

            fahrenheit "И рассчитывала, что мы будем соблюдать осторожность."

            fahrenheit "Я уже рада, что мы на эмоциях не натворили лишнего, но просто хочу, чтобы ты помнила, чем мы рискуем."

            iam "Прости, обещаю, что этого не повториться."

            iam "Когда мы найдём Сэмми, этот инцендент - последнее о чём вспомнят, если вообще узнают."

            $ play_walking()

            me "Она лишь слегка кивнула, развернулась и устремилась прочь от дома Коллинзов."

    me "Да уж, не удивлена, что Сэмми стал жертвой травли, когда его родителям абсолютно наплевать на его судьбу."

    me "Всё что мне удалось найти - это:"

    me "Сэмми склонен сортировать любые вещи."

    me "Рисует, учитывая мельчашие детали."

    me "Родители уделяли мало внимания сыну из-за одержимости телепередачами и фильмами."

    me "В жизни Сэмми был важный пожилой человек, скорее всего дедушка."

    me "Он подарил мальчику калейдоскоп, который был для подростка чем-то очень важным."

    me "Он брал его с собой в школу, но в этот раз он оставил его в сундуке под кроватью."

    me "Не так много, как бы хотелось, но уже неплохие зацепки."

    me "Возможно, мистер Террел поможет понять мне куда двигаться дальше."

    me "Необходимо продолжать расследование."

    jump act_second_teacher

    return

label act_second_sammy_home_alone:

    hide character
    hide background

    show act_second_sammy_house_entrance as background

    play music west_city_music loop volume 0.6
    # play music sammy_parents_music loop volume 0.6

    $ game_state.fahrenheit_is_ready = False
    $ game_state.resonance_deal_agree = False

    $ play_walking()

    me "Я поднималась по ступенькам к дверям дома, где жили родители Сэмми."

    me "Я понимала, что просто так войти в дом и начать расспрашивать о Сэмми не получится."

    me "Найти номер телефона родителей Сэмми не представляло особого труда."

    me "Другое дело, как именно заинтересовать их и сделать готовыми говорить со мной."

    me "Представиться сотрудником полиции или тем более кейпом Протектората было плохим вариантом."

    me "Родители Сэмми легко могли бы проверить эту информацию, с помощью одного телефонного звонка."

    me "Это привело бы не только к концу моего расследования, но и моей карьеры."

    me "Поэтому, я решила представиться как репортёр, который хотят снять сюжет."

    me "Люди склонны в большей степени доверять репортёрам и журналистам, особенно в такой трагической ситуации."

    me "И это сработало."

    me "Мистер Коллинз без каких-либо дополнительных вопросов назвал свой адрес и время, в которое я могу приехать."

    me "Я даже не ожидала, что получить согласие будет так просто."

    $ play_doorbell()

    me "Я нажала пальцем на звонок, после чего раздался продолжительный неприятный звук."

    nobody_sammy_father "Да? Кто там?"
    
    me "Спокойный и мягкий мужской голос раздался по ту сторону двери."

    iam "Меня зовут Энджел Стэф."

    iam "Мы договаривались с вами о встрече по телефону."

    $ play_door_open()

    me "Дверь распахнулась."

    show sammy_father_idle as character

    iam "Добрый день, мистер Коллинз, я полагаю?"

    sammy_father "Очень рад видеть вас."

    sammy_father "Можете называть меня Билл."

    sammy_father "Прошу, проходите!"

    hide character

    me "Голос мистера Коллинза звучал невозмутимо и даже слишком беззаботно, несмотря на обстоятельства."

    me "С некоторой неуверенностью, отец Сэмми отошёл в сторону, приглашая меня внутрь."

    show act_second_sammy_house_hall as background

    $ play_door_close()

    me "Переступив порог, я сразу ощутила смену атмосферы."
    
    me "Прохлада подъезда сменилась на домашний уют."
    
    me "Пахло выпечкой."

    me "Но в этом уюте чувствовалась какая-то искусственность."
    
    me "Будто каждый элемент интерьера был тщательно расставлен для создания определенного впечатления."

    me "Из кухни раздавались звуки, которые сложно было не узнать."

    me "Популярное и, на мой взгляд, посредственное шоу \"Мой Шедевр\"."

    me "Участники должны были приготовить блюда за ограниченное время из ограниченного количества продуктов."

    me "Это всё сопровождалось дешёвыми постановочными скандалами и неадекватным поведением участников."

    me "Иногда было весело посмеяться с абсурдности происходящего вместе с Виктором и Нэнси."

    me "Но я ни за что бы не согласилась смотреть это одной на полном серьёзе."

    me "Видимо во всём этом Коллинзы находят в этом для себя какое-то утешение и способ держать себя в руках."

    show sammy_father_idle as character

    sammy_father "Дорогая, у нас гости!"

    me "Однако, никто не ответил."

    $ play_walking()

    me "Мы прошли дальше."

    hide character

    show act_second_sammy_house_kitchen as background

    me "Передо мной открылась небольшая кухня."

    me "Мистер Коллинз жестом пригласил присесть за стол."

    me "Затем он направился к кофемашине."

    me "Пока он возился с ней, я обратила внимание на миссис Колинз."

    me "Всё это время она продолжала увлеченно следить за кулинарным шоу по телевизору."

    me "На экране участник с энтузиазмом взбивал шоколадный крем."
    
    me "Мне показалось, что миссис Коллинз едва заметно подражала его движениям."

    play sound coffee_machine volume 1.0 channel "backsounds_channel"

    me "Раздался громкий звук кофемашины."

    me "Миссис Коллинз, не отрывая взгляда от телевизора, взяла в руки пульт и прибавила громкость."
    
    me "Это действие показалось мне каким-то слишком механическим."

    me "Через несколько минут Мистер Коллинз поставил передо мной наполненную чашку и присел за рядом."

    play sound sip volume 4.0 channel "backsounds_channel"

    me "Я мгновенно осушила чашку."

    iam "Весьма неплохо, спасибо большое."

    show sammy_father_idle as character

    sammy_father "Должен признать, вы выглядите довольно молодо для того, чтобы работать на телевидении."

    sammy_father "Вы уже ранее снимали сюжеты о таких случаях, как наш?"

    iam "Вы не первый, кто удивляется моему возрасту, но вы сами сможете убедиться в моём профессионализме."

    iam "Особенно когда нанчутся съёмки."

    show sammy_father_sad as character

    sammy_father "Да конечно, надеюсь я никак не задел вас своим вопросом?"
    
    sammy_father "Мы просто первый раз имеем дело с репортёрами."

    iam "Ничего страшного, это нормально."

    hide character

    me "На самом деле это показалось мне странным."

    me "Он не известна ли какая-то новая информация об их сыне, доводилось ли репортёрам общаться с кем-то ранее."

    me "Не уверена, но думаю - это первое, чтобы я спросила в подобной ситуации."

    iam "Как вы уже могли догадаться, я здесь, чтобы поговорить о пропаже вашего сына."

    show sammy_father_sad as character

    sammy_father "Да, конечно. Мы с женой очень обеспокоены."
    
    sammy_father "Мы хотим, чтобы о случае узнали как можно больше людей."
    
    iam "Соболезную вам, я даже боюсь представить каково вам приходится сейчас."

    sammy_father "Спасибо за ваше сочувствие. Каждый день без Сэмми - это испытание для нас."

    iam "Я понимаю. Можете рассказать, когда вы впервые обнаружили пропажу Сэмми?"

    sammy_father "Конечно, только я бы попросил вас записывать всё что я скажу."

    sammy_father "Не хочу, чтобы что-то было упущено в последствии."

    hide character

    me "Чёрт, вот где я прокололась."

    me "Наверняка опытный репортёр, записывал бы каждую деталь."

    me "К счастью, у меня были с собой блокнот и ручка, которые я мгновенно извлекла из своей сумки."

    show sammy_father_sad as character

    sammy_father "Это произошло в прошлую пятницу."
    
    sammy_father "Сэмми ушёл в школу, и мы даже не подозревали, что что-то может случиться."
    
    sammy_father "Он просто не вернулся домой после занятий."

    sammy_father "Он всегда возвращался домой вовремя."

    sammy_father "Ни минуты лишней не задерживался в школе."

    iam "Кажется, я знаю почему."

    iam "Я уже успела поговорить с учителем и некоторыми его сверстниками."

    iam "Мне сказали, что он подвергался травле со стороны старшеклассников."

    show sammy_father_angry as character

    sammy_father "Что?"

    sammy_father "Но это... это не может быть правдой."
    
    sammy_father "Сэмми никогда не говорил нам о травле."

    show sammy_father_sad as character

    sammy_father "Возможно, он не хотел нас беспокоить."

    iam "Это понятно. Родители часто узнают последними. Старшеклассники могут быть очень жестокими."

    iam "Может быть вы заметили что-то необычное в его личных вещах?"
    
    sammy_father "Сейчас важно, чтобы его комната и всё что находится в ней оставалось не тронутым."

    sammy_father "Мы бы предпочли дождаться профессионалов, которые снимут всё на камеру, чтобы люди знали, что мы ничего не скрываем."

    hide character

    me "Я попыталась скрыть своё удивление."
    
    me "Почему так много внимания уделяется тому, чтобы всё фиксировалось на камеру?"
    
    me "Почему не начать сразу активно искать любую информацию, которая могла бы помочь."

    show sammy_mother_idle as character

    sammy_mother "Я хочу чтобы все знали."

    sammy_mother "Как бы странно не вёл себя наш сын, я принимаю его любым."

    sammy_mother "Я...я..."

    hide character

    play sound crying_female volume 1.0 channel "backsounds_channel"

    me "Внезапно она ударилась в слёзы."

    me "Мистер Коллинз осторожно обнял её."

    me "Даже в этот момент она не отводила взгляда от телевизора."

    me "С родителями явно было что-то не так."

    me "Словно они пытались скрыть что-то очень важное."

    me "Мне необходимо попасть в комнату Сэмми."

    me "Только вот они ни за что меня не пустят, даже если я попрошу."

    me "Нужен план."

    play sound long_electricity loop volume 0.2 channel "backsounds_channel"

    me "Я постаралась сконцентрироваться на электроприборах в доме."

    if game_state.resonance_deal_agree:

        stop sound channel "backsounds_channel"

        me "Проклятье."

        me "Я могла ощущать общее напряжение, но никакой информации о форме."

        me "Так я ничего не добьюсь."

        me "Что ж, придётся искать комнату самостоятельно."

    if not game_state.resonance_deal_agree:

        me "Был ещё один телевизор на первом этаже и тоже включён."

        me "В чём прикол оставлять его так, когда в комнате никого нет?"

        me "Ещё один  телевизор - на втором этаже и выключен."

        me "Похоже, что это та комната, что мне нужна."

        stop sound channel "backsounds_channel"

    me "Нужно придумать убедительную причину, чтобы иметь достаточно времени на обыск."

    if game_state.resonance_deal_agree:

        me "А учитывая, что я до сих пор не понимаю где комната, придётся искать комнату Сэмми не полагаясь на мою Силу."

    me "Жаль что Алисы нет рядом."

    me "С её эмпатией, она могла приковать внимание практически любого человека."

    me "Но да ладно, нужно действовать."

    iam "Я хотела бы продолжить, только мне нужно вспользоваться уборной, если вы не против."

    show sammy_father_idle as character

    sammy_father "Ой, да, конечно!"

    sammy_father "На первом этаже, прямо направо и прямо до красной двери."

    hide character

    me "Я кивнула и вышла из кухни, стараясь, чтобы моих шагов не было слышно."

    show act_second_sammy_house_hall as background

    me "Я старалась двигаться максимально тихо, чтобы не создавать лишний шум."

    if game_state.resonance_deal_agree:

        $ play_walking()

        me "Я прошла в одну из комнат на первом этаже."

        me "Там работал ещё один телевизор, который показывал то же шоу, что и на кухне."

        me "Зачем вообще было оставлять его включённым?"

        me "Осторожно закрыв дверь я поспешила в следующую комнату."

        me "Чёрт, кладовка."

        me "Судя по всему, мне нужно на второй этаж."

    stop music

    me "Я старалась контроллировать каждую мышцу своего тела, чтобы максимально бесшумно подняться по лестнице."

    me "Что-то странное было в родителях мальчика или же мне только так показалось."

    me "Я увидела дверь, усеянную наклейками, которые шли в упаковках от жвачек."

    me "Наклейки с героями из разных известных фильмов."

    me "Кажется, мне нужна эта комната."

    $ play_door_open()

    me "Я осторожно осторожно открыла дверь и аккуратно вошла внутрь комнаты Сэмми."

    play music sammy_parents_music loop volume 0.6

    show act_second_sammy_house_room as background

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

    me "На столе всё было также организовано, как и в других частях комнаты."

    me "Ручки к ручкам, карандаши к карандашам, листки бумаги сложенные в стопки."

    me "Последние особенно привлекли моё внимание."

    play sound hugging volume 0.8 channel "backsounds_channel"

    me "Я взяла в руки стопку."

    me "На каждом листке было по одному рисунку."

    me "Хорошим художником Сэмми было назвать сложно."

    play sound paper_wrap volume 5.0 channel "backsounds_channel"

    me "Это были бы обычные детские рисунки, если бы не одно НО."

    me "\"Дорога из школы домой\" - очень схематично, но всё же, Сэмми указал очень точный путь."

    me "В последнее время, мы с командой много работали с картами и я могла без труда узнавать улицы по очертаниям."

    me "Чёрт возьми, тут даже были наброски дорожных знаков."

    me "Также здесь Сэмми нарисовал себя, с сумкой в руках, внутри которой обозначены книги и тетради, а также очень странный разноцветный круглый предмет."

    play sound paper_wrap volume 5.0 channel "backsounds_channel"

    me "Следующий рисунок."

    me "\"Школа\" - я вспоминала план, который описывал мистер Террел."

    me "Рисунок вновь идеально соответствовал ему, вплоть до расположения уборных."

    me "Сэмми нарисовал себя на заднем дворе школы, а в его сумке всё также книги, тетради и опять разноцветный круг."

    play sound paper_wrap volume 5.0 channel "backsounds_channel"

    me "\"Дом\" - идеальная схема комнат."

    me "Я без труда нашла место где стою сейчас."

    me "Тут была отображена практически каждая вещь, даже самые незначительные, почти также, как они расположены сейчас."

    me "Справа шкаф, в центре - письменный стол, слева кровать..."

    me "И тут, я увидела, что под кроватью нарисован ящик или сундук, внутри которого уже закомый мне разноцветный круглый предмет."

    play sound dragging volume 1.0 channel "backsounds_channel"

    me "Я залезла под кровать и, игнорируя создаваемый мною шум, вытащила оттуда сундук."

    $ play_door_open()

    me "Открыть его не составляло проблем, но, очевидно, Сэмми вряд ли хотел, чтобы он попал в чужие руки."

    me "Внутри не было ничего, кроме цветного колейдоскопа."

    me "Очевидно, это был тот самый круглый предмет, который я видела на рисунках."

    me "Я посмотрела в него, покрутила несколько раз."

    me "Ничего не обычного, вот только..."

    me "Он явно представлял что-то крайне важное, для маленького Сэмми."

    me "Я не была уверена, что могу забрать его с собой."
    
    me "Если я не справлюсь, то забрав его, смогу навредить дальнейшему расследованию."

    me "Пока эти размышления крутились в моей голове, я продолжила осматривать рисунки."

    play music creepy_music loop volume 0.6

    me "И тут я нашла то, что действительно меня напугало."

    me "Я без труда опознала на нескольких рисунках комнату Сэмми."

    me "Он изображал себя сидящим рядом с кроватью, обхватившим колени руками."

    me "На дверях был изображён непропорционально огромный железный замок."

    me "На рисунках также были родители Сэмми, которым он старался дорисовать даже самые мелкие отличительные черты."

    me "На всех рисунках, без исключения, мистер и миссис Колинз были прикованы к экрану телевизора."

    me "Ни одного изображения, где они бы были рядом с Сэмми."

    play sound sigh_female volume 1.0 channel "backsounds_channel"

    me "Жесть."

    me "Боже мой..."

    me "Они что запирали его в комнате?"

    sammy_father "Мисс Стэф, с вами всё в порядке?"

    me "Времени больше не осталось."

    me "В панике я запихнула все найденные мной рисунки, а также калейдоскоп, в сумку."

    me "К сожалению, время для более тщательного осмотра всей комнаты закончилось."

    $ play_door_close()

    me "Затем, я осторожно открыла дверь, в ожидании, что могу столкнуться с кем-то из родителей Сэмми."

    show act_second_sammy_house_hall as background

    stop music

    me "Повезло."

    me "Никого в поле зрения."

    $ play_walking()

    me "Я, облегчённо вздохнув, стала спускаться вниз по лестнице."

    play sound sudden_appearance volume 1.0 channel "backsounds_channel"

    show sammy_father_angry as character

    sammy_father "Что вы здесь делали?"

    sammy_father "Я же уточнил, что уборная на первом этаже."

    iam "Да, я знаю."

    iam "Я просто..."

    iam "Обратила внимание на то, как украшена дверь."

    iam "Эти наклейки с героями из разных фильмов."

    iam "Стало интересно, кто в вашем доме такой фанат кинематографа."

    play music west_city_music loop volume 0.6

    show sammy_father_idle as character

    sammy_father "Оу, я разве не говорил, что у нас есть огромная коллекция видеокасет?"

    iam "А? Что?"

    sammy_father "Давайте вернёмся на кухню, я вам всё покажу."

    hide character

    me "Не могу поверить, что это сработало."

    me "Минуту назад, я думала что мне конец."

    me "Но стоило мне упомянуть про коллекцию, как мистер Коллинз забыл про всё на свете."

    show sammy_father_idle as character

    sammy_father "А здесь у меня хиты 1996 года, много боевиков, но есть и мелодрамы..."

    sammy_father "Каждую пересматривал минимум по пять раз."

    sammy_father "А вот здесь лучшее, что выходило с Уиллом Смитом..."

    hide character

    me "Я почти не слушала."

    me "Всё ждала, когда он закончит, но уже сомневалась что этот момент когда-нибудь наступит."

    me "Миссис Колинз всё ещё была прикована к мерзкому шоу по телевизору."

    play music west_city_music loop volume 0.6

    show act_second_sammy_house_kitchen as background

    show sammy_father_idle as character

    sammy_father "А эта мне досталась всего за 4 доллара, настоящее сокровище."

    sammy_mother "Прекрасная съёмка и актёрская игра."

    sammy_father "Если вы не сильно спешите, могли бы устроить совместный просмотр."

    iam "Ой, даже не знаю, у нас так много работы, ведь нужно подготовиться к завтрашним съёмкам."

    show sammy_mother_idle as character

    sammy_mother "Боже мой, уже завтра?"

    show sammy_father_idle as character

    sammy_father "Нам нужно хорошенько прибраться!"

    show sammy_mother_smile as character

    sammy_mother "Конечно милый, только узнаю кто победил и начнём."

    hide character

    me "Коллинзы прильнули к телевизору."

    me "Словно в какой-то момент забыли о том, что я стою рядом."

    me "Выпуск шоу подходил к концу."

    tv_host "Мы закончили подсчёт баллов."

    tv_host "Пять долгих недель вы сражались друг с другом за главный приз \"Моего Шедевра\"."

    me "Так, это уже выходит за рамки."

    me "В лучшем случае - им плевать на сына."

    me "В худшем - они как-то замешаны в его пропаже."

    me "Меня переполняла ярость."

    tv_host "Через несколько секунд, станет известен победитель..."

    me "Но что я могу сделать?"

    me "Я даже не имею возможности сообщить обо всём этом кому-то из героев."

    me "Остаётся просто уйти и надеяться найти дополнительные улики."

    stop music

    me "Или же...?"

    tv_host "И победителем становится..."

    menu:

        "Просто уйти":

            play music west_city_music loop volume 0.6

            tv_host "Джерри Фостер - наш чемпион."

            play sound applause volume 2.0 channel "backsounds_channel"

            me "Из телевизора раздались оглушительные аплодисменты."

            me "Миссис Коллинз взвизгнула и подскочила на стуле."

            sammy_father "А мы ведь были уверены, что он вылетет."

            sammy_mother "А я говорила тебе, у него все шансы взять приз."

            me "Я приложила все усилия, чтобы успокоиться."

            me "Как бы сильно я не злилась, я не могу позволить себе действовать радикально."

            me "Несколько глубоких вдохов и я смогла прийти в норму."

            iam "Я вспомнила, что нужно быть в офисе до часа дня."

            iam "Извините, у меня ещё очень много работы."

            show sammy_father_idle as character

            sammy_father "Перестаньте. Всё в порядке!"

            show sammy_mother_idle as character

            sammy_mother "Будем ждать вас завтра."

            hide character

            me "Миссис Коллинз всё ещё не отрывалась от шоу, хотя сейчас там показывали только титры."

            iam "Тогда, до свидания и хорошего дня!"

            show sammy_father_idle as character

            sammy_father "До встречи, безумно рад был поговорить с вами!"

            show sammy_mother_smile as character

            sammy_mother "До завтра!"

            hide character

            show act_second_sammy_house_street as background

            play music basement_music loop volume 0.6

        "Использовать Силу и надавить на родителей":

            play music disturbing_music loop volume 0.6

            show act_second_sammy_house_kitchen_no_electricity as background

            me "Свет в доме погас."

            me "Телевизоры, лампочки и прочая техника прекратили свою работу."

            show sammy_mother_idle as character

            sammy_mother "Проклятье! На таком моменте!"

            hide character

            me "Как только родители повернулись в мою сторону, они оба вскрикнули и отстранились назад."

            play sound long_electricity volume 0.2 channel "backsounds_channel"

            me "Я стояла перед ними, а вокруг меня вращались электрические сферы."

            show sammy_father_angry as character

            sammy_father "Я видел тебя по телевизору."

            sammy_father "Ты из Стражей."

            sammy_father "Решила нас обмануть."

            iam "Теперь поговорим на чистоту."

            iam "Почему на двери вашего сына висел замок."

            sammy_father "Я добъюсь того, чтобы тебя вышвырнули..."

            hide character

            play sound short_electricity volume 3.0 channel "backsounds_channel"

            me "Электрический импульс полетел в коллекцию видеокасет."

            play sound fall_down volume 1.0 channel "backsounds_channel"

            me "Они разлетелись по всей комнате."

            me "Некоторые из них сломались пополам от сильного удара о стену."

            me "Это мгновенно прервало уверенную речь мистера Коллинза."

            me "Теперь в их глазах я наблюдала неподдельный человеческий страх."

            iam "Вы никому ничего не сообщите."

            iam "Если я узнаю, что вы пытались рассказать об этом случае, найти вас не составит большого труда."

            me "Я достала из сумки рисунок, где на двери в комнату Сэмми стоял огромный замок."

            iam "А теперь отвечайте на вопросы или я не буду сдерживаться."

            show sammy_father_sad as character

            sammy_father "С-с-сэмми, убегал из дома."

            iam "Да ладно, и вы решили об этом не говорить?"

            show sammy_mother_idle as character

            sammy_mother "Он был очень расстроен смертью своего дедушки."

            sammy_mother "И убегал в тайне от нас на кладбище, чтобы навестить его могилу."

            sammy_father "Что мы ещё могли сделать?"

            hide character

            iam "Даже не знаю..."

            iam "Может быть навестить могилу вместе с ним?"

            iam "Может быть поговорить с ребёнком о том, что такое смерть?"

            iam "А не сидеть на диване и смотреть мусорные телепередачи?"
            
            show sammy_mother_idle as character

            sammy_mother "Мой отец - дедушка Сэмми, считал нас ужасными родителями."

            sammy_mother "Он не давал нам возможность воспитывать сына и проводить с ним время."

            hide character

            iam "А может он просто был прав?"

            me "Я видела как Коллинзы дрожат в то время как я возвышалась над ними, окружённая электричеством."

            me "Кажется, вряд ли они скажут что-либо ещё."

            me "Говорят ли они правду?"

            me "Или же просто стараются не выдать свою причастность к пропаже мальчика?"

            me "К сожалению, сейчас я не смогу узнать больше."

            show act_second_sammy_house_kitchen as background

            me "Я вернула электричество в каждый электроприбор в доме."

            me "А затем покинула дом Коллинзов."

            play music west_city_music loop volume 0.6

            show act_second_sammy_house_street as background

            me "Как только я оказалась на улице, до меня дошло осознание того что я сделала."

            me "Будучи Стражем, использовала Силу против гражданских."

            me "Угражала им в случае, если они сообщат кому-либо."

            me "Я, очевидно, перешла черту."

            me "Сомневаюсь, что мои действия долгое время будут оставаться в тайне."

            me "Единственное, что я могу сделать сейчас, это приложить все усилия, чтобы завершить расследование."

    me "Нужно собраться с мыслями."

    me "Вот всё что мне удалось найти:"

    me "Сэмми склонен сортировать любые вещи."

    me "Рисует, учитывая мальчашие детали."

    me "Родители уделяли мало участия жизни сына из-за одержимости телепередачами и фильмами."

    me "Сэмми хранил под кроватью калейдоскоп, который был для него чрезвычайно важным."

    me "Не так много, как бы хотелось, но уже есть некоторые зацепки."

    me "Возможно, мистер Террел поможет понять мне куда двигаться дальше."

    me "Необходимо продолжать расследование."

    jump act_second_teacher

    return

label act_second_teacher:

    me "Кабинет мистера Террела был примерно таким, как я и ожидала."

    me "Слегка неряшливый, множество приборов для лабораторных работ, занимавшие полки в шкафу..."

    me "Много книг, как внутри шкафов, так и на столе."

    if game_state.monument_is_ready:

        teacher "О, уважаемые Стражи, очень рад вас видеть."

        teacher "Присаживайтесь!"

        me "Я села на свободный стул напротиве учителя."

        me "Не знаю насколько он был искренним, учитывая что в прошлый раз я оказалась в эпицентре нападения на детей на прошлой неделе."

        me "А тут ещё и пропал ученик."

        me "Девид занял место рядом со мной."

        me "Всё-таки, я рада, что у далось его убедить."

        me "В его присутствии я ощущала себя гораздо более уверенной в себе."

    if not game_state.monument_is_ready:

        teacher "О, Искра, если не ошибаюсь."

        iam "Да, всё верно."

        teacher "Очень рад вас видеть."

        teacher "Присаживайтесь!"

        me "Я села на свободный стул напротив учителя."

        me "Не знаю насколько он был искренним, учитывая что в прошлый раз я оказалась в эпицентре нападения на детей на прошлой неделе."

        me "А тут ещё и пропал ученик."

        me "В этот момент я подумала про Девида."

        me "Без его поддержки было невероятно трудно продумать, что делать дальше."

        me "Тем не менее, действовать было необходимо."

    teacher "Кажется, я понимаю по какому делу вы пришли."

    iam "Думаю да."

    iam "Сэмми пропал как раз после..."

    iam "Того случая, когда я..."

    teacher "Только не берите в голову..."

    teacher "В произошедшем нет вашей вины."

    teacher "Могу только представить, насколько сложной может быть работа..."

    teacher "Для людей со сверх..."

    teacher "В общем, вы поняли."

    me "Поняли только то, что он хотел меня подбодрить."

    me "В любом случае - мило."

    iam "Спасибо вам."

    iam "Я хотела спросить про тех двух хулиганах, которые издевались над Сэмми."

    iam "Я понимаю, что это ваши ученики, но я не могу исключать их потенциальную причастность."

    teacher "Прекрасно могу понять."

    teacher "Стэн и Грегор, мягко говоря, не самые прилежные ученики."

    teacher "И в конфликтах оказывались не один раз."

    teacher "Тем не менее..."

    teacher "Похищение одноклассника?"

    teacher "Подумайте сами, зачем?"

    iam "Это я и хочу выяснить."

    if game_state.monument_is_ready:

        monument "Если они додумались издеваться над тем кто слабее, игнорировали Стража Протектората, то почему это вдруг не способны на похищение?"

        teacher "Боже правый, вы серьёзно?"

    teacher "Оба мальчика из не самых благополучных семей."

    teacher "Родители всячески игнорировали наши просьбы прийти в школу."

    teacher "Даже, когда стоял вопрос об исключении."

    teacher "Но есть ли вина детей в этом?"

    iam "Думаю, вы знаете не хуже меня..."

    iam "Немало детей, детство которых было по-настоящему кошмарным, в итоге смогли достичь успехов без какого-либо насилия."

    iam "Как бы не было плохо человеку, даже если он подросток."

    iam "Возможность выбирать и нести ответственность за свои действия ещё никто не отменял."

    if game_state.monument_is_ready:

        me "Девид совершил жест, напоминающий аплодисменты."

        monument "Ну, тут собственно крыть нечем."

    teacher "Выбор?"

    me "Мистер Террел как-то странно изменился в лице."

    teacher "Скажу вам, как человек науки..."

    teacher "Есть ли у нас выбор или нет - это далеко не самый простой вопрос."

    teacher "Вы ведь, в тот день, во дворе школы, уверены, что сделали верный выбор?"

    iam "Абсолютно нет."

    iam "Не могу быть уверена, но будь у меня возможность вернуться в прошлое, я бы во многом поступила иначе."

    teacher "Лишь потому, что вы уже знаете, к чему привели последствия ваших действий."

    teacher "А знания эти появились у вас, исключительно, после принятых решений."

    teacher "Это и называется опыт."

    teacher "Если бы только существовал парачеловек с такой Силой или устройство, способное переносить нас в прошлое..."

    teacher "Тогда, может быть и шла речь об осознанном выборе."

    me "Я бы хотела возразить, но после сказанного, только одна мысль занимала всё моё сознание в этот момент..."

    me "ВИКТОР."

    if game_state.monument_is_ready:

        monument "Предлагаю вернуться к тебе, не ударяясь в философию."

        teacher "Да, конечно."

        teacher "Просто..."

    teacher "Ну, сейчас не об этом."

    teacher "У мальчиков есть алиби."

    teacher "Их увезли в больницу сразу после инцендента с суперзлодеем."

    iam "В Протекторате мне сообщили, что у одного из них травмы не были серьёзными и он достаточно быстро вернулся домой."

    teacher "Вот именно, Искра, домой."

    teacher "Грегор вернулся домой."

    teacher "Думаете, первое, что он захотел бы сделать - отправиться в погоню за младшеклассником?"

    iam "Я не хочу никого обвинять заранее."

    iam "Важно только то, что он проявлял к нему агрессию, а мотив до сих пор не ясен."

    me "Какое-то время мистер Террел молчал."

    me "Он изменился в лице."

    me "Смотрел на меня так, словно пытался просканировать."

    if game_state.monument_is_ready:

        teacher "Ребята, я бы хотел спросить напрямую."

    if not game_state.monument_is_ready:

        teacher "Искра, я бы хотел спросить напрямую."

    teacher "Протекторат назначил вас провести расследование?"

    teacher "Или же они не в курсе, а вами движут личные мотивы?"

    me "Проклятье."

    me "У меня и мысли не было, что именно он поднимет этот вопрос."

    me "Если скажу правду - он никогда не даст мне адрес учеников, которых, видимо, готов защищать до последнего."

    me "Если совру, то когда на месте окажется команда Легион - меня раскроют."

    me "Более того, если он уже относится с подозрением, мне придётся изрядно надавить, чтобы достигнуть желаемого."

    me "Здесь уже выкрутится не получится."

    me "Надо понять, что говорить, прямо сейчас."

    menu:

        "Сказать правду":

            iam "Я здесь по собственной инициативе."
            
            iam "Простите, но я действительно чувствую вину за произошедшее."

            if game_state.monument_is_ready:

                monument "Мой руководитель назначил меня на это расследование."

                monument "Вам ведь известно, кто такой Ронин?"

                me "Мистер Террел согласно кивнул."

                monument "Мне же дали возможность выбрать себе помощника."

                monument "Я выбрал Искру не только из-за личных мотивов, но и потому что мы прекрасно работаем в команде."

                me "Он посмотрел на меня."

                me "Я ощущала неловкость, не понимая, действительно ли он думает так или же просто спасает мою задницу от провала."

                monument "Думаю вам известно, что Ронин славится своей дисциплинированностью и уважением к правилам."

                monument "Поэтому, можете не сомневаться в нас."

                monument "Мы всего-лишь поговорим с Грегором."

                monument "Ни более того."

                me "Мистер Террел внимательно слушал каждое слово Девида."

                me "Казалось он взвешивает все за и против, пытаясь понять как действовать дальше."

                teacher "Ох, надеюсь вы не подведёте меня, ребята."

                me "Он взял листок бумаги и написал на нём что-то."

                me "Затем он протинул листок Девиду."

                teacher "Очень надеюсь, что это поможет."

                monument "Благодарю."

                monument "А сейчас, мы вынуждены уйти."

                monument "Спасибо ещё раз."

                me "Мы вышли из кабинета и проследовали по школьному коридору."

                iam "У тебя могут быть серьёзные проблемы, зачем ты это сделал?"

                monument "Он бы не дал нам адрес и не совсем не факт, что не сдал бы нас."

                monument "Поверь, это было лучшее решение."

                iam "Но мы собирались действовать, максимально осторожно."

                iam "Ронин точно узнает."

                iam "Да, может без каких-либо подробностей, но узнает."

                me "Девид положил руку мне на плечо и широко улыбнулся."

                monument "Да плевать мне."

                monument "Мы вписались, чтобы сделать что-то действительно хорошее."

                monument "Отступать поздно."

                me "Всё ещё сложно было откинуть мысль, что у Девида будут проблемы из-за меня."

                me "Но, всё-таки, сейчас мы стали на шаг впереди к тому, чтобы найти Сэмми."

                me "Осталось только попасть в дом по указанному адресу..."

            if not game_state.monument_is_ready:

                teacher "Как я уже сказал - это не ваша вина."

                teacher "И я искренне ценю вашу откровенность."

                teacher "Обещаю, что я никому не скажу, дабы не создавать вам проблемы."

                iam "Спасибо."

                iam "Но всё-таки, мне действительно важно найти..."

                teacher "Нет-нет-нет."

                teacher "Это мои ученики, это моя ответственность."

                teacher "Если будет официальный запрос от Стражей, которые ведут расследование - я с удовольствием предоставляю всё что нужно."

                teacher "Но не сейчас."

                if game_state.attack_teen:
                
                    teacher "И никто не посмеет причинить им вред."

                    teacher "Ни суперзлодей, ни член Протектората."

                    teacher "Надеюсь, я выразился достаточно ясно?"

                    me "Я поняла, что он намекает на мой проёб в прошлую пятницу."

                    me "А что я вообще могла сделать?"

                    me "Просто смотреть?"

                    me "Мистер Террел смотрел на меня, не скрывая злобы и отвращения."

                    teacher "Думаю, Искра, вам пора."

                teacher "Всего доброго."

                me "Он демонстративно уткнулся в какую-то книгу."

                me "Делать было нечего."

                me "Я вышла из кабинета и побрела по школьному коридору."

                me "Полный провал."

                me "И чем я только думала?"

                me "Ну да ладно."

                me "Может мистер Террел и прав."

                me "Зачем подросткам, даже отбитым, заниматься похищением, в городе где столько супергероев."

                me "Сэмми пропал после своего триггера."

                me "Если его действительно похитили, это с большой вероятностью был кейп."

                me "Плевать."

                me "Здесь не получилось, зато сэкономила время и успею в остальные места."

                me "Осталось решить, куда идти дальше."

                jump act_second_school_territory

        "Надавить":

            if not game_state.monument_is_ready:

                me "Я встала из-за стола и приготовилась к худшему."

                iam "Официально, мистер Террел."

                teacher "Что-то я крайне сильно в этом сомневаюсь."

                iam "Кажется я поняла в чём дело."

                teacher "Что вы имеете в виду?"

                iam "Вот это ваше \"Вы не виноваты, Искра, у вас такая сложная работа\"."

                iam "Вы ненавидите кейпов!"

                iam "Я помню наш разговор."

                iam "Дети не могут развиваться, когда так много Технарей вокруг."

                iam "Детям надо на кого-то ровняться."

                iam "Вы готовы простить любого подонка, который издевается над слабым, лишь бы не доверять кому-то со сверхспособностями."

                me "Я нависала над ним, пока он сидел, что создавало явный дискомфорт."

                me "И я чувствовала это."

                me "Чувствовала его желание уйти отсюда."

                teacher "А теперь я скажу..."

                iam "СИДЕТЬ НА МЕСТЕ!"

                me "В кабинете замигал свет."

                me "Он, в полнейшем недоумении, опустился обратно в своё кресло."

                me "Часть собранного электричества пульсировала вокруг моей левой руки."

                iam "Мы не полиция, мистер Террел."

                iam "Я Страж Протектората."

                iam "Защитник этого города."

                iam "Хотите от меня документов?"

                iam "А я хочу, чтобы Сэмми нашли живым."

                iam "Желаете пожаловаться на тяжкую жизнь учителя в мире супергероев?"

                iam "Звоните в горячую линию Протектората."

                iam "А мне - плевать!"

                me "Я перевела дыхание, стараясь выглядеть всё также максимально грозно."

                me "Я рассеяла электричество вокруг моей руки."

                me "В воздухе повис запах озона."

                me "Мистер Террел"

                iam "А теперь я жду адрес."

                iam "Сейчас же!"

                me "Я вышла в кордиор."

                me "В руках я держала адрес, написанный дрожащей рукой мистера Террела."

                me "Так и хотелось сказать самой себе, что у меня не было выбора."

                me "Только это будет означать, что мистер Террел прав и выбор - всего-лишь иллюзия."

                me "Чувствую, последствия того, что я сделала, не заставят себя долго ждать."

                me "Но, всё-таки, сейчас я стала на шаг впереди к тому, чтобы найти Сэмми."

                me "Осталось только попасть в дом по указанному адресу..."

            if game_state.monument_is_ready:

                me "Мы вышли в коридор."

                me "Адрес был у нас."

                monument "Мда..."

                monument "Добром это явно не кончится."

                iam "Что мне ещё было делать?"

                monument "Если бы тут была Алиса, то накатала бы целый список."

                monument "Я же просто мягко отмечу, что Ронин не заценит то, что ты угрожала школьному учителю, чтобы без доказательств преследовать его ученика."

                iam "Если хочешь слиться - сделай это сейчас."

                monument "Девид положил руку мне на плечо."

                monument "Даже и в мыслях не было!"

                monument "Просто сообщил то, что думаю."

                me "Кажется пронесло."

                me "Мне кажется, всё могло сложиться значительно хуже."

                me "Но, всё-таки, сейчас мы стали на шаг впереди к тому, чтобы найти Сэмми."

                me "Осталось только попасть в дом по указанному адресу..."

    jump act_second_teacher_gregor_house

    return

label act_second_teacher_gregor_house:

    me "Я прибыла по адресу, где жил Грэгор Штейнхолд."

    me "Совершенно очевидно, что подросток не отреагирует дружелюбно, учитывая наше последнее столкновение с ним."

    if game_state.attack_teen:

        me "Особенно, учитывая тот факт, что я применила против него силу."

    me "Я заняла место в кустах неподалёку и сосредоточилась на всей технике, находящейся в доме."

    me "Свет был включён в нескольких комнатах."

    me "Работал телевизор."

    me "В какой-то момент включился, а затем выключился спустя 10 минут пылесос."

    me "В доме явно кто-то есть и не происходит ничего не обычного."

    me "Кроме одной детали."

    me "В одной из комнат, я ощутила несколько сферических приборов разных размеров."

    me "Без малейшего понятия что это."

    me "Однако напряжение внутри достаточно мощное."

    me "Времени не так много, поэтому нужно действовать."

    me "Выманить его из дома."

    me "Я отключила все электроприборы, которые смогла."

    me "Абсолютно всё, кроме неизвестных мне объектов, ибо не знала, могут ли они сдетонировать, если я сделаю что-то не так."

    me "5 минут..."

    me "10..."

    me "Никакой реакции."

    me "Тогда я принялась включать и отключать технику с интервалом, примерно, в 10 секунд."

    me "Это уже явно что-то менее обычное, что должно заставить кого-то выйти из дома и проверить что происходит."

    me "Через некоторое время дверь открылась."

    me "Но..."

    me "Никого."

    me "Уже довольно приличное время никто не показывался."

    me "Я продолжала играть с электроприборами в надежде, что всё-таки что-то произойдёт."

    me "Так и случилось."

    me "Стоило лишь немного подождать, как я увидела фигуру уже знакомого мне подростка, который устремился к обратной стороне дома."

    me "Ну готовься, парень."

    me "Сегодня ты не будешь таким борзым как в прошлый раз."

    me "Я уже была готова..."

    me "Но, что-то явно было не так."

    me "Фигура крайне неестественно спускалась с лестницы."

    me "Ноги словно периодически проваливались в неё."

    me "А когда левая рука фигуры прошла сквозь фонарный столб..."

    me "Я всё поняла."

    me "Голограмма!"

    me "ЧЁРТ!"

    me "Раздался взрыв."

    me "Я не успела обернуться."

    me "Яркий свет ударил мне в глаза."

    me "Окружение стало постепенно проявляться."

    me "Вот только совсем не то, в которым я находилась ещё минуту назад."

    me "Да и сложно было назвать это местом."

    me "Какая-то безумная смесь разных природных ландшафтов."

    me "Я хотела осмотреть своё тело, убедиться что руки и ноги на месте."

    me "Вот только я не смогла их увидеть."

    me "Стало по-настоящему страшно."

    me "Я ощутила острую боль."

    me "Словно в меня что-то вонзилось."

    me "Я ринулась вперёд."

    me "Или мне только кажется, что я ринулась."

    me "Все ощущения казались сплошным обманом."

    me "Единственное чему я готова была доверять - это своей Силе."

    me "Я не чувствовала расстояния, но прекрасно ощущала электрическую активность тех самых сферических уйстройств."

    me "Около восьми штуки."

    me "Держу пари, именно они и отвечают за эти иллюзии."

    me "Я бы могла попытаться взорвать их все сразу, но даже не могу представить себе масштаб ущерба."

    me "Мгновенно вспомнила историю про Вектора, который в ходе задания, сделал так, что погибли четверо гражданских."

    me "Снова."

    me "Резкая боль в плече."

    me "Я не могу их обесточить из-за замкнутого корпуса."

    me "Разве что сконцентрироваться и попытаться снизить напряжение."

    me "Вот только..."

    me "Если я буду медлить, неизвестно, прикончат ли меня за это время."

    me "Нужно принимать решение и немедленно!"

    menu:

        "Взорвать устройства":

            me "Я снова начала чувствовать."

            me "Зазвенело в ушах."

            me "Меня куда-то отбросило."

            me "Теперь я могла видеть собственные руки."

            me "Иллюзорное окружение расстворялось на моих глазах, позволяя снова видеть реальность."

            me "Я попыталась сдвинуться с места."

            me "В этот момент заболели раны в плече и правом боку."

            me "Они кровоточили."

            me "Благо костюм значительно снизил урон, иначе я бы уже не смогла двигаться."

            me "Обернувшись, я увидела его."

            me "Грегор, лежал на земле."

            me "Глаза закрыты."

            me "Его правая рука была в ужасном состоянии."

            me "Рядом лежал окровавленный нож."

        "Попытаться снизить напряжение":

            me "Я полностью сконцентрировалась на электрическом потоке."

            me "При этом мне нужно было постоянно перемещаться, без ощущения движения."

            me "А вот боль я ощущала отлично."

            me "Ещё один удар под ребром."

            me "Еще один в ногу."

            me "Было сложно понять сколько крови я уже потеряла."

            me "Но наконец-то..."

            me "Мне удалось снизить напряжение."

            me "Иллюзии растворялись на моих глазах."

            me "Реагировать нужно было быстро."

            me "Обернувшись, я увидела Грегора, который замахивается на меня с ножом."

            me "Я увернулась."

            me "Кажется этого он не ожидал."

            me "Я мгновенно собрала электричество вокруг в мощный импульс и отбросила подростка."

            me "Кажется это было слишком сильно."

            me "Он ударился головой о дерево и мгновенно потерял сознание."

    me "Я бросилась к нему и проверила пульс."

    me "Живой."

    me "Но, после чувства облегчения, последовал гнев и ненависть."

    me "Он пытался меня убить."

    me "Да он ещё, оказывается, и кейп."

    me "Я бы хотела доставить его в больницу, но в этом случае мне конец."

    me "Делать было нечего."

    me "Я, собравшись с силами, подняла Грэгора и потащила его в сторону леса."

    jump act_second_teacher_gregor_forest

label act_second_teacher_gregor_forest:

    me "Грегор очнулся."

    me "Сразу же после пробуждения, он попытался броситься на меня."

    me "Разумеется, я была готова."

    me "Подросток был надёжно привязан к дереву."

    me "Я его как можно дальше от города."

    gregor "Ты совсем сумасшедшая?"

    gregor "Похищение гражданского?"

    iam "Гражданского, серьёзно?"

    iam "Будешь меня убеждать, что голограмы не твоих рук дела?"

    me "Грегор посмотрел на меня с улыбкой."

    me "Как и в тот раз..."

    me "Не кажется что он боится."

    gregor "Я ничего тебе говорить не буду."

    gregor "А ты, в итоге, ничего мне не сделаешь."

    iam "Хочешь проверить?"

    gregor "Ещё как!"

    me "Предположим, он непричастен ко всему этому."

    me "Однако, он был готов к тому, что кейп заявится к нему домой."

    me "И не побоялся вонзить в меня нож."

    me "Нет."

    me "Невиновный не будет вести себя так."

    me "Он явно что-то знает."

    me "Или же я надумываю."

    me "В любом случае, разговорить его будет не просто."

    me "Я и так уже натворила достаточно."

    me "Стоит ли сдерживаться сейчас и упустить важную информацию?"

    me "Или же показать, что для меня нет никаких пределов."

    me "Или же пойти на крайности?"

    gregor "Ну что ты там? Будешь держать меня тут весь день?"

    iam "Где Сэмми?"

    gregor "Думаю твоя шайка из Протектората будет просто в восторге, когда всё узнают."

    menu:

        "Попытаться уговорить":

            iam "Послушай, Грегор."

            iam "Нет ни единой причины, почему Сэмми должен страдать."

            iam "Поступи правильно."

            iam "Скажи мне всё, что ты знаешь."

            gregor "Боже мой..."

            gregor "Как же это жалко!"

            me "Он рассмеялся мне в лицо."

            me "С другой стороны, а чего ещё стоило ожидать?"

        "Угрожать":

            iam "Не хочешь сотрудничать?"

            iam "А что если я просто оставлю тебя здесь."

            iam "Интересно, как скоро тебя найдут?"

            gregor "Что за херню ты несёшь?"

            gregor "Найдут рано или поздно."

            gregor "А когда это произойдёт - тебе никто не поверит."

            gregor "Попрощаешься с карьерой героя и с нормальной жизнью тоже."

    menu:

        "Попытаться договориться":

            iam "Грегор."

            iam "Похищение - это уже не буллинг."

            iam "Доказательства будет найти не сложно."

            iam "Когда узнают, что ты ещё и кейп, тебя закроют надолго."

            iam "Но если расскажешь всё здесь и сейчас."

            iam "Я сделаю всё, чтобы о тебе никто не узнал."

            gregor "Закроют говоришь?"

            gregor "Возможно."

            gregor "Но тебя закроют ещё на дольше за превышение полномочий."        


        "Угрожать физической силой":

            me "Я подняла с земли камень."

            gregor "Что ты собралась делать?"

            me "Я подошла максимаьно близко и приложила камень к его лицу."

            gregor "Ты что, больная?"

            gregor "Убери это от меня!"

        "Ударить":

            me "Я подошла максимально близко и нанесла резкий удар в живот."

            me "Он слегка вскринул."

            gregor "Подняла руку на связанного подростка?"

            gregor "Для тебя всё закончится хуже, чем я думал."

        "Сильно ударить":

            me "Я сделала вид, что собираюсь уйти..."

            me "А затем, со всего размаху, ударила ногой по лицу."

            me "Настолкьо сильно, что его шея, кажется наклонилась, под неестественным углом."

            me "Он издал истошный крик."

            gregor "Никто тебе не поверит, когда увидят на мне кровь и синяки!"

            gregor "Так что, повторюсь..."

            gregor "ИДИ НАХУЙ!"

    menu:

        "Про родителей Сэмми" if game_state.sammy_house_visited:

            iam "Я понимаю, что тебе с родителями приходится несладко."

            iam "Не во всём есть твоя вина."

            iam "А что ты знаешь про родителей Сэмми?"

            gregor "Да в семье, очевидно, любимчик."

            gregor "То как он выглядит, одевается."

            gregor "Предки явно с ним носятся."

            iam "Вот и ошибка."

            iam "Родители Сэмми - конченые уёбки!"

            me "Он явно удивился моему ответу."

            iam "Родители помешены на телешоу и передачах."

            iam "Они ни разу не появлялись в школе, когда их просили прийти."

            iam "Они ничего не знают про его проблемы."

            iam "Внешний вид Сэмми - это исключительно его заслуга и дедушки, который любил его."

            iam "А знаешь, почему теперь нет близкого человека, который бы его любил?"

            me "Грегору не требовался ответ."

            me "Неужели у меня действительно получилось задеть его?"

            iam "За что вы напали на него на школьном дворе?"

            gregor "Он прятал от нас какую-то свою побрякушку."

            gregor "Не хотел показывать."

            gregor "Да мы бы посмотрели и вернули..."

            gregor "Наверное."

            iam "Калейдоскоп."

            iam "Подарок от покойного дедушки."

            iam "Единственное напоминание о нём."

            gregor "Чёрт возьми!"

            me "Внутри него, как будто, происходила серьёзная внутренняя борьба."

            gregor "Я не знаю где Колинз."

            gregor "Он нас невероятно бесил."

            gregor "Я же не знал, что у него дома творится."

            gregor "Но и мне жаль, что всё это произошло."

            iam "Ты скажешь мне всё что знаешь?"

            gregor "Нет."

            gregor "И уже не потому что не хочу."

            gregor "Не могу!"

            gregor "Прошу, забудь про эти поиски."

            gregor "Это слишком опасно."

            iam "Ты что-то знаешь про угрозу S-класса?"

            gregor "Есть влиятельные люди, которые контроллируют ситуацию."

            gregor "Они знают, что делают."

            gregor "Любое вмешательство приведёт к катастрофе."

            iam "Влиятельные люди?"

            iam "Ты говоришь о Коллекторе?"

            gregor "Больше я ничего не скажу."

            gregor "Я не могу!"

        "Рассказать про угрозу класса S":

            me "Я понимаю, что ты не главный виновник всего этого."

            me "Тебе кажется, что всё это мелочь."

            me "Кейп, который похитил Сэмми, представляет реальную опасность."

            me "Ты даже не представляешь себе масштаб и степень этой угрозы."

            me "Расскажи сейчас всё что знаешь и у нас будет шанс избежать реальной беды."

            me "Грегор рассмеялся."

            me "Не своим обычным, а неестественно безумным смехом."

            gregor "Что ты вообще знаешь про угрозу?"

            gregor "Ты ведь даже близко не представляешь, что происходит."

            iam "Что ты имеешь ввиду?"

            me "Кажется он хотел сказать что-то язвительное."

            me "Но внезапно его лицо стало серьёзным."

            me "Он плотно сомкнул губы."

            me "Его слегка начало трясти."

            iam "Повторяю, что ты имеешь ввиду?"

            me "Но он молчал."

            me "Я попробовала замахнуться на него."

            me "Но он никак не отреагировал."

        "Избивать":

            me "Я едва могла себя контроллировать."

            me "Вспомнила его отвратительную ухмылку..."

            me "Бесящую самоуверенность..."

            me "И, конечно же, тот факт, что он пытался меня убить..."

            me "Удары сыпались один за другим."

            me "Казалось, его крики слышны далеко за пределами леса."

            me "Уже было поздно сдерживаться."

            gregor "СТОП! СТОП!"

            me "Последний удар лишил подростка нескольких зубов."

            me "Из его рта стала стекала кровь."

            me "Я остановилась."

            iam "Слушаю тебя очень внимательно."

            gregor "Я нихрена не знаю."

            gregor "Правда."

            iam "Ты в этом абсолютно уверен?"

            gregor "Клянусь!"

            me "Я сделала очередной замах."

            gregor "Ладно, ладно."

            gregor "Я..."

            gregor "Просто..."

            gregor "Не могу говорить."

            iam "В каком смысле?"

            me "Я добилась своего, теперь он был явно напуган."

            me "Он явно был готов что-то рассказать, но словно никак не мог себя заставить."

            gregor "Я этого не делал."

            gregor "Всё что я сделал, это забрал его погремуху."

            gregor "И всё!"

            iam "Какую ещё погремуху?"

            if game_state.sammy_house_visited:

                me "Очевидно, речь шла о колейдоскопе."

            gregor "Да носился он с ней."

            gregor "Мы говорили ему, дай позырить."

            gregor "А он..."

            gregor "Послал Стэна куда подальше."

            gregor "Ну и собственно, разобраться надо было."

            gregor "За базар чтобы ответил."

            gregor "А он не отдавал."

            iam "Ты оправдываешь себя тем, что тебе не дали стащить чужую вещь?"

            gregor "Да хрень это всё! Понял я уже!"

            gregor "Эта штуковина выпала, когда он свалил."

            gregor "Я засунул её в сумку."

            gregor "Думал продать эту штуку."

            gregor "А когда венулся домой и открыл сумку..."

            gregor "Она исчезла!"

            iam "Это всё???"

            iam "Больше ничего не хочешь сказать?"

            me "Я вновь подняла камень."

            me "Грегор как будто пытался вымолвить хоть что-то, но словно невидимая сила останавливала его."

            gregor "Прошу!"

            gregor "Я НЕ МОГУ НИЧЕГО СКАЗАТЬ!"

            gregor "НЕ МОГУ!"

            me "Я не опускала камень, готовясь в любой момент нанести удар."

            me "После криков и мольбы о помощи я увидела настоящее безумие."

            me "На лице застыл испуг."

            me "Дыхание стало тяжёлым."

            gregor "Бэмми..."

            gregor "Гер..."

            gregor "Полье..."

            gregor "Гжербд..."

            gregor "Абывдрн..."

            me "Он издавал неестественные звуки, мало похожие на слова."

            me "Похоже..."

    me "Я сделала всё что смогла."

    me "Больше я ничего не смогу узнать."

    me "Теперь, осталось понять, что же мне с ним делать?"

    me "Если отпущу его сейчас, в Протекторате слишком быстро узнают о том, что произошло."

    me "Я не смогу избежать серьёзных последствий."

    me "Оставить его здесь?"

    me "Я смогу выиграть время и найти Сэмми."

    me "Это даст мне возможность оправдать свои действия."

    me "Как же мне поступить?"

    menu:

        "Отпустить Грегора":

            iam "Чёрт с тобой - иди!"

            me "Я развязала верёвки, на всякий случай приготовясь к возможной атаке."

            me "Но её не последовало."

            me "Как только подросток освободился, он мгновенно устремился в сторону города."

            me "Стоит ли так рисковать?"
            
            me "Учитывая, что теперь все узнают о том, что я допрашивала школьника."

            me "Хреново - это мягко сказано."

            me "Но мне нужно было спешить дальше."

            me "Осталось только понять - куда именно?"

        "Оставить Грегора в лесу":
            
            me "Если дам ему освободиться, Протекторат узнает обо всём достаточно быстро."

            me "Нельзя этого допустить, пока я не найду Сэмми."

            me "Я встала и оставила Грегора в полном одиночестве."

            me "Казалось, что он пытался что-то кричать мне вслед."

            me "Но мне нужно было спешить дальше."

    jump act_second_school_territory

label act_second_school_territory:

    me "Территория неподалёку от школы выглядела как обычно."

    me "Вот только пройдя значительное расстояния я начала замечать странности."

    me "Насколько зданий в округе, которые ещё на прошлой недели были окрашены в серый цвет, теперь пестрили всеми цветами радуги."

    me "Было похоже на какую-то показательную акцию, но, насколько я знала, суперзлодеи обычно изображают символы своих банд или лозунги."

    me "Здесь же была проделана огромная работа без какой-либо видимой цели."

    me "Впереди меня была оцеплённая территория, охраняемая просто безумным количеством сотрудников СКП."

    me "Я ощущала немало количество электроаппаратуры, которую запросто могла отключить."

    me "Вот только смысла в этом было ноль."

    me "Это всё-равно не поможет мне попасть внутрь."

    me "А учитывая, что мои способности известны общественности, не будет сложно догадаться кто именно стал виновником."

    me "Также я заметила по перемитру несколько клонов Легион."

    me "Суть её способности - в возможности контроллировать сразу пять своих тел, которые могут как действовать синхронно, так и заниматься разными задачами."

    me "Значит и члены её команды намного вероятно находятся здесь."

    me "Малейшая ошибка приведёт к тому, что мои намерения раскроют."

    me "Я тщательно изучила местность, насколько это было возможно."

    me "Единственный шанс, найти хотя бы небольшую уязвимую зону, чтобы попасть в парк в обход."

    me "Я значительно обошла территорию вокруг, прежде чем найти нечто подобное."

    me "В одном месте, под каменной оградой, было совсем небольшое отверстие."

    me "Пролезть туда было невозможно, однако если немного раскопать рыхлую землю под ним - шанс есть."

    me "Вот только невозможно узнать заранее - удастся ли мне там пролезть незаметно."

    me "Если меня обнаружат, я уже не отделаюсь выговором от Ронина."

    me "Более чем уверена, что это серьёзная статья."

    me "Я ещё могу повернуть обратно, но тогда вряд ли приближу себя к цели."

    me "Думай Айрин, думай!"

    menu:

        "Отправиться в другие места для расследования":

            me "Риск слишком высок."

            me "Я поняла, что не готова к нему."

            me "Едва сопротивляясь неутолимому желанию получить информацию о Сэмми, я развернулась и ушла прочь."

            me "Единственный плюс - у меня будет гораздо больше времени, чтобы заняться расследованием в других местах."

            me "Осталось выбрать куда отправиться дальше."

            $ game_state.school_short_visited = True

        "Попытаться проникнуть на территорию парка":

            me "Нет пути назад. Нужно действовать."

            me "Я начала аккуратно раскапывать землю руками, стараясь не привлекать внимание."

            me "Через несколько минут упорного труда отверстие стало достаточно широким, чтобы можно было пролезть."

            me "Я медленно проскользнула внутрь."

            me "Сердце бешено колотилось."

            me "В ближайшем окружении никого не было, но мой обзор всё ещё был ограничен."

            if not game_state.planar_is_ready:

                me "Я безумно пожалела о том, что со мной не было Марка."

            me "Я двигалась вперед, при каждом шаге ожидая худшего."

            me "Нужно было зайти за угол."

            me "В тот же момент я столкнулась с сотрудником СКП."

            me "Не было времени гадать: знает ли он кто я и должна ли быть здесь."

            me "Он замялся, а я действовала на уровне рефлексов."

            me "Электрический импульс угодил точно в цель и в следующую минуту сотрдник СКП лежал на земле и не двигался."

            me "Не успела я ужаснуться произосшедшему, как услышала голос позади себя."

            nobody_knight "Ничего себе."

            nobody_knight "Что это мы тут забыли?"

            me "Голос явно был мне знаком."

            me "Я обернулась."

            me "Сияющие латы, которые больше напоминали не рыцарские доспехи, а гламурный костюм."

            me "А ещё..."

            me "Меч, который я уже видела в кабинете, моего псевдопсихологического сеанса, в тот день, когда я первый раз пришла в офис Протектората."

            iam "Алекс?"

            me "Он подошёл ближе, абсолютно не опасаясь того, что я только что на его глазах вырубила агента."

            alex "На службе я, всё-таки, Ланцелот."

            iam "Хорошо Ланцелот, я полагаю, ты намерен меня задержать?"

            alex "Ну уж нет, очевидно в прямом боестолкновении ты окажешься лучше."

            iam "Тогда что? Сдашь меня?"

            alex "Возможно."

            me "И почему я вдруг ждала, что он скажет \"Нет!\""

            iam "Дашь мне объясниться?"

            alex "Зачем?"

            alex "Скажешь что переживала за пропавшего пацана, что у тебя не было выбора, потому что Ронин отстранил тебя от задания."

            iam "Ты уж слишком много знаешь."

            alex "Это простая логика, ничего более."

            iam "Если ты ответил \"возможно\", значит мы можем договориться?"

            me "Внезапно он снял шлем."

            me "Я увидела лицо парня, которое с самого начало внушало мне доверие, а под конец нашего \"сеанса\" - страх и тревогу."

            alex "Я позволю тебе пройти дальше."

            alex "Более того, я подскажу тебе как попасть на территорию, полную аномалий."

            alex "И я никому не сообщу о твоей самодеятельности."

            iam "Если я..."

            alex "Если ты, после всех событий, честно и откровенно расскажешь..."

            alex "О СВОЁМ ТРИГГЕРЕ!"

            me "Тот же самый азартный оскал на его лице."

            iam "Да нахрена тебе сдался мой триггер?"

            alex "Это уже моё дело."

            alex "От тебя требуется только выполнить условие."

            alex "Иначе, все узнают о том, что происходило здесь."

            alex "Не беспокойся, член СКП тоже будет молчать, пока жива наша сделка."

            me "Дерьмовей ситуации не придумать."

            me "Он даже не представляет, насколько ужасным может быть моё погуржение в прошлое."

            me "Иногда мне кажется, что я и от себя упорно прячу эти воспоминания."

            me "Может потом у меня и получится как-то избежать этого разговора..."

            me "Но сейчас, выбора не было."

            iam "Я согласна."

            alex "Прекрасно."

            alex "Удачи тебе в твоём расследовании."

            alex "И постарайся вернуться целой."

            alex "Пока."

            me "Он сделал дурацкий жест, символизирующий воздушный поцелуй, надел шлем на голову и указал мне сторону в которую нужно идти."

            me "Вряд ли бы он пытался меня обмануть в такой ситуации, если настолько сильно хочет получить желаемое."

            me "Я ринулась вперёд в указанном направлении и через несколько минут достигла маста, которое я искала."

            
            
            
            
            me "Воздух здесь казался другим - тяжелым и приторно сладким."

            me "Словно где-то вокруг горел склад с леденцами."

            me "Деревья были окрашены в разные цвета, также как и стены домов, которые я видела ранее."

            me "На некоторых из них были скамейки."

            me "Они были надёжно прикручены к стволам деревьев на самой разной высоте."

            me "Чем дальше я заходила, тем более безумным казалось мне окружение."

            me "Многие растения не были неподвижными."

            me "Они словно дышали - расширяясь и сужаясь с определённой периодичностью."

            me "В какой-то момент я захотела посмотреть вверх или найти тропу в пространстве между деревьями."

            me "Но всё, что мне удавалось разглядеть - неестественно яркий, почти ослепляющий, свет."

            me "Постоянное чувство безумного дискомфорта и тревоги одолевало меня."

            if not game_state.sammy_house_visited:

                me "Я долго бродила по парку и пыталась найти хотя бы малейшую зацепку."

                me "Но тщетно."

            if game_state.sammy_house_visited:

                me "Я уже не была уверена, что мне удасться вернуться назад самостоятельно."

                me "Слишком запутанно было всё вокруг."

                me "Но я не сдавалась и упорно старалась найти хоть что-то похожее на рисунки Сэмми."

                me "И наконец, мне повезло."

                me "После нескольких часов поисков, я обнаружила стену, на которой был обнаружен тот странный символ, на одном из рисунков пропавшего мальчика."

                me "Учитывая окружение, меня крайне удивил тот факт, что эта стена осталась нетронутой изменениями."

                me "Вокруг не было ничего не обычного для обычного взгляда."

                me "Но только не для моей силы."

                me "На расстоянии около 100-200 метрах от меня, где-то глубоко под землёй, я отчётливо ощущала электрическую активность."

                me "Компьютеры, генераторы, мониторы."

                me "Подземная база?"

                me "Моя Сила вела мня словно высокочувствительный локатор."

                me "На месте, где она достигла своего максимума, я не заметила ничего, что могло бы быть похоже на вход."

                me "Вооружившись стальной балкой, найденной неподалёку, я приготовилась к долгой изнурительной работе."

                me "В итоге, я смогла выкопать землю достаточно, чтобы обнаружить стальной люк, для открытия которого нужен был электронный ключ."

                me "Всё-таки мне повезло, что я, при должной концентрации, и есть тот самый электронный ключ."

                me "Через некоторое время игры с напряжением, дверь отворилась."

                me "Я ощутила холодный спёртый подвальный воздух."

                me "Было страшно спускаться, но останавливаться после такой находки было бы глупо."

                me "Воспользовавшись длинной лестницей я оказалась внизу."

                me "Оборудованная комната, чем-то напоминавшая нашу тренировочную базу."

                me "Вокруг те самые мониторы, которые я ощущала с поверхности."

                me "Я включила каждый из них и увидела то, что заставило меня содрогнуться."

                me "Сэмми сидел, облокотившись о стену тесной комнаты, похожей на тюремный карцер."

                me "Он был прикован цепями, а его глаза были закрыты."

                me "Проследив ещё некоторое время, я обнаружила неизвестного человека, облачённого в синюю броню с плотным шлемом, который зашёл в комнату к мальчику."

                me "Он взял его за руку, а своей рукой коснулся его шеи, словно проверяя пульс."

                me "Проведя с ним так несколько минут, неизвестный удалился."

                me "Дерьмо."

                me "Я не могу понять где его держат."

                me "Из этого помещения нет другого выхода, я бы почувствовала его."

                me "У меня даже нет камеры, чтобы записать или сфотографировать происходящее."

                me "Нужно будет вернуться сюда, иначе мне никто не поверит."

                me "Я выбралась из подвала и закрыла люк."

                me "Нужно было постараться из-за всех сил найти отсюда выход."

                me "Чувство найденной важной зацепки перемешивалось с чувством непреодолимой паники."

            me "Я двигалась словно наощупь по этому безумному месту."

            me "Электроника в черте города была моим единственным маяком."

            me "Наконец-то я добралась до места из которого мне удалось войти на территорию."

            me "Вокруг не было агентов СКП."

            me "Вдалеке только одна фигура."

            me "Фигура подняла меч вверх, а затем едва заметно помахала мне."

            me "Чёртов Алекс."

            me "Вертела я твои сделки."

            me "Позже об этом подумаю."

            if not game_state.sammy_house_visited:

                me "Судя по всему, этот путь был проделан зря."

                me "Единственная надежда, что я смогу найти зацепку, которая приведёт меня к нужному месту здесь."

                me "Если ещё не будет поздно."

                me "Я хотя бы знаю один, хоть и не самый надёжный вход."

            if not game_state.sammy_house_visited:

                me "В любом случае, моё проникновение сюда было не напрасным."

    jump act_second_wards_basement_after_investigation

    return

label act_second_wards_basement_after_investigation:

    $ all_team_ready = game_state.fahrenheit_is_ready and game_state.monument_is_ready and game_state.planar_is_ready
    $ all_team_not_ready = not game_state.fahrenheit_is_ready and not game_state.monument_is_ready and not game_state.planar_is_ready

    me "Я вернулась на тренировочную базу."

    if all_team_ready:

        iam "Мы отлично поработали, ребята."

        fahrenheit "Ещё как!"

        monument "Команда!"

        planar "Давайте лучше посмотрим, что у нас есть сейчас."

        me "Он был прав."

        me "Я собралась с мыслями и начала перечислять:"

        if game_state.kaleidoscope_clue:

            iam "Коллейдоскоп Сэмми - важная для него вещь, которая, намного вероятно может иметь значение."

        if game_state.secret_park_place_clue:

            iam "В парке есть несколько мест, которые подростки обозначали разными символами."

        if game_state.secret_sign_clue:

            iam "Символ на рисунке, который изобразил Сэмми."

        if game_state.sammy_video_clue:

            iam "Подвальное помещение, где находится видеонаблюдение за Сэмми."

        monument "Нужно попасть в парк как можно раньше."

        planar "И захватить необходимое для съёмки, чтобы подтвердить наши слова при отчёте."

        iam "Отлично."

        iam "Нам нельзя медлить."

        iam "Мы слишком много рисковали и обязаны предоставить остальным доказательства."

        fahrenheit "Тогда вперёд!"

        me "Мы надели наши маски и отправились к месту, откуда можно попасть в парк."

    if all_team_not_ready:

        iam "Ребята, вы должны мне помочь."

        monument "Ты что-то нашла?"

        iam "Да"

        if game_state.sammy_video_clue:

            iam "Сэмми удерживают в каком-то помещении."

            iam "Я без понятия где оно находится, но я видела собственными глазами."

            planar "Ничего не понял."

            planar "Так что именно ты видела?"

            iam "Я проникла в парк."

            iam "На камерах видеонаблюдения Сэмми был связан."

            iam "Какой-то человек или кейп приходил к нему."

            iam "Его явно держат там против своей воли."

        if not game_state.sammy_video_clue:

            iam "Все ответы находятся где-то в оцеплённой территории."

            iam "Там Сэмми прятался от хулиганов."

            iam "Он точно где-то там."

            iam "Вот что у меня есть - послушайте:"

            if game_state.kaleidoscope_clue:

                iam "Коллейдоскоп Сэмми - важная для него вещь, которая, намного вероятно может иметь значение."

            if game_state.secret_park_place_clue:

                iam "В парке есть несколько мест, которые подростки обозначали разными символами."

            if game_state.secret_sign_clue:

                iam "Символ на рисунке, который изобразил Сэмми."

            me "Ребята смотрели на меня с выражениями лица полными тревоги и озабоченности."

            planar "Ты серьёзно думаешь, что этого достаточно, чтобы убедить Ронина."

            planar "Да и вообще, достаточно чтобы убедить нас?"

        iam "Пока ещё нет, но..."

        me "Тут до меня дошло."

        iam "Что?"

        iam "В смысле?"

        iam "Я правду говорю."

        me "Алиса подошла ко мне и положила руку мне на плечо."

        fahrenheit "Айрин, успокойся."

        fahrenheit "Я понимаю о чём ты говоришь."

        fahrenheit "Но пойми нас."

        fahrenheit "Целый день ты была чёрти где."

        fahrenheit "И единственное чем ты одержима - любая возможность найти Сэмми."

        iam "Ребята, вы гоните?"

        iam "Я рисковала не только карьерой, но и свободой, чтобы получить это всё."

        monument "Даже если так и есть."

        monument "Даже если мы верим тебе."

        monument "Какой в этом смысл, если у тебя нет убедительных доказательств на руках?"

        me "Эмоции взяли верх надо мной."

        iam "Вы просто конченые!"

        iam "Даже не знаю как вас назвать."

        fahrenheit "Айрин..."

        me "Я не стала ждать, что она ответит."

        me "Просто выбежала из базы."

        me "Плевать."

        me "Плевать на них всех."

        me "Пойду туда одна и раздобуду доказательства."

        me "А затем, серьёзно подумаю о смене команды."

    if not all_team_ready and not all_team_not_ready:

        iam "Получилось."

        if game_state.fahrenheit_is_ready:

            fahrenheit "Я уже всё рассказала."

            fahrenheit "Теперь все в курсе дел."

        elif game_state.monument_is_ready:

            monument "Я уже всё рассказал."

            monument "Теперь все в курсе дел."

        elif game_state.planar_is_ready:

            planar "Я уже всё рассказал."

            planar "Теперь все в курсе дел."

        if not game_state.fahrenheit_is_ready:

            fahrenheit "Прости что сразу не доверилась тебе."

            fahrenheit "Это было слишком рискована для меня."

            fahrenheit "А теперь стыдно, что ты не смогла рассчитывать на мою помощь."

        if not game_state.monument_is_ready:

            monument "Ты просто огонь, Айрин!"

            monument "А вот я облажался."

            monument "Извини меня."

            monument "Впредь я не подведу тебя, обещаю!"

        if not game_state.planar_is_ready:

            monument "Ну что я могу сказать."

            monument "Шансов что-то разузнать было мало."

            monument "Но это не значит, что стоило держаться в стороне."

            planar "Сорян."

        iam "Сейчас не время извиняться."

        iam "У нас ещё много работы."

        iam "Нужно сейчас сосредоточиться на этом."

        planar "Давайте лучше посмотрим, что у нас есть сейчас."

        me "Он был прав."

        me "Я собралась с мыслями и начала перечислять:"

        if game_state.kaleidoscope_clue:

            iam "Коллейдоскоп Сэмми - важная для него вещь, которая, намного вероятно может иметь значение."

        if game_state.secret_park_place_clue:

            iam "В парке есть несколько мест, которые подростки обозначали разными символами."

        if game_state.secret_sign_clue:

            iam "Символ на рисунке, который изобразил Сэмми."

        if game_state.sammy_video_clue:

            iam "Подвальное помещение, где находится видеонаблюдение за Сэмми."

        monument "Нужно попасть в парк как можно раньше."

        planar "И захватить необходимое для съёмки, чтобы подтвердить наши слова при отчёте."

        iam "Отлично."

        iam "Нам нельзя медлить."

        iam "Мы слишком много рисковали и обязаны предоставить остальным доказательства."

        fahrenheit "Тогда вперёд!"

        me "Мы надели наши маски и отправились к месту, откуда можно было попасть в парк."

    jump act_second_night_base

label act_second_night_base:

    # Ночью из-за проникновения Айрин среагировала группировка Учителя, что привело к обстрелам сотрудников СКП, однако про неё никто не знает и Протекторат будет думать, что это Злодеи
    # Тут потом окажется, что Резонанс и Вакуум проследовали за Айрин, чтобы спасти её, поэтому в итоге попадут под подозрение и это скажется на следующем эпизоде - конфликт Злодеев и Протектората

    jump act_second_night_base_battle

    return 

label act_second_night_base_battle:

    # Битва в ночном парке
    jump act_second_night_base_after_battle

    return

label act_second_night_base_after_battle:

    # После битвы в ночном парке
    jump act_second_ronin_cabinet_after_investigation

    return

label act_second_ronin_cabinet_after_investigation:

    # Отчёт у Ронина после расследования
    jump act_second_irene_career

    return

label act_second_irene_career:

    # Отчёт у Ронина после расследования
    jump act_second_new_clue

    return

label act_second_new_clue:

    # Отчёт у Ронина после расследования
    jump act_second_new_clue

    return