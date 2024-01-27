init python:
    def monsterTurns():
        global use_skill
        for m in game_state.battle_monsters:
            game_state.hit_t = []
            game_state.missed_t = []
            game_state.skill_affected_targets = []
            use_skill = False
            if not m.dead:
                game_state.message = "none"
                if not game_state.battle_end:
                    monsterTarg(m)
                    renpy.play(game_state.sfx_whoosh)
                    renpy.pause(0.3, hard=True)
                    renpy.play(game_state.atk_sfx)
                    game_state.msg_mons = m.name
                    if use_skill:
                        game_state.msg_skill = game_state.b_skill.name
                        game_state.message = "m_skill"
                    else:
                        game_state.message = "m_atk"
                    for t in game_state.picked_targs:
                        monsterAtk(m, t)

                    m.state = None
                    renpy.show_screen("player_dmg")
                    renpy.pause(0.2, hard=True)
                    renpy.pause(1.0)
                    renpy.hide_screen("player_dmg")
                    battle_manager.playersChk()

    def monsterTarg(m):
        global use_skill
        global roll_target
        bf.alive_players_count()
        targs = 1
        game_state.picked_targs = []
        game_state.atk_sfx = "audio/battle/monsters/" + m.sfx_atk + ".ogg"
        if m.skills:
            use_skill = renpy.random.choice([True, False])
            if use_skill:
                game_state.b_skill = renpy.random.choice(m.skills)
                game_state.b_skill.useSkill()
                if game_state.b_skill.targ == "all":
                    game_state.picked_targs = game_state.alive_players
                    return
                else:
                    targs = game_state.b_skill.targs
        while targs > 0:
            roll_target = renpy.random.choice(game_state.alive_players)
            game_state.picked_targs.append(roll_target)
            targs -= 1

    def monsterAtk(m, p):
        m.state = "attacking"
        monsterDmg(m, p)
        if bf.accept_formula(m, p):
            if skill_manager.skillChk(p, radar):
                game_state.hit_t.append(p)
                p._hp -= m_damage
                roll_shake = renpy.random.randint(1,2)
                if roll_shake == 1:
                    renpy.with_statement(hpunch)
                if roll_shake == 2:
                    renpy.with_statement(vpunch)

    def monsterDmg(m, p):
        global roll_target
        global m_damage
        global currdmg
        global use_skill
        turnbonus = 0
        if use_skill:
            currdmg = game_state.damage
        else:
            currdmg = int(m.atk*1.1 - (m.atk * renpy.random.randint(1,20) / 100))
        if p.defending == True:
            turnbonus += 1*p.lvl
            renpy.play("audio/battle/skills/block.ogg")
        m_damage = int(currdmg*currdmg/(currdmg+p.dfn+p.bonus_dfn+turnbonus))

    def monsterImg(m):
        if m.state == "attacking":
            return im.MatrixColor(battle_manager.getImage(m), im.matrix.tint(1,.5,.5))
        if m.state == "hit":
            return im.MatrixColor(battle_manager.getImage(m), im.matrix.tint(1,.5,.5))
        if m.state == "heal": # green
            return im.MatrixColor(battle_manager.getImage(m), im.matrix.tint(.5,1,.5))
        if m.state == "dying":
            return im.MatrixColor(battle_manager.getImage(m), im.matrix.invert())
        if m.state == "other": # blue
            return im.MatrixColor(battle_manager.getImage(m), im.matrix.tint(.5,.5,1))
        if m.state == "other2": # hue
            return im.MatrixColor(battle_manager.getImage(m), im.matrix.hue(90))
        else:
            return battle_manager.getImage(m)
