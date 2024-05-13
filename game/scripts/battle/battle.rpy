init python:
    from game.scripts.battle.battle_scripts.fighter import Fighter
    from game.scripts.battle.battle_scripts.skills.attack_skills.attack_skill import AttackSkill
    from game.scripts.battle.battle_scripts.skills.armor_skills.armor_skill import ArmorSkill
    from game.scripts.battle.battle_scripts.skills.restore_skills.restore_skill import RestoreSkill
    from game.scripts.battle.battle_scripts.skills.attack_skills.electric_impulse import ElectricImpulse
    from game.scripts.battle.battle_scripts.skills.attack_skills.electric_thunder import ElectricThunder
    from game.scripts.battle.battle_scripts.skills.attack_skills.electric_shock import ElectricShock
    from game.scripts.battle.battle_scripts.skills.armor_skills.electric_armor import ElectricArmor
    from game.scripts.battle.battle_scripts.skills.restore_skills.restore_electricity import RestoreElectricity

    from game.scripts.battle.battle_scripts.effects.stun_effect import StunEffect
    import random

    def update_enemy_effects():
        for effect in enemy.effects:
            if effect.duration <= 0:
                enemy.effects.remove(effect)
                continue

            effect.duration -= 1

define player_x_pos = 350
define player_y_pos = 150

define enemy_x_pos = 1600
define enemy_y_pos = 150

label test_battle:
    default active_player_number = 0
    default active_enemy_number = 0

    image stunned_effect = "images/effects/stunned.png"
    image effect_icon = "images/effects/stunned.png"

    scene bg

    show player_idle as battler at left, char_sway
    show enemy_idle as enemy at right, char_sway

    show screen battle_overlay(player.hp, player.mp, enemy.hp, enemy.mp)
    show screen player_turn_screen(players, active_player_number)
    show screen enemy_turn_screen(enemies, active_enemy_number)

    jump player_select_turn

label player_select_turn:
    show screen player_turn_screen(players, active_player_number)

    if len(players) == 1:
        jump player_turn

    # Формирование списка пунктов меню с проверкой здоровья
    $ menu_items = [(player.name if player.hp > 0 else "{} (недоступен)".format(player.name), i if player.hp > 0 else None) for i, player in enumerate(players)]

    # Отображение меню и получение выбранного индекса или None для недоступных игроков
    $ selected_player_index = renpy.display_menu(menu_items)

    $ active_player_number = selected_player_index
    $ player = players[active_player_number]
    show player_idle as battler at left, char_sway
    show screen player_turn_screen(players, active_player_number)
    show screen battle_overlay(player.hp, player.mp, enemy.hp, enemy.mp)
    jump player_turn

