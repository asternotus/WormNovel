from game.scripts.battle.battle_scripts.skills.skill import Skill

class HealSkill(Skill):
    def __init__(self, name, cost, amount, sound, heal_text, description=None, icon_path=None):
        super().__init__(name, cost)
        self.amount = amount
        self.sound = sound
        self.heal_text = heal_text
        self.effect = None
        self.description = description
        self.icon_path = icon_path