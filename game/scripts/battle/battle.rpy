init python:
    def playerAction(player):
        if not game_state.battle_end and not player.turn:
            if game_state.renpy.get_screen("turn_select"):
                return Return(player)
            else:
                return NullAction()
        else:
            return NullAction()

    def runEvent():
        global eventrunning
        eventrunning = True
        config.allow_skipping = True
        config.rollback_enabled = True
        game_state.renpy.choice_for_skipping()
        game_state.renpy.hide_screen("tooltip")
        game_state.renpy.retain_after_load()

    def stopEvent():
        global eventrunning
        eventrunning = False
        config.allow_skipping = False
        config.rollback_enabled = False
        game_state.renpy.block_rollback()
        game_state.renpy.choice_for_skipping()
        preferences.afm_enable = False

$ after_battle_level = "act_first_review"

label battle:
    $ stopEvent()

    $ game_state.monster_slot = game_state.battle_monsters
    $ renpy.random.shuffle(game_state.monster_slot)
    $ battle_manager.asignPos()

    $ game_state.row1btn = False
    $ game_state.row2btn = False
    $ game_state.missed_t = []
    $ game_state.win = False
    $ game_state.battle_end = False
    $ game_state.monsters_dead = 0
    $ game_state.current_player = None
    show screen battle_tooltip

    random:
        scene bb1
        scene bb2
        scene bb3
    with pixellate

    call player_select from _call_player_select
    show screen display_monsters with diss
    show screen battle_message
    show screen battle_overlay with diss
    jump battling

label player_select:
    $ spark.img_pos = 512
    $ spark.bar_pos = 944
    $ spark.dmg_pos = 1136
    # call screen select_p1

    return

screen select_p1():
    style_prefix "confirm"
    frame:
        yalign 0.2
        has vbox:
            label "Выбери игрока №1"
            for c in game_state.party_list:
                if c != spark:
                    textbutton "[c.name]" xalign 0.5 action Return(c)
            textbutton "Пропустить" xalign 0.5 action Return("none")

screen battle_tooltip():
    zorder 20
    $ tooltip = GetTooltip()
    if tooltip:
        timer 1 action SetVariable("tt_timer", True)
        if tt_timer:
            add MouseTooltip()
            $ mouse_pos = renpy.get_mouse_pos()
            $ renpy.set_mouse_pos(mouse_pos[0], mouse_pos[1])
    else:
        timer 0.001 action SetVariable("tt_timer", False)

screen battle_overlay():
    fixed:
        xoffset 192
        for p in game_state.battle_players:
            if game_state.current_player == p:
                add p.img + "_battle" yalign 1.05 xpos p.img_pos at char_sway
            else:
                imagebutton:
                    focus_mask True
                    yalign 1.1 xpos p.img_pos
                    idle p.img + "_battle"
                    tooltip "{0}\nATK: {1}\nDFN: {2}\n{3}".format(p.name, p.atk, p.dfn, p.p_skills[0].name)
                    action  Function(playerAction(p))
            fixed:
                pos p.bar_pos, 896
                vbox:
                    if game_state.current_player == p:
                        text "[p.name!u]" anchor (1.0,1.0) xoffset 110 style_group "battle_playername" color "#ffcc66"
                    else:
                        text "[p.name!u]" anchor (1.0,1.0) xoffset 110 style_group "battle_playername"
                    text "LVL.[p.lvl] " anchor (1.0,1.0) yoffset -12 xoffset 120 style_group "battle_playerlvl"
                    fixed:
                        yoffset -24
                        bar style "bar_hp" value AnimatedValue(value=p.hp, range=p.hpmax, delay=0.25) xanchor .5
                        bar style "bar_mp" value AnimatedValue(value=p.mp, range=p.mpmax, delay=0.25) xanchor .5 yalign 0.05
                        text "[p.hp]/[p.hpmax]" xanchor .5 yalign 0.0075
                        text "[p.mp]/[p.mpmax]" xanchor .5 yalign 0.0575

screen display_monsters():
    fixed:
        pos (576, 600)
        for m in game_state.monster_slot:
            fixed:
                xpos m.sprite_pos
                if not m.dead:
                    imagebutton at m.anim:
                        hover im.MatrixColor(battle_manager.getImage(m), im.matrix.brightness(0.1))
                        action Return(m), SensitiveIf(skill_manager.canTarget(m))
                        idle monsterImg(m) anchor (0.5,1.0)
                        if renpy.get_screen("select_monster"):
                            insensitive im.MatrixColor(battle_manager.getImage(m), im.matrix.saturation(0.1))
                        tooltip "{0} HP: {1}".format(m.name, m.hp)
                    bar style "bar_mhp" value AnimatedValue(value=m.hp, range=m.hpmax, delay=0.25) anchor (0.5,1.0)
                    text "[m.hp]" xanchor 0.5

screen battle_message():
    add "images/battle/messagebox.png"
    hbox:
        xpos 110 yalign 0.07
        if game_state.message == "attack":
            text "Кто атакует?"
        elif game_state.message == "skill":
            text "Ходит {0}".format(game_state.current_player.name)
        elif game_state.message == "item":
            text "Выбрать предмет"
        elif game_state.message == "other_skill":
            text "{0} использует [game_state.msg_skill]!".format(game_state.current_player.name)
        elif game_state.message == "attack_skill":
            text "{0} атакует [game_state.msg_mons]!".format(game_state.current_player.name)
        elif game_state.message == "defend":
            text "{0} защищается!".format(game_state.current_player.name)
        elif game_state.message == "m_skill":
            text "[game_state.msg_mons] атакует с помощью [game_state.msg_skill]!"
        elif game_state.message == "m_atk":
            text "[game_state.msg_mons] атакует {0}!".format(roll_target.name)
        elif game_state.message == "target_who":
            text "Кто цель?"
        elif game_state.message == "m_dead":
            text "[game_state.msg_mons] выбывает!"
        elif game_state.message == "player_ko":
            text "[game_state.koplayer] вне боя!"
        elif game_state.message == "you_win":
            text "Победа!"
        elif game_state.message == "lost":
            text "Поражение..."
        elif game_state.message == "use_on_who":
            text "Кто цель способности?"
        elif game_state.message == "none":
            text ""

label battling:
    $ inCombat = True
    while inCombat:
        if game_state.battle_end == True:
            $ inCombat = False
            jump end_battle
        $ battle_manager.startPlayersTurn()
        $ game_state.message = "attack"
        call turn_actions from _call_turn_actions
        $ game_state.message = "none"
        $ monsterTurns()

label end_battle:
    hide screen battle_overlay
    with dissolve
    if game_state.win:
        stop music
        play sound fanfare
        me "Победа!"
        stop sound
        $ bf.exp_formula()
        call expression after_battle_level from _call_expression
    else:
        $ game_state.message = "lost"
        "Поражение."
        jump start
    hide screen battle_message
    hide screen display_monsters
    $ battle_manager.partyRevive()
    return

