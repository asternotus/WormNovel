from game.scripts.battle.battle_scripts.enemy import Enemy
from game.scripts.battle.battle_scripts.skills import Skill

class BattleManager:
    def __init__(self, game_state, bf):
        self.game_state = game_state
        self.bf = bf

    def prepareBattle(self, enemies=None, fixedset=None):
        self.game_state.battle_monsters = [enemy for enemy in enemies]
        self.game_state.monsters_total = len(self.game_state.battle_monsters)

        for battle_enemy in self.game_state.battle_monsters:
            battle_enemy._hp = battle_enemy.hpmax
            battle_enemy.dead = False

            self.assignMonsterPositions(battle_enemy, len(self.game_state.battle_monsters))

    def assignMonsterPositions(self, enemy, index):
        positions = [(0, 580, 380), (256, 866, 380), (512, 1122, 380), (768, 1378, 380), (1024, 1634, 380), (1280, 1890, 380)]
        if index < len(positions):
            pos, dmg_x, dmg_y = positions[index]
            enemy.sprite_pos = pos
            enemy.dmg_pos = (dmg_x, dmg_y)

    def asignPos(self):
        if len(self.game_state.battle_monsters) > 0:
            self.game_state.battle_monsters[0].sprite_pos = 0
            self.game_state.battle_monsters[0].dmg_pos = (580, 380)
        if len(self.game_state.battle_monsters) > 1:
            self.game_state.battle_monsters[1].sprite_pos = 256
            self.game_state.battle_monsters[1].dmg_pos = (866, 380)
        if len(self.game_state.battle_monsters) > 2:
            self.game_state.battle_monsters[2].sprite_pos = 512
            self.game_state.battle_monsters[2].dmg_pos = (1122, 380)
        if len(self.game_state.battle_monsters) > 3:
            self.game_state.battle_monsters[3].sprite_pos = 768
            self.game_state.battle_monsters[3].dmg_pos = (1378, 380)
        if len(self.game_state.battle_monsters) > 4:
            self.game_state.battle_monsters[4].sprite_pos = 1024
            self.game_state.battle_monsters[4].dmg_pos = (1634, 380)
        if len(self.game_state.battle_monsters) > 5:
            self.game_state.battle_monsters[5].sprite_pos = 1280
            self.game_state.battle_monsters[5].dmg_pos = (1890, 380)

    def swapSlot(self, old_slot, new_slot):
        self.renpy.hide_screen("display_monsters")
        self.game_state.monster_slot[old_slot], self.game_state.monster_slot[new_slot] = self.game_state.monster_slot[new_slot], self.game_state.monster_slot[old_slot]
        self.asignPos()
        self.renpy.show_screen("display_monsters")

    def partyRevive(self):
        for c in self.game_state.party_list:
            c.bonus_dfn = 0
            if c.dead == True:
                c.dead = False
                c._hp = 1

    def restorehp(self):
        for c in self.game_state.party_list:
            c._hp = c.hpmax

    def restoremp(self):
        for c in self.game_state.party_list:
            c._mp = c.mpmax

    def startPlayersTurn(self):
        for p in self.game_state.battle_players:
            p.actions_count = 2
            p.turn = False
            p.defending = False

    def endTurn(self, hpunch, vpunch):
        self.game_state.message = "other_skill"
        self.game_state.misstext = self.game_state.renpy.random.choice(self.game_state.misstext_list)
        if isinstance(self.game_state.b_skill, Skill):
            self.game_state.b_skill.useSkill()
            if self.game_state.b_skill.sfx == "defend":
                self.bf.defend(vpunch)
            elif self.game_state.b_skill.sfx == "res_restore":
                self.bf.resource_restore(vpunch)
        elif isinstance(self.game_state.b_skill, "Item"):
            self.use_item()
        if self.game_state.target == "all":
            self.bf.attack_all()
        if self.game_state.target == "enemy" or self.game_state.target == "row":
            self.bf.attack_enemy()
        if self.game_state.target == "ally":
            self.bf.attack_ally()
        if self.game_state.target == "self":
            self.bf.attack_self()
        if self.game_state.target == "ko":
            self.bf.attack_ally()
        if self.game_state.target == "attack":
            self.bf.attack(hpunch)
        if self.game_state.target == "defend":
            self.game_state.message = "defend"
            self.bf.defend(vpunch)
        self.game_state.current_player.turn = False
        self.game_state.current_player.actions_count -= 1
        self.game_state.current_player._mp -= self.game_state.mp_lost
        self.game_state.current_player._hp -= self.game_state.hp_lost
        self.game_state.renpy.pause(1.5, hard=True)
        self.bf.alive_players_count()
        self.game_state.renpy.hide_screen("monster_dmg")
        self.playersChk()

    def startTurn(self):
        self.game_state.row1btn = False
        self.game_state.row2btn = False
        self.game_state.target = "enemy"
        self.game_state.message = "skill"
        self.game_state.damage = 0
        self.game_state.mpdmg = 0
        self.game_state.mp_lost = 0
        self.game_state.hp_lost = 0
        self.game_state.atk_sfx = None
        self.game_state.dropitem = None
        self.game_state.picked_targs = []
        self.game_state.hit_t = []
        self.game_state.missed_t = []
        self.game_state.skill_affected_targets = []

    def playersChk(self):
        for player in self.game_state.battle_players:
            if player.hp == 0 and not player.dead:
                self.game_state.renpy.pause(0.5)
                player.dead = True
                self.game_state.koplayer = player.name
                self.game_state.message = "player_ko"
                self.game_state.renpy.pause(0.7)
        for enemy in self.game_state.battle_monsters:
            if enemy.hp <= 0 and not enemy.dead:
                enemy.state = "dying"
                self.game_state.msg_mons = enemy.name
                self.game_state.message = "m_dead"
                self.game_state.renpy.play(self.game_state.sfx_monsterdead)
                self.game_state.renpy.pause(1)
                self.game_state.message = "none"
                self.game_state.monsters_dead += 1
                enemy.dead = True
        if all(p.hp == 0 for p in self.game_state.battle_players):
            self.game_state.battle_end = True
        if self.game_state.monsters_dead == self.game_state.monsters_total:
            self.game_state.message = "you_win"
            self.game_state.win = True
            self.game_state.battle_end = True

    def getImage(self, i):
        if isinstance(i, Enemy):
            return "images/monsters/"+ i.img+".png"
        if isinstance(i, Skill):
            return "images/skills/" + i.img + ".png"

    def use_item(self):
        pass