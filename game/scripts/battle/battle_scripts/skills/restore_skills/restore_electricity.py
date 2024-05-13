import random
from game.scripts.battle.battle_scripts.skills.restore_skills.restore_skill import RestoreSkill

class RestoreElectricity(RestoreSkill):
    def __init__(self, cost, description=None, icon_path=None):
        super().__init__("Собрать электричество", cost, description, icon_path)

        self.description = description
        self.icon_path = icon_path

        self.success_texts = [
            "Я собрала электричество со всех источников, чтобы быть готовой к атаке.",
            "Я пополнила запас подконтрольного мне электричества, чтобы быть готовой к бою.",
            "Электричество заструилось ко мне из всех приборов, которые находились неподалёку."
        ]

    def get_effect(self):
        return self.effect

    def get_restore(self):
        return random.randint(2, 5)
    
    def get_success_sound(self):
        return "audio/battle/monsters/thunder.ogg"

    def get_failure_sound(self):
        return "audio/battle/monsters/thunder.ogg"

    def get_success_text(self):
        return random.choice(self.success_texts)