label turn_actions:
    while not game_state.battle_end:
        $ bf.alive_players_count()
        $ game_state.current_player = None
        $ game_state.message = "attack"
        call screen turn_select
        $ game_state.current_player = _return
        if game_state.current_player != "done":
            call player_skill from _call_player_skill
            $ battle_manager.endTurn(hpunch, vpunch)
            jump turn_actions
        else:
            $ game_state.current_player = None
            $ game_state.message = None
            return
    return

screen turn_select():
    style_prefix "confirm"
    frame:
        yalign 0.2
        has vbox:
            for p in game_state.battle_players:
                if p.actions_count > 0 and p.hp > 0:
                    textbutton "[p.name]" xalign 0.5 action Return(p)
            textbutton "Завершить Ход" xalign 0.5 action Return("done")

label player_skill:
    $ battle_manager.startTurn()
    call screen choose_skill
    $ game_state.b_skill = _return
    if isinstance(game_state.b_skill, Skill):
        $ game_state.target = game_state.b_skill.targ
        call target_select(game_state.b_skill.targs) from _call_target_select
    if game_state.b_skill == "item":
        $ game_state.message = "item"
        call screen inventory_inbattle(player_inv)
        hide screen inv_tooltip
        $ game_state.b_skill = _return
        $ game_state.target = getTarget(game_state.b_skill)
        call target_select from _call_target_select_1
    elif game_state.b_skill == "attack":
        call target_select from _call_target_select_2
        $ game_state.target = "attack"
    if game_state.b_skill == "defend":
        $ game_state.target = "defend"
    call skill_effects from _call_skill_effects
    return

screen choose_skill():
    key "mouseup_3" action Function(renpy.pop_call), Jump("turn_actions")
    add "images/battle/skillbox.png" pos 8, 214
    vpgrid:
        align (0.06, 0.30)
        cols 4
        rows 2
        spacing 32
        transpose True
        for skll in game_state.current_player.skills:
            if skll.img == None:
                textbutton "[skll.name]" align (.5,.5) action Return(skll), SensitiveIf(skill_manager.sensIf(skll)) tooltip "Damage: {0}\nMP Cost: {1}".format(skll.pwr, skll.mp_cost)
            else:
                imagebutton:
                    align (.5,.5) action Return(skll), SensitiveIf(skill_manager.sensIf(skll))
                    idle battle_manager.getImage(skll)
                    hover im.MatrixColor(battle_manager.getImage(skll), im.matrix.brightness(0.2))
                    insensitive im.MatrixColor(battle_manager.getImage(skll), im.matrix.saturation(0.1))
                    tooltip "{0}\nDamage: {1}\nMP Cost: {2}".format(skll.name, skll.pwr, skll.mp_cost)
        for i in range(0, (8-len(game_state.current_player.skills))):
            imagebutton:
                idle "images/skills/blank.png"
        style_group "skills"
    vbox:
        align (0.35, 0.30)
        # textbutton "Инвентарь" align (.5,.5) action Return("item")
        textbutton "Отмена" align (.5,.5) action Function(renpy.pop_call), Jump("turn_actions")
    timer 300 action Hide('choose_skill'), Function(renpy.pop_call), Jump("turn_actions")

label target_select(targs=1):
    if game_state.target == "enemy":
        $ game_state.message = "target_who"
        while targs > 0 and len(game_state.picked_targs) < (game_state.monsters_total - game_state.monsters_dead):
            call screen select_monster
            $ game_state.picked_targs.append(_return)
            $ targs -= 1
    elif game_state.target == "ally":
        $ game_state.message = "use_on_who"
        while targs > 0 and len(game_state.picked_targs) < len(game_state.alive_players):
            call screen select_ally
            $ game_state.picked_targs.append(_return)
            $ targs -= 1
    elif game_state.target == "ko":
        $ game_state.message = "use_on_who"
        while targs > 0 and len(game_state.picked_targs) < (len(game_state.battle_players)-len(game_state.alive_players)):
            call screen select_ally
            $ game_state.picked_targs.append(_return)
            $ targs -= 1
    if game_state.target == "row":
        $ game_state.message = "target_who"
        call screen select_monster
        if _return in game_state.monster_slot[0:4]:
            python:
                for m in game_state.monster_slot[0:4]:
                    if not m.dead:
                        game_state.picked_targs.append(m)
        elif _return in game_state.monster_slot[4:8]:
            python:
                for m in game_state.monster_slot[4:8]:
                    if not m.dead:
                        game_state.picked_targs.append(m)
    return

screen select_ally():
    key "mouseup_3" action Function(renpy.pop_call), Jump("player_skill"), SensitiveIf(not game_state.picked_targs)
    style_prefix "confirm"
    frame:
        yalign 0.2
        has vbox:
            label "Select player"
            for p in game_state.battle_players:
                if not p in game_state.picked_targs:
                    if game_state.target == "ko":
                        if p.hp == 0:
                            textbutton "[p.name]" xalign 0.5 action Return(p)
                    else:
                        if p.hp > 0:
                            textbutton "[p.name]" xalign 0.5 action Return(p)
            textbutton "Отмена" xalign 0.5 action Function(renpy.pop_call), Jump("player_skill"), SensitiveIf(not game_state.picked_targs)

screen select_monster():
    key "mouseup_3" action Function(renpy.pop_call), Jump("player_skill"), SensitiveIf(not game_state.picked_targs)
    frame:
        yalign 0.2
        has vbox:
            textbutton "Отмена" xalign 0.5 action Function(renpy.pop_call), Jump("player_skill"), SensitiveIf(not game_state.picked_targs)

screen monster_dmg():
    style_group "dmg"
    for m in game_state.monster_slot:
        if m in game_state.missed_t:
            text "[game_state.misstext]" anchor (.5,.5) pos m.dmg_pos at shake_fade
        elif m in game_state.skill_targets:
            text "[game_state.skill_text]" anchor (.5,.5) pos m.dmg_pos at shake_fade
        elif m in game_state.hit_t:
            text "[m.finaldmg]" anchor (.5,.5) pos m.dmg_pos at shake_fade
    timer 1 action Hide('monster_dmg')

screen player_dmg():
    style_group "dmg"
    for p in game_state.battle_players:
        if p in game_state.missed_t:
            text "[game_state.misstext]" anchor (.5,.5) xpos p.dmg_pos ypos 800 at shake_fade
        elif p in game_state.hit_t:
            text "[m_damage]" anchor (.5,.5) xpos p.dmg_pos ypos 800 at shake_fade
        elif p in game_state.skill_targets:
            if game_state.radar_block:
                add "radar" anchor (.5,.5) xpos p.dmg_pos ypos 800 at shake_fade
                text "[game_state.skill_text]" anchor (.5,.5) xpos p.dmg_pos ypos 800 at shake_fade
    timer 1 action Hide('player_dmg')
