class Skill:
    def __init__(self, renpy, name, img, damage_min, damage_max, description="No description"):
        self.renpy = renpy
        self.name = name
        self.img = img
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.description = description
        self.difficulty = 0

    def apply(self, target):
        damage = self.renpy.random.randint(self.damage_min, self.damage_max)
        target.hp = max(target.hp - damage, 0)
        print(f"Applied {self.name} to {target.name}. Damage dealt: {damage}. {target.name} HP: {target.hp}")
        return damage