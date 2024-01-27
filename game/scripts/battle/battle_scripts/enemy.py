class Enemy(object):
    # Конструктор класса Monster.
    def __init__(self, name, hpmax, atk, dfn, exp, lvl, img, sfx_atk, anim=None, skills=None, state=None, dead=False, finaldmg=0, slot=1, sprite_pos=0, dmg_pos=(0,0), mpmax=100):
        # Инициализация основных атрибутов монстра
        self.name = name  # Имя монстра
        self.hpmax = hpmax  # Максимальное значение здоровья
        self._hp = hpmax  # Текущее значение здоровья
        self.atk = atk  # Атака
        self.dfn = dfn  # Защита
        self.lvl = lvl  # Уровень
        self.exp = exp  # Опыт, получаемый за победу над монстром
        self.dead = dead  # Флаг, показывающий, мертв ли монстр
        self.skills = [] if skills is None else skills  # Список навыков монстра
        self.img = img  # Изображение монстра
        self.sfx_atk = sfx_atk  # Звуковой эффект атаки монстра
        self.finaldmg = finaldmg  # Итоговый урон, наносимый монстром
        self.slot = slot  # Слот, в котором находится монстр
        self.anim = anim  # Анимация монстра
        self.sprite_pos = sprite_pos  # Позиция спрайта монстра
        self.dmg_pos = dmg_pos  # Позиция отображения урона
        self.mpmax = mpmax  # Максимальное значение маны
        self._mp = mpmax  # Текущее значение маны
        self.state = state  # Текущее состояние монстра (например, "атакует", "защищается")

    # Свойство для доступа к здоровью монстра.
    @property
    def hp(self):
        # Возвращает текущее значение здоровья в пределах допустимых границ.
        return max(0, min(self.hpmax, self._hp))

    @hp.setter
    def hp(self, value):
        # Устанавливает значение здоровья, учитывая максимально допустимое значение.
        self._hp = value

    # Свойство для доступа к мане монстра.
    @property
    def mp(self):
        # Возвращает текущее значение маны в пределах допустимых границ.
        return max(0, min(self.mpmax, self._mp))

    @mp.setter
    def mp(self, value):
        # Устанавливает значение маны, учитывая максимально допустимое значение.
        self._mp = value