class Fighter:
    def __init__(self, name, hp, max_hp, mp, max_mp, skills=[], image="", avatar=""):
        self.name = name
        self.max_hp = max_hp
        self.max_mp = max_mp
        self.hp = hp
        self.mp = mp
        self.skills = skills or []
        self.effects = []
        self.image = image
        self.avatar = avatar

    def add_skill(self, skill):
        self.skills.append(skill)

    def take_damage(self, amount):
        """Уменьшает количество здоровья, но не ниже нуля."""
        self.hp = max(self.hp - amount, 0)

    def heal(self, amount):
        """Увеличивает количество здоровья, но не выше максимального."""
        self.hp = min(self.hp + amount, self.max_hp)

    def use_mp(self, amount):
        """Уменьшает количество магических очков, если достаточно, возвращает True."""
        if self.mp >= amount:
            self.mp -= amount
            return True
        else:
            self.mp = 0
            return False

    def restore_mp(self, amount):
        """Восстанавливает магические очки, но не выше максимального."""
        self.mp = min(self.mp + amount, self.max_mp)

    def update_effects(self):
        # Сначала собираем эффекты, которые нужно удалить
        to_remove = []
        for effect in self.effects:
            effect.duration -= 1
            if effect.duration <= 0:
                to_remove.append(effect)

        # Теперь безопасно удаляем эти эффекты
        for effect in to_remove:
            self.effects.remove(effect)

