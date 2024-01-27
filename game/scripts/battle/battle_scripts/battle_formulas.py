class BattleFormulas:
    def __init__(self, game_state, skill_manager):
        self.game_state = game_state
        self.skill_manager = skill_manager

    def attack_all(self):
        self.game_state.renpy.play(self.game_state.atk_sfx)
        self.game_state.renpy.pause(0.2, hard=True)
        
        for enemy in self.game_state.battle_monsters:
            if not enemy.dead:
                if self.accept_formula(self.game_state.current_player, enemy):
                    self.dmg_formula(enemy)
                    enemy._hp -= enemy.finaldmg
                    enemy._mp -= self.game_state.mpdmg
        self.game_state.renpy.show_screen("monster_dmg")
        self.game_state.renpy.with_statement(self.game_state.s_trans)

    def attack_row(self):
        self.game_state.renpy.play(self.game_state.atk_sfx)
        self.game_state.renpy.pause(0.2, hard=True)
        
        for self.game_state.target in self.game_state.picked_targs:
            if self.accept_formula(self.game_state.current_player, self.game_state.target):
                self.dmg_formula(self.game_state.target)
                self.game_state.target._hp -= self.game_state.target.finaldmg
                self.game_state.target._mp -= self.game_state.mpdmg
                self.game_state.renpy.show_screen("monster_dmg")
                self.game_state.renpy.with_statement(self.game_state.s_trans)

    def attack_enemy(self):
        for self.game_state.target in self.game_state.picked_targs:
            self.game_state.renpy.play(self.game_state.atk_sfx)
            self.game_state.renpy.pause(0.2, hard=True)
            if self.accept_formula(self.game_state.current_player, self.game_state.target):
                self.dmg_formula(self.game_state.target)
                self.game_state.target._hp -= self.game_state.target.finaldmg
                self.game_state.target._mp -= self.game_state.mpdmg
                self.game_state.renpy.show_screen("monster_dmg")
                self.game_state.renpy.with_statement(self.game_state.s_trans)
                self.skill_manager.afterFX(self.game_state.target)

    def attack_ally(self):
        for self.game_state.target in self.game_state.picked_targs:
            self.game_state.renpy.play(self.game_state.atk_sfx)
            self.game_state.renpy.pause(0.2, hard=True)
            self.game_state.target._hp -= self.game_state.damage
            self.game_state.target._mp -= self.game_state.mpdmg
            self.game_state.renpy.with_statement(self.game_state.s_trans)

    def attack_self(self):
        self.game_state.renpy.play(self.game_state.atk_sfx)
        self.game_state.renpy.pause(0.2, hard=True)
        self.game_state.current_player._hp -= self.game_state.damage
        self.game_state.current_player._mp -= self.game_state.mpdmg
        self.game_state.renpy.with_statement(self.game_state.s_trans)

    def defend(self, vpunch):
        self.game_state.current_player.defending = True
        self.game_state.renpy.play("audio/battle/skills/defend.ogg")
        self.game_state.renpy.with_statement(vpunch)

    def resource_restore(self, vpunch):
        self.game_state.current_player._mp += 10
        self.game_state.renpy.play("audio/battle/skills/defend.ogg")
        self.game_state.renpy.with_statement(vpunch)

    def attack(self, hpunch):
        for self.game_state.target in self.game_state.picked_targs:
            self.game_state.game_state.damage = self.game_state.current_player.atk
            self.game_state.msg_mons = self.game_state.target.name
            self.game_state.message = "attack_skill"
            self.game_state.renpy.play("audio/battle/skills/sword.ogg")
            self.game_state.renpy.pause(0.2, hard=True)
            if self.accept_formula(self.game_state.current_player, self.game_state.target):
                self.game_state.target.state = "hit"
                self.dmg_formula(self.game_state.target)
                self.game_state.target._hp -= self.game_state.target.finaldmg
                self.game_state.target._mp -= self.game_state.mpdmg
                self.game_state.renpy.show_screen("monster_dmg")
                self.game_state.renpy.with_statement(hpunch)
                self.game_state.renpy.pause(0.2)
                self.game_state.target.state = None

    def accept_formula(self, attacker, defender):
        misschance = 0
        if defender.lvl > attacker.lvl:
            misschance = defender.lvl - attacker.lvl
        accuracy = 10 - int(misschance * 0.7)
        self.game_state.miss_roll = self.game_state.renpy.random.randint(1, 10)
        if self.game_state.miss_roll > accuracy:
            self.game_state.missed_t.append(defender)
            self.game_state.renpy.play(self.game_state.sfx_whoosh)
            self.game_state.renpy.show_screen("monster_dmg")
            return False
        else:
            return True

    def dmg_formula(self, target):
        random_factor = self.game_state.renpy.random.randint(1, 20) / 100
        preliminary_damage = int(self.game_state.damage * 1.1 - (self.game_state.damage * random_factor))
        target.finaldmg = int(preliminary_damage * (100 / (100 + target.dfn)))
        self.game_state.hit_t.append(target)

    def exp_formula(self):
        self.game_state.curr_exp = 0
        self.alive_players_count()

        for enemy in self.game_state.battle_monsters:
            if self.game_state.monsters_total > 0:
                self.game_state.curr_exp += enemy.exp
                self.game_state.monsters_total -= 1
        
        self.game_state.curr_exp /= len(self.game_state.battle_players)

        for player in self.game_state.battle_players:
            if player.hp > 0:
                player.exp += self.game_state.curr_exp
                self.game_state.renpy.play("audio/game/exp.ogg")
                self.game_state.renpy.say(None, "%s earned %i experience points!" % (player.name, self.game_state.curr_exp))
                while player.exp >= (player.lvl+1)**3:
                    player.lvl += 1
                    self.game_state.renpy.play("audio/game/lvlup.ogg")
                    self.game_state.renpy.say(None, "%s reached lvl %i!" % (player.name, player.lvl))

    def alive_players_count(self):
        self.game_state.players = 0
        self.game_state.alive_players = []
        for player in self.game_state.battle_players:
            if player.hp > 0:
                player.dead = False
                self.game_state.players += 1
                self.game_state.alive_players.append(player)