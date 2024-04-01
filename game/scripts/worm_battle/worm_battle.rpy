# Определяем персонажей и их характеристики
init python:
    from game.scripts.worm_battle.character import Character
    from game.scripts.worm_battle.skill import Skill
    from game.scripts.worm_battle.game import Game

    # TRANSfROMS
    CHAR_MOVE_LINEAR = 0.5
    CHAR_MOVE_XOFFSET_MAX = 10
    CHAR_MOVE_XOFFSET_MIN = -10

    INVISIBLE = 0.0
    VISIBLE = 1.0

    DAMAGE_ANIM_SPEED = 0.25
    DAMAGE_ANIM_DURATION = 1.0
    DAMAGE_ANIM_DELAY = 1.5

    # PLAYER POSTION
    PLAYER_X_POS = 0.1
    PLAYER_STATS_X_POS = 0.22
    PLAYER_Y_POS = 1.8
    PLAYER_STATS_Y_POS = 0.2

    # ENEMY POSITION
    ENEMY_X_POS = 0.8
    ENEMY_STATS_X_POS = 0.73
    ENEMY_Y_POS = 1.0
    ENEMY_STATS_Y_POS = 0.2

    # DAMAGE ON PLAYER
    DAMAGE_ON_PLAYER_X_ALIGN = 0.20
    DAMAGE_ON_PLAYER_Y_ALIGN = 0.2

    # DAMAGE ON ENEMY
    DAMAGE_ON_ENEMY_X_ALIGN = 0.71
    DAMAGE_ON_ENEMY_Y_ALIGN = 0.2

    # SKILLS PANEL
    SKILLS_PANEL_X_ALING = 0.5
    SKILLS_PANEL_Y_ALING = 0.5
    SKILLS_PANEL_X_SIZE = 1280
    SKILLS_PANEL_Y_SIZE = 720

    # SKILLS HINT POSITION
    SKILL_HINT_X_ALIGN = 0.73
    SKILL_HINT_Y_ALIGN = 0.23

    # SKILLS POSITION
    SKILLS_INITIAL_X_ALIGN = 0.22
    SKILLS_Y_ALIGN = 0.23
    SKILLS_X_MOVER = 0.07

    # DIFFICULTY TEXT POSITION
    DIFFICULTY_TEXT_NUMBER_X_ALIGN = 0.502
    DIFFICULTY_TEXT_NUMBER_Y_ALIGN = 0.34

    # SKILLS SLOTS POSITION
    SKILLS_SLOTS_X_ALIGN = 0.5
    SKILLS_SLOTS_Y_ALIGN = 0.42
    SKILLS_SLOTS_SPACING = 10

    SKILLS_SLOTS_COUNT = 3

    # DICE POSITION
    DICE_X_ALING = 0.5
    DICE_Y_ALING = 0.6

    # SUBMIT BUTTON
    SUBMIT_BUTTON_X_ALIGN = 0.5
    SUBMIT_BUTTON_Y_ALIGN = 0.72

    # RESULT TEXT
    RESULT_TEXT_X_ALIGN = 0.5
    RESULT_TEXT_Y_ALIGN = 0.72

    # RESULT NUMBER
    RESULT_NUMBER_X_ALIGN = 0.502
    RESULT_NUMBER_Y_ALIGN = 0.585

    def fight_hint_text_generator():
        result_text = ""
        hints = []

        hints.append("1. Выберите от ОДНОЙ до ТРЁХ способностей.")
        hints.append("2. Каждая способность имеет СЛОЖНОСТЬ против\nконкретного противника.")
        hints.append("3. Больше способностей за ход - выше СЛОЖНОСТЬ.")
        hints.append("4. Против каждого противника есть \nУЯЗВИМОСТЬ (уникальная комбинация), приводящая \nк победе.")
        hints.append("5. Сложность УЯЗВИМОСТИ всегда равна 10.")
        hints.append("6. Чтобы найти УЯЗВИМОСТЬ следите за индикаторами:")

        hints.append("{color=#FF0000}КРАСНЫЙ{/color} - способности нет в УЯЗВИМОСТИ.")
        hints.append("{color=#FFFF00}ЖЁЛТЫЙ{/color} - способность должна быть не на этой ячейке.")
        hints.append("{color=#00FF00}ЗЕЛЁНЫЙ{/color} - способность в нужной ячейке.")

        for hint in hints:
            result_text += hint + "\n\n"

        return result_text

# Стили
style hint_text:
    xalign 0.03
    yalign 0.06
    size 40
    color "#FFFFFF"

style fight_hint:
    xalign 0.25
    yalign 0.5
    size 15
    color "#000000"    

style battle_stats:
    size 40
    color "#FFFFFF"

style battle_action:
    size 20

