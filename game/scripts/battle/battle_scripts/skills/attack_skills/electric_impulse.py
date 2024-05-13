import random
from game.scripts.battle.battle_scripts.skills.attack_skills.attack_skill import AttackSkill

class ElectricImpulse(AttackSkill):
    def __init__(self, cost, description=None, icon_path=None):
        super().__init__("Электрический импульс", cost, description, icon_path)

        self.description = description
        self.icon_path = icon_path

        self.success_texts = [
            "Сосредотачивая статический заряд в кончиках пальцев, я сформировала импульс и выпустила его в противника.",
            "Электрический импульс осветил местность синеватым светом, поражая моего противника точно в цель.",
            "Я выпустила серию быстрых электрических импульсов, которые устремились к противнику."
        ]

    def get_effect(self):
        return self.effect

    def get_damage(self):
        return random.randint(1, 3)
    
    def get_success_sound(self):
        return "audio/battle/skills/thunder.ogg"

    def get_failure_sound(self):
        return "audio/battle/skills/thunder.ogg"

    def get_success_text(self):
        return random.choice(self.success_texts)