label player_turn:

    show screen blank_clickable_screen

    $ effects_images = [effect.image for effect in player.effects]
    show screen player_effects_screen(effects_images)

    $ effects_images = [effect.image for effect in enemy.effects]
    show screen enemy_effects_screen(effects_images)

    if any(isinstance(effect, StunEffect) for effect in player.effects):
        hide screen blank_clickable_screen

        me "Я оглушена, не могу действовать."

        show screen blank_clickable_screen

        $ player.update_effects()
        jump enemy_select_turn

    menu:
        "Атака":

            $ attack_skills = [skill for skill in player.skills if isinstance(skill, AttackSkill)]
            show screen skill_hint_screen(attack_skills)

            $ attack_options = [(skill.name, skill if player.mp >= skill.cost else None) for skill in player.skills if isinstance(skill, AttackSkill)]
            $ attack_options.append(("Назад", "back"))

            $ chosen_skill = renpy.display_menu(attack_options)

            hide screen skill_hint_screen
            hide screen skill_description_screen
            hide screen blank_clickable_screen

            if chosen_skill == "back":
                jump player_turn

            $ player.use_mp(chosen_skill.cost)
            $ damage = chosen_skill.get_damage()
            $ effect = chosen_skill.get_effect()

            if effect is not None:
                $ enemy.effects.append(effect)

            $ enemy.take_damage(damage)

            show screen monster_dmg(damage, enemy_x_pos, enemy_y_pos)
            show screen battle_overlay(player.hp, player.mp, enemy.hp, enemy.mp)
            $ renpy.play(chosen_skill.get_success_sound())

            hide enemy_idle
            show enemy_idle as enemy at right, dying_fade_out, invert_colors
            pause 0.1
            show enemy_idle as enemy at right, char_sway, reset_invert

            $ success_text = chosen_skill.get_success_text()
            # me "[success_text]"
            $ renpy.pause(1.5, hard=True)

            if all(enemy.hp <= 0 for enemy in enemies):
                $ renpy.play(character_battle_dead)
                hide enemy_idle
                show enemy_idle as enemy at right, dying_fade_out, invert_colors
                hide screen blank_clickable_screen
                jump victory

            if enemy.hp <= 0:
                $ renpy.play(character_battle_dead)
                show enemy_idle as enemy at right, dying_fade_out, invert_colors
                $ renpy.pause(2.5, hard=True)
                hide enemy

                jump enemy_select_turn

        "Защита":
            $ armor_skills = [skill for skill in player.skills if isinstance(skill, ArmorSkill)]
            show screen skill_hint_screen(armor_skills)

            $ armor_options = [(skill.name, skill if player.mp >= skill.cost else None) for skill in player.skills if isinstance(skill, ArmorSkill)]
            $ armor_options.append(("Назад", "back"))

            $ chosen_skill = renpy.display_menu([ (name, skill) for name, skill in armor_options ])

            hide screen skill_hint_screen
            hide screen skill_description_screen
            hide screen blank_clickable_screen

            if chosen_skill == "back":
                jump player_turn

            $ player.use_mp(chosen_skill.cost)
            $ heal_amount = chosen_skill.get_heal()
            $ player.heal(heal_amount)

            show screen battle_overlay(player.hp, player.mp, enemy.hp, enemy.mp)
            $ renpy.play(chosen_skill.get_success_sound())

            $ success_text = chosen_skill.get_success_text()
            # me "[success_text]"
            $ renpy.pause(1.5, hard=True)

        "Ресурсы":
            $ restore_skills = [skill for skill in player.skills if isinstance(skill, RestoreSkill)]
            show screen skill_hint_screen(restore_skills)

            $ restore_options = [(skill.name, skill if player.mp >= skill.cost else None) for skill in player.skills if isinstance(skill, RestoreSkill)]
            $ restore_options.append(("Назад", "back"))

            $ chosen_skill = renpy.display_menu([ (name, skill) for name, skill in restore_options ])

            hide screen skill_hint_screen
            hide screen skill_description_screen
            hide screen blank_clickable_screen

            if chosen_skill == "back":
                jump player_turn

            $ restore_amount = chosen_skill.get_restore()
            $ player.restore_mp(restore_amount)

            show screen battle_overlay(player.hp, player.mp, enemy.hp, enemy.mp)
            $ renpy.play(chosen_skill.get_success_sound())

            $ success_text = chosen_skill.get_success_text()
            # me "[success_text]"
            $ renpy.pause(1.5, hard=True)

        "Пропустить":
            hide screen skill_hint_screen
            hide screen skill_description_screen
            hide screen blank_clickable_screen
            hide screen blank_clickable_screen

            me "Я ничего не делаю."

            show screen blank_clickable_screen

    jump enemy_select_turn

label enemy_select_turn:
    show screen enemy_turn_screen(enemies, active_enemy_number)

    if len(enemies) == 1:
        jump enemy_turn

    $ active_enemies = [i for i, enemy in enumerate(enemies) if enemy.hp > 0]

    if len(active_enemies) > 0:
        $ active_enemy_number = random.choice(active_enemies)
        $ enemy = enemies[active_enemy_number]
        show enemy_idle as enemy at right, char_sway
        show screen enemy_turn_screen(enemies, active_enemy_number)
        show screen battle_overlay(player.hp, player.mp, enemy.hp, enemy.mp)
        jump enemy_turn

