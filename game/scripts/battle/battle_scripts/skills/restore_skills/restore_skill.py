from game.scripts.battle.battle_scripts.skills.skill import Skill

class RestoreSkill(Skill):
    def __init__(self, name, cost, restor_value=None, sound=None, restore_text=None, description=None, icon_path=None):
        super().__init__(name, cost)
        self.restor_value = restor_value
        self.sound = sound
        self.restore_text = restore_text
        self.effect = None
        self.description = description
        self.icon_path = icon_path