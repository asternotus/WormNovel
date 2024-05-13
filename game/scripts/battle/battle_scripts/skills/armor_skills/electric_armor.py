import random
from game.scripts.battle.battle_scripts.skills.armor_skills.armor_skill import ArmorSkill

class ElectricArmor(ArmorSkill):
    def __init__(self, cost, description=None, icon_path=None):
        super().__init__("Электрическая броня", cost, description, icon_path)

        self.description = description
        self.icon_path = icon_path

        self.success_texts = [
            "Я обрамляю электричество вокруг себя в подобие защитного поля.",
            "Электричество собирается вокруг меня, создавая искрящийся щит.",
            "Я обволакиваю себя плотным слоем электрических волн, чтобы защититься от атак противника."
        ]

    def get_effect(self):
        return self.effect

    def get_heal(self):
        return random.randint(2, 5)
    
    def get_success_sound(self):
        return "audio/battle/skills/ice.ogg"

    def get_failure_sound(self):
        return "audio/battle/skills/ice.ogg"

    def get_success_text(self):
        return random.choice(self.success_texts)