style damage_on_enemy:
    xalign DAMAGE_ON_ENEMY_X_ALIGN
    yalign DAMAGE_ON_ENEMY_Y_ALIGN
    color "#FF0000"
    size 80

style damage_on_player:
    xalign DAMAGE_ON_PLAYER_X_ALIGN
    yalign DAMAGE_ON_PLAYER_Y_ALIGN
    color "#FF0000"
    size 80

style title_skill:
    size 24
    color "#FFFFFF"

style description_skill:
    size 20
    color "#000000"

style skill_box:
    xalign 0.42
    yalign 0.75
    color "#FF0000"
    size 80

style result_check_text:
    size 40

style result_check_number:
    size 40

style skill_slot_blank:
    background None

style skill_slot_red:
    background "#FF0000"

style skill_slot_yellow:
    background "#FFF200"

style skill_slot_green:
    background "#00FF00"

##################################################################################
# Универсальный transform для эффекта hover
transform hover_effect:
    on hover:
        alpha 0.8
    on idle:
        alpha 1.0

# Анимация движения персонажей влево и вправо
transform sway:
    linear CHAR_MOVE_LINEAR xoffset CHAR_MOVE_XOFFSET_MIN
    linear CHAR_MOVE_LINEAR xoffset CHAR_MOVE_XOFFSET_MAX
    linear CHAR_MOVE_LINEAR xoffset CHAR_MOVE_XOFFSET_MIN
    repeat

# Анимация цифры с уроном по противику
transform damage_animation_transform:
    alpha INVISIBLE
    linear DAMAGE_ANIM_SPEED alpha VISIBLE
    linear DAMAGE_ANIM_DURATION alpha VISIBLE
    linear DAMAGE_ANIM_SPEED alpha INVISIBLE

# Анимация цифры с уроном по персонажу игрока
transform damage_enemy_animation_transform:
    alpha INVISIBLE
    pause DAMAGE_ANIM_DELAY
    linear DAMAGE_ANIM_SPEED alpha VISIBLE
    linear DAMAGE_ANIM_DURATION alpha VISIBLE
    linear DAMAGE_ANIM_SPEED alpha INVISIBLE

# Анимация смерти
transform death:
    alpha 1.0
    linear 2.5 alpha 0.0

##################################################################################

# Экран для отображения текстовых подсказок
screen game_hint(hint_message):
    zorder 1000

    add "images/battle/messagebox.png":
        xalign -0.5
        yalign 0.0
        
    text hint_message:
        style "hint_text"

# Экран урона по противнику
screen damage_animation(damage_amount=0, target=""):
    if damage_amount > 0:
        text str(damage_amount):
            style "damage_on_enemy"
            at damage_animation_transform
    else:
        text "Промах":
            style "damage_on_enemy"
            at damage_animation_transform

# Экран урона по игроку
screen damage_animation_enemy(damage_amount=0, target=""):
    if damage_amount > 0:
        text str(damage_amount):
            style "damage_on_player"
            at damage_enemy_animation_transform
    else:
        text "Промах":
            style "damage_on_player"
            at damage_enemy_animation_transform

    timer 3.0 action Function(game.finish_damage_animation)

# ЭКРАН БОЯ
screen battle_screen():
    
    # Фон
    add game_state.current_battle_background

    # Расположение персонажа Игрока
    if not game.player_dead:
        add game.player.image:
            xalign PLAYER_X_POS
            yalign PLAYER_Y_POS
            at sway

        text "[game.player.hp]/[game.player.max_hp]":
            xalign PLAYER_STATS_X_POS
            yalign PLAYER_STATS_Y_POS
            style "battle_stats"
    else:
        add game.player.image:
            xalign PLAYER_X_POS
            yalign PLAYER_Y_POS
            at death

        text "[game.player.hp]/[game.player.max_hp]":
            xalign PLAYER_STATS_X_POS
            yalign PLAYER_STATS_Y_POS
            style "battle_stats"
            at death


    # Расположение Противника
    if not game.enemy_dead:
        imagebutton:
            idle game.enemy.image
            xalign ENEMY_X_POS
            yalign ENEMY_Y_POS
            at sway, hover_effect
            action [Function(game.start_select_skills), Show("skill_panel")]

        text "[game.enemy.hp]/[game.enemy.max_hp]":
            xalign ENEMY_STATS_X_POS
            ypos ENEMY_STATS_Y_POS
            style "battle_stats"

    else:
        imagebutton:
            idle game.enemy.image
            xalign ENEMY_X_POS
            yalign ENEMY_Y_POS
            at death
            action Show("skill_panel")

        text "[game.enemy.hp]/[game.enemy.max_hp]":
            xalign ENEMY_STATS_X_POS
            ypos ENEMY_STATS_Y_POS
            style "battle_stats"
            at death        

# ЭКРАН ОПИСАНИЯ СКИЛЛА
screen skill_info(skill_image="images/skills/blank.png", skill_name="", skill_description=""):
    zorder 200
    modal False
    vbox:
        xalign SKILL_HINT_X_ALIGN
        yalign SKILL_HINT_Y_ALIGN
        add skill_image
        text skill_name:
            style "title_skill"
        text skill_description:
            style "description_skill"

# ЭКРАН ВЫБОРА СКИЛЛОВ
screen skill_panel():

    # Центральная панель скиллов
    add "images/battle/skillbox.png":
            xalign SKILLS_PANEL_X_ALING
            yalign SKILLS_PANEL_Y_ALING
            xsize SKILLS_PANEL_X_SIZE
            ysize SKILLS_PANEL_Y_SIZE

    # Расположение скиллов
    $ x_align = SKILLS_INITIAL_X_ALIGN
    for skill in game.player.skills:
        imagebutton:
            idle skill.img
            hover skill.img
            xalign x_align
            yalign SKILLS_Y_ALIGN
            action Function(game.add_skill_to_slot, skill)
            at hover_effect
            hovered [Show("skill_info", skill_image=skill.img, skill_name=skill.name, skill_description=skill.description),]
            unhovered [Hide("skill_info"),]
        $ x_align += SKILLS_X_MOVER

    text fight_hint_text_generator():
        style "fight_hint"

    # Динамические слоты для скиллов
    hbox:
        xalign SKILLS_SLOTS_X_ALIGN
        yalign SKILLS_SLOTS_Y_ALIGN
        spacing SKILLS_SLOTS_SPACING
    hbox:
        xalign SKILLS_SLOTS_X_ALIGN
        yalign SKILLS_SLOTS_Y_ALIGN
        spacing SKILLS_SLOTS_SPACING
        for i in range(SKILLS_SLOTS_COUNT):
            $ slot_skill = game.skill_slots[i]
            $ slot_img = slot_skill.img if slot_skill is not None else "images/skills/blank.png"
            $ slot_style = game.slot_styles[i]
            if slot_skill is not None:
                $ skill_name = slot_skill.name
                $ skill_description = slot_skill.description
                imagebutton:
                    idle slot_img
                    hover slot_img
                    action Function(game.clear_slot, i)
                    at hover_effect
                    hovered [Show("skill_info", skill_image=slot_img, skill_name=skill_name, skill_description=skill_description),]
                    unhovered [Hide("skill_info"),]
                    style slot_style
            else:
                imagebutton:
                    idle "images/skills/blank.png"
                    action NullAction()
                    style slot_style
    
    # Таймер для анимации числа, запускается после нажатия кнопки "Подтвердить"
    if game.number_animation_running:
        timer 0.02 repeat True action Function(game.animate_number)

    # Расположение кубика
    add "images/battle/dice.png":
        xalign DICE_X_ALING
        yalign DICE_Y_ALING

    # Расположение числового результата проверки
    text str(game.current_number):
        xalign RESULT_NUMBER_X_ALIGN
        yalign RESULT_NUMBER_Y_ALIGN
        color game.number_color
        style "result_check_number"

    $ current_difficulty = ""
    if game.current_difficulty == 0:
        $ current_difficulty = ""
    else:
        $ current_difficulty = game.current_difficulty

    # Расположение требуемой сложности для проверки
    text "Сложность: " + str(current_difficulty):
        xalign DIFFICULTY_TEXT_NUMBER_X_ALIGN
        yalign DIFFICULTY_TEXT_NUMBER_Y_ALIGN

    # Кнопка Подтвердить
    if any(slot is not None for slot in game.skill_slots) and game.show_confirm_button:
        textbutton "Подтвердить":
            action [Function(game.save_skills_and_start_number_animation), Function(game.update_slot_styles_based_on_weakness), Function(game.finish_select_skills)]
            xalign SUBMIT_BUTTON_X_ALIGN
            yalign SUBMIT_BUTTON_Y_ALIGN

    # Определение текста после результата броска Успех или Провал
    $ result_text = "Успех" if game.number_color == "#00FF00" else "Провал"
    $ result_color = game.number_color

    if not game.number_animation_running and not game.show_confirm_button:
        text result_text:
            xalign RESULT_TEXT_X_ALIGN
            yalign RESULT_TEXT_Y_ALIGN
            color result_color
            style "result_check_text"

    # Закрыть экран, если выбор сделан
    if game.should_close_panel:
        timer 2.0 action Function(game.hide_skill_panel)

# ИГРОВОЙ ЦИКЛ
label worm_battle:
    $ game.start_battle()
    call screen battle_screen
    return

screen check_end_game_conditions:
    timer 3.5 action [Function(game.hide_all_battle_screens), If(game.enemy.hp <= 0, Jump(game_state.training_win_label), If(game.player.hp <= 0 and game.enemy.hp > 0, Jump(game_state.training_lose_label))), Hide("check_end_game_conditions")]