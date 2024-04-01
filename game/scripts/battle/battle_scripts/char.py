import renpy

class Char(object):
    # Конструктор класса Char.
    def __init__(self, name, img="player", atk=5, dfn=0, lvl=1, exp=0, hpmax=60, mpmax=100, 
                    skills=None, p_skills=None, equip=None, condition=None, 
                    turn=False, defending=False, dead=False, bonus_atk=0, bonus_dfn=0, 
                    img_pos=0, bar_pos=0, dmg_pos=0):
        # Инициализация атрибутов персонажа.
        self.name = name  # имя персонажа
        self.img = img  # изображение персонажа
        self.atk = atk  # атака
        self.dfn = dfn  # защита
        self.lvl = lvl  # уровень
        self.exp = exp  # опыт
        self.hpmax = hpmax  # максимальное здоровье
        self._hp = hpmax  # текущее здоровье
        self.mpmax = mpmax  # максимальная мана
        self._mp = mpmax  # текущая мана
        self.skills = [] if skills is None else skills  # навыки
        self.p_skills = [] if p_skills is None else p_skills  # пассивные навыки
        self.equip = {'hand': None, 'head': None, 'chest': None, 'accs': None} if equip is None else equip  # экипировка
        self.condition = {'burn': False, 'freeze': False, 'paral': False, 'poison': False, 
                            'sleep': False, 'stun': False, 'confus': False, 'wound': False, 
                            'rage': False} if condition is None else condition  # состояния персонажа
        self.turn = turn  # флаг хода
        self.defending = defending  # флаг защиты
        self.dead = dead  # флаг смерти
        self.bonus_atk = bonus_atk  # бонусная атака
        self.bonus_dfn = bonus_dfn  # бонусная защита
        self.img_pos = img_pos  # позиция изображения
        self.bar_pos = bar_pos  # позиция полоски
        self.dmg_pos = dmg_pos  # позиция урона
        self.actions_count = 1  # количество действий

    # Свойство для здоровья.
    @property
    def hp(self):
        # Проверка и возврат текущего здоровья в допустимом диапазоне.
        return max(0, min(self.hpmax, self._hp))

    @hp.setter
    def hp(self, value):
        # Установка здоровья с учетом максимального значения.
        self._hp = value

    # Свойство для маны.
    @property
    def mp(self):
        # Проверка и возврат текущей маны в допустимом диапазоне.
        return max(0, min(self.mpmax, self._mp))

    @mp.setter
    def mp(self, value):
        # Установка маны с учетом максимального значения.
        self._mp = value

    # Метод для добавления экипировки.
    def addEquip(self, slot, item):
        # Добавление предмета в указанный слот.
        old_item = self.equip.get(slot)
        self.equip[slot] = item
        if old_item is None:
            renpy.say(None, f"You equipped {item}.")  # "Вы экипировали {item}."
        else:
            renpy.say(None, f"Replacing {old_item} for {item}.")  # "Замена {old_item} на {item}."

    # Метод для удаления экипировки.
    def removeEquip(self, slot):
        # Удаление предмета из указанного слота.
        if slot in self.equip and self.equip[slot] is not None:
            renpy.say(None, f"Removed {self.equip[slot]}.")  # "Удалено {self.equip[slot]}."
            self.equip[slot] = None