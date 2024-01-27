init python:
    import copy
    from game.scripts.battle.battle_scripts.char import Char
    from game.scripts.battle.battle_scripts.enemy import Enemy
    from game.scripts.battle.battle_scripts.game_state import GameState
    from game.scripts.battle.battle_scripts.skills import SkillManager
    from game.scripts.battle.battle_scripts.skills import Skill, ActiveSkill, PassiveSkill
    from game.scripts.battle.battle_scripts.battle_formulas import BattleFormulas
    from game.scripts.battle.battle_scripts.battle_manager import BattleManager

    if not renpy.variant("touch"):
        config.mouse = {"default":[ ("images/cursor.png", 1, 1) ] }
    
    game_state = GameState(renpy)
    skill_manager = SkillManager(game_state)
    bf = BattleFormulas(game_state, skill_manager)
    battle_manager = BattleManager(game_state, bf)

    # ACTIVE SKILLS (name, pwr, mp_cost, sfx, targ, targs, type='active', trans=None, img=None, back_row=False)
    doubleattack = ActiveSkill(game_state, "Двойная атака", 25, 5, "sword", "enemy", 2, back_row=True) # two enemy targets
    attackall = ActiveSkill(game_state, "Атака по области", 75, 45, "rock", "all") # targets all enemies
    magicheal = ActiveSkill(game_state, "Лечение", -50, 25, "heal", "self") # negative pwr to heal
    defenseup = ActiveSkill(game_state, "Защита", 0, 25, "defend", "self") # use is in skill_effects
    magicswap = ActiveSkill(game_state, "Подмена", 0, 15, "heal", "enemy", 2, back_row=True) # can target back row
    arrowhail = ActiveSkill(game_state, "Град Стрел", 10, 40, "bow", "all", img="arrowhail", back_row=True)
    mindfreeze = ActiveSkill(game_state, "Заморозка Сознания", 15, 5, "ice", img="mindfreeze", back_row=True)
    iceball = ActiveSkill(game_state, "Ледяной Шар", 30, 5, "ice", "row", img="iceball") # attacks whole row
    asteroid = ActiveSkill(game_state, "Астероид", 20, 5, "rock", img="asteroid")
    swordofdeath = ActiveSkill(game_state, "Клинок Смерти", 30, 10, "sword", img="swordofdeath")
    rockthrow = ActiveSkill(game_state, "Бросок Камня", 30, 40, "rock", "enemy", 2, back_row=True, img="rockthrow")
    spikeshield = ActiveSkill(game_state, "Шипастый Щит", 45, 70, "block", "all", img="spikeshield")
    circleofhealing = ActiveSkill(game_state, "Круг Лечения", -30, 10, "heal", "ally", img="circleofhealing")
    mindburn = ActiveSkill(game_state, "Поджёг Крови", 35, 15, "fire", img="mindburn")
    mindblast = ActiveSkill(game_state, "Громовой Удар", 20, 5, "thunder", img="mindblast")
    souldrain = ActiveSkill(game_state, "Поглощение Души", 80, 60, "acid", img="souldrain")
    lavaburst = ActiveSkill(game_state, "Взрыв Лавы", 20, 5, "fire", img="lavaburst")
    deathmissile = ActiveSkill(game_state, "Смертельная Ракета", 70, 45, "rock", img="deathmissile")
    meteorshower = ActiveSkill(game_state, "Метеоритный Дождь", 80, 40, "rock", "all", img="meteorshower")
    hellrage = ActiveSkill(game_state, "Адская Ярость", 120, 80, "fire", "all", img="hellrage")
    lifedrain = ActiveSkill(game_state, "Поглощение Жизни", 80, 15, "acid", img="lifedrain")
    devastationbeam = ActiveSkill(game_state, "Опустошительный Луч", 30, 5, "fire", "all", img="devastationbeam")
    energybeams = ActiveSkill(game_state, "Энергетический Луч", 70, 40, "thunder", "all", img="energybeams")
    giftofangels = ActiveSkill(game_state, "Подарок от Ангелов", -35, 10, "heal", "ally", 2, img="giftofangels")
    charging_shield = ActiveSkill(game_state, "Зарядный Щит", 0, 10, "defend", "self", img="mindblast")
    recharging = ActiveSkill(game_state, "Заряд", 0, 0, "res_restore", "self", img="energybeams")

    # PASSIVE SKILLS (name, sfx=None, img=None, trans=None, lvl=0)
    radar = PassiveSkill(game_state, "Радар", "heal")
    passive1 = PassiveSkill(game_state, "Пассивный навык №1", "heal")
    passive2 = PassiveSkill(game_state, "Пассивный навык №2", "heal")

    # SPARK SKILLS
    weapon_attack = ActiveSkill(game_state, "Атака оружием", 30, 0, "thunder", "enemy", img="weapon_attack")
    electric_pulse = ActiveSkill(game_state, "Электрический Импульс", 30, 0, "thunder", "enemy", img="electric_pulse")
    thunderbolt = ActiveSkill(game_state, "Цепная Молния", 30, 0, "thunder", "enemy", 3, img="thunderbolt", back_row=True)
    overload = ActiveSkill(game_state, "Перегрузка", 30, 0, "thunder", "enemy", img="overload")
    
    charge = ActiveSkill(game_state, "Зарядка", -30, 10, "heal", "self", 2, img="charge")
    charge_weapon = ActiveSkill(game_state, "Зарядить оружие", 0, 0, "defend", "self", img="charge_weapon")
    blackout = ActiveSkill(game_state, "Обесточить", 0, 0, "thunder", "enemy", img="blackout")
    



