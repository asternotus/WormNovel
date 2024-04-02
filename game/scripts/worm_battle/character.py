class Character:
    def __init__(self, name, hp, max_hp, mp, image):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.mp = mp
        self.image = image
        self.skills = []
        self.weakness = []
        self.skill_slots_count = 3
        