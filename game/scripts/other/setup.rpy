init python:
    import copy
    from game.scripts.battle.battle_scripts.game_state import GameState
    from game.scripts.worm_battle.character import Character
    from game.scripts.worm_battle.skill import Skill
    from game.scripts.worm_battle.game import Game

    if not renpy.variant("touch"):
        config.mouse = {"default":[ ("images/cursor.png", 1, 1) ] }
    
    game_state = GameState(renpy)

    electric_pulse = Skill(
        renpy,
        name="Электрический Импульс",
        img="images/skills/electric_pulse_border.png",
        damage_min=3,
        damage_max=6,
        description="Наносит от 3 до 6 кинетического урона."
    )

    thunderbolt = Skill(
        renpy,
        name="Молния",
        img="images/skills/thunderbolt_border.png",
        damage_min=4,
        damage_max=8,
        description="Наносит от 5 до 8 кинетического урона.\n30% шанс оттолкнуть противника."
    )

    overload = Skill(
        renpy,
        name="Перегруз",
        img="images/skills/overload_border.png",
        damage_min=6,
        damage_max=10,
        description="Перегруз техники вокруг, провоцирующий взрыв.\nНаносит от 10 до 15 взрывного урона."
    )

    enemy_attack = Skill(
        renpy,
        name="Enemy Attack",
        img="images/skills/enemy_attack.png",
        damage_min=3,
        damage_max=7,
        description="Вражеский скилл."
    )