label enemy_turn:

    if enemy.hp > 0:

        $ effects_images = [effect.image for effect in player.effects]
        show screen player_effects_screen(effects_images)

        $ effects_images = [effect.image for effect in enemy.effects]
        show screen enemy_effects_screen(effects_images)

        if any(isinstance(effect, StunEffect) for effect in enemy.effects):
            hide screen blank_clickable_screen

            me "Противник оглушен и пропускает ход."

            show screen blank_clickable_screen

            $ enemy.update_effects()
            jump player_select_turn

        $ available_skills = [skill for skill in enemy.skills if enemy.mp >= skill.cost]

        if available_skills:

            $ chosen_skill = random.choice(available_skills)

            if isinstance(chosen_skill, AttackSkill):
                $ enemy.use_mp(chosen_skill.cost)
                $ damage = chosen_skill.get_damage()

                $ effect = chosen_skill.get_effect()

                if effect is not None:
                    $ player.effects.append(effect)

                $ player.take_damage(damage)

                show screen monster_dmg(damage, player_x_pos, player_y_pos)
                show screen battle_overlay(player.hp, player.mp, enemy.hp, enemy.mp)
                $ renpy.play(rock_battle_sound)

                hide player_idle
                show player_idle as battler at left, dying_fade_out, invert_colors
                pause 0.1
                show player_idle as battler at left, char_sway, reset_invert

                $ success_text = chosen_skill.get_success_text()
                # me "[success_text]"
                $ renpy.pause(1.5, hard=True)

                if all(player.hp <= 0 for player in players):
                    $ renpy.play(character_battle_dead)
                    show player_idle as battler at left, dying_fade_out, invert_colors
                    hide screen blank_clickable_screen
                    jump defeat

                if player.hp <= 0:
                    $ renpy.play(character_battle_dead)
                    hide battler
                    show player_idle as battler at left, dying_fade_out, invert_colors
                    $ renpy.pause(2.5, hard=True)
                    hide battler

                    jump player_select_turn

            elif isinstance(chosen_skill, ArmorSkill):
                $ enemy.use_mp(chosen_skill.cost)
                $ heal_amount = chosen_skill.get_heal()
                $ enemy.heal(heal_amount)

                show screen battle_overlay(player.hp, player.mp, enemy.hp, enemy.mp)
                $ renpy.play(chosen_skill.get_success_sound())

                $ success_text = chosen_skill.get_success_text()
                # me "[success_text]"
                $ renpy.pause(1.5, hard=True)

            elif isinstance(chosen_skill, RestoreSkill):
                $ restore_amount = chosen_skill.get_restore()
                $ enemy.restore_mp(restore_amount)

                show screen battle_overlay(player.hp, player.mp, enemy.hp, enemy.mp)
                $ renpy.play(chosen_skill.get_success_sound())

                $ success_text = chosen_skill.get_success_text()
                # me "[success_text]"
                $ renpy.pause(1.5, hard=True)
        else:
            hide screen blank_clickable_screen

            me "Противник ничего не делает."

            show screen blank_clickable_screen

    jump player_select_turn
    return

label victory:
    $ game_state.battles[game_state.current_battle_tag] = True
    $ renpy.pause(2.5, hard=True)
    hide screen blank_clickable_screen
    hide screen player_effects_screen
    hide screen enemy_effects_screen
    hide screen skill_hint_screen
    hide screen monster_dmg
    hide screen battle_overlay
    hide screen player_turn_screen
    hide screen enemy_turn_screen

    jump expression game_state.training_win_label

    return

label defeat:
    $ game_state.battles[game_state.current_battle_tag] = False
    $ renpy.pause(2.5, hard=True)
    hide screen blank_clickable_screen
    hide screen player_effects_screen
    hide screen enemy_effects_screen
    hide screen skill_hint_screen
    hide screen monster_dmg
    hide screen battle_overlay
    hide screen player_turn_screen
    hide screen enemy_turn_screen

    jump expression game_state.training_lose_label

    return