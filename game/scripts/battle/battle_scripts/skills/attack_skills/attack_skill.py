from game.scripts.battle.battle_scripts.skills.skill import Skill

class AttackSkill(Skill):
    def __init__(self, name, cost, damage=None, sound=None, hit_texts=None, miss_texts=None, description=None, icon_path=None):
        super().__init__(name, cost)
        self.damage = damage
        self.sound = sound
        self.hit_texts = hit_texts
        self.miss_texts = miss_texts
        self.effect = None
        self.description = description
        self.icon_path = icon_path