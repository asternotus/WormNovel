from game.scripts.battle.battle_scripts.skills.skill import Skill

class ArmorSkill(Skill):
    def __init__(self, name, cost, armor_boost=None, sound=None, armor_text=None, description=None, icon_path=None):
        super().__init__(name, cost)
        self.armor_boost = armor_boost
        self.sound = sound
        self.armor_text = armor_text
        self.effect = None
        self.description = description
        self.icon_path = icon_path