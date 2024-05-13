screen battle_overlay(player_hp, player_mp, enemy_hp, enemy_mp):
    bar style "bar_hp" value AnimatedValue(value=player_hp, range=player.max_hp, delay=0.25) pos(500, 150)
    bar style "bar_mp" value AnimatedValue(value=player_mp, range=player.max_mp, delay=0.25) pos(500, 200)
    text "[player_hp]/[player.max_hp]" pos(550, 155)
    text "[player_mp]/[player.max_mp]" pos(550, 205)

    bar style "bar_hp" value AnimatedValue(value=enemy_hp, range=enemy.max_hp, delay=0.25) pos(1200, 150)
    bar style "bar_mp" value AnimatedValue(value=enemy_mp, range=enemy.max_mp, delay=0.25) pos(1200, 200)
    text "[enemy_hp]/[enemy.max_hp]" pos(1250, 155)
    text "[enemy_mp]/[enemy.max_mp]" pos(1250, 205)

screen monster_dmg(damage, x, y):
    style_group "dmg"
    text "[damage]" anchor (.5,.5) pos (x, y) at shake_fade
    timer 1 action Hide('monster_dmg')

screen enemy_effects_screen(active_effects):
    # Этот скрин отображает все активные эффекты в заданной позиции

    $ x = 0
    for effect in active_effects:
        imagebutton:
            idle effect
            xpos enemy_x_pos + x - 120
            ypos enemy_y_pos - 50
            action NullAction()  # Элементы будут статичны, без действий по клику
        $ x += 100

screen player_effects_screen(active_effects):
    # Этот скрин отображает все активные эффекты в заданной позиции

    $ x = 0
    for effect in active_effects:
        imagebutton:
            idle effect
            xpos player_x_pos + x - 120
            ypos player_y_pos - 50
            action NullAction()  # Элементы будут статичны, без действий по клику
        $ x += 100

screen skill_description_screen(icon_path, skill_name, skill_description):
    # Центральная панель скиллов
    add "images/battle/skillbox.png":
            xpos 600
            ypos 750
            xsize 700
            ysize 300

    # Расположение скиллов
    imagebutton:
        idle icon_path
        xpos 650
        ypos 770

    text skill_name:
        xpos 780
        ypos 810
        size 24
        color "#FFFFFF"

    text skill_description:
        xpos 660
        ypos 900
        size 18
        color "#000000"

screen blank_clickable_screen():
    # Создаем полноэкранный прозрачный textbutton для обработки клика
    textbutton "":
        xalign 0.0
        yalign 0.0
        xsize config.screen_width
        ysize config.screen_height
        background None  # Нет фона, полностью прозрачный
        action [Hide("skill_description_screen")]

screen player_turn_screen(players, active_player_number):
    zorder 200
    $ green_matrix = im.matrix.tint(0.0, 1.0, 0.0)
    $ red_matrix = im.matrix.tint(1.0, 0.0, 0.0)

    add "images/battle/turn_order_container.png":
        xpos -300
        ypos 10

    for i in range(0, len(players)):
        $ player_avatar_path = players[i].avatar
        $ player_avatar_path_active = im.MatrixColor(players[i].avatar, green_matrix)
        $ player_avatar_path_dead = im.MatrixColor(players[i].avatar, red_matrix)

        if i == active_player_number:
            imagebutton:
                ypos 10
                xoffset i * 103
                idle player_avatar_path_active

        elif players[i].hp <= 0:
            imagebutton:
                ypos 10
                xoffset i * 103
                idle player_avatar_path_dead

        else:
            imagebutton:
                ypos 10
                xoffset i * 103
                idle player_avatar_path

screen enemy_turn_screen(enemies, active_enemy_number):
    zorder 200
    $ green_matrix = im.matrix.tint(0.0, 1.0, 0.0)
    $ red_matrix = im.matrix.tint(1.0, 0.0, 0.0)

    $ container_width = 1280
    $ avatar_width = 103
    $ x_offset = 642

    add "images/battle/turn_order_container.png":
        xpos 1000
        ypos 10

    for i in range(0, len(enemies)):
        $ enemy_avatar_path = enemies[i].avatar
        $ enemy_avatar_path_active = im.MatrixColor(enemies[i].avatar, green_matrix)
        $ enemy_avatar_path_dead = im.MatrixColor(enemies[i].avatar, red_matrix)

        if i == active_enemy_number:
            imagebutton:
                ypos 10
                # Рассчитываем позицию x так, чтобы аватарки шли справа налево
                xoffset x_offset + container_width - (i + 1) * avatar_width
                idle enemy_avatar_path_active

        elif enemies[i].hp <= 0:
            imagebutton:
                ypos 10
                xoffset x_offset + container_width - (i + 1) * avatar_width
                idle enemy_avatar_path_dead

        else:
            imagebutton:
                ypos 10
                # Аналогично рассчитываем позицию для неактивных аватаров
                xoffset x_offset + container_width - (i + 1) * avatar_width
                idle enemy_avatar_path



screen skill_hint_screen(attack_options):
    zorder 200

    $ skills_count = len(attack_options)
    $ y_initial_pos = 518

    for i in range (skills_count):
        $ y_initial_pos -= 40

    vbox:
        xpos 650
        ypos y_initial_pos

        for i in range(skills_count):
            $ icon_path = "images/battle/hint_circle.png"
            $ icon_path_hovered = im.MatrixColor("images/battle/hint_circle.png", im.matrix.brightness(0.3))
            imagebutton:
                idle icon_path
                hover icon_path_hovered
                action [Show("skill_description_screen", icon_path=attack_options[i].icon_path, skill_name=attack_options[i].name, skill_description=attack_options[i].description),]
                yoffset i * 52