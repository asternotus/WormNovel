import random
from game.scripts.battle.battle_scripts.skills.attack_skills.attack_skill import AttackSkill
from game.scripts.battle.battle_scripts.effects.stun_effect import StunEffect

class ElectricShock(AttackSkill):
    def __init__(self, cost, description=None, icon_path=None):
        super().__init__("Шок", cost, description, icon_path)

        self.description = description
        self.icon_path = icon_path

        self.success_texts = [
            "Молния оттолкнула противника, позволяя сократить расстояние между нами.",
            "Мощный поток электрической энергии не давал противнику ко мне прблизиться.",
            "Раздался оглушительный звук молниеносной атаки, которая повалила противника на землю."
        ]
    
    def get_effect(self):
        return self.effect

    def get_damage(self):
        self.effect = None
        if random.random() < 1.5:
            self.effect = StunEffect()
        return random.randint(1, 3)

    def get_success_sound(self):
        return "audio/battle/skills/thunder.ogg"

    def get_failure_sound(self):
        return "audio/battle/skills/thunder.ogg"

    def get_success_text(self):
        return random.choice(self.success_texts)