# ПЕРСОНАЖИ
define character.spark = Character("Искра", image="player")
default spark = Char("Искра", img="player", skills=[weapon_attack, electric_pulse, thunderbolt, overload, charge, charge_weapon, blackout], p_skills=[passive1], equip={'hand': "Bow", 'head': None, 'chest': None, 'accs': None})

define character.knight = Character("Рыцарь", image="yu")
default knight = Char("Рыцарь", lvl=3, hpmax=102, img="yu", skills=[lavaburst, deathmissile, meteorshower, hellrage], p_skills=[radar], equip={'hand': None, 'head': None, 'chest': None, 'accs': None})

default name = "Искра"
default eventrunning = False
default _game_menu_screen = "preferences"

# НАСТРОЙКА БИТВЫ
label load_setup:
    if not name:
        $ name = "Искра"
    $ spark.name = name
    #$ magicheal.addSkill(a) # add new skills
    $ defenseup.addSkill(knight)
    $ magicswap.addSkill(knight)
    call load_enemies from _call_load_enemies
    $ game_state.party_list = [spark,knight] # initial party list, including main character
    $ fixedset = "set 1"
    $ wild_monsters = [mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11]
    $ battle_manager.restorehp()
    $ battle_manager.restoremp()
    return

# МОНСТРЫ
label load_enemies:
    $ empty = Enemy(None, None, None, None, None, None, None, None, dead=True)
    $ mon1 = Enemy("Lapras", 40, 15, 1.0, 50, 3, "1", "water", anim=slow_sway, skills=[arrowhail])
    $ mon2 = Enemy("Ditto", 50, 20, 6.0, 50, 4, "2", "pound", anim=squeeze, skills=[mindfreeze])
    $ mon3 = Enemy("Eevee", 30, 40, 3.0, 50, 5, "3", "tackle", anim=idle_shake, skills=[lifedrain])
    $ mon4 = Enemy("Vaporeon", 25, 10, 10.0, 50, 4, "4", "water", anim=idle_y, skills=[devastationbeam])
    $ mon5 = Enemy("Jolteon", 45, 35, 10.0, 50, 4, "5", "thunder", anim=idle_xy, skills=[asteroid])
    $ mon6 = Enemy("Flareon", 70, 50, 9.0, 50, 8, "6", "fire", anim=idle_x, skills=[swordofdeath])
    $ mon7 = Enemy("Espeon", 15, 50, 7.0, 50, 5, "7", "cut", anim=idle_shake, skills=[rockthrow])
    $ mon8 = Enemy("Umbreon", 55, 25, 2.0, 50, 4, "8", "scratch", anim=idle_shake, skills=[mindburn])
    $ mon9 = Enemy("Venasaur", 60, 40, 3.0, 50, 6, "9", "leaf", anim=idle_xy, skills=[lavaburst])
    $ mon10 = Enemy("Charizard", 90, 95, 4.0, 50, 8, "10", "fire", anim=idle_shake, skills=[deathmissile])
    $ mon11 = Enemy("Blastoise", 85, 85, 5.0, 50, 5, "11", "water", anim=idle_x, skills=[thunderbolt])
    return

# ОБРАБОТКА НАВЫКОВ
label skill_effects:
    if game_state.b_skill == defenseup:
        $ game_state.current_player.bonus_dfn += 5
    elif game_state.b_skill == magicswap:
        $ game_state.skill_text = "SWaP!"
        $ game_state.skill_targets.append(game_state.picked_targets[0])
        $ game_state.skill_targets.append(game_state.picked_targets[1])
        $ battle_manager.swapSlot(game_state.monster_slot.index(game_state.picked_targets[0]), game_state.monster_slot.index(game_state.picked_targets[1]))
    return
