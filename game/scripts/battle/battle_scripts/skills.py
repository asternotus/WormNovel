class Skill(object):
    # Конструктор основного класса навыков.
    def __init__(self, game_state, name, sfx=None, img=None, trans=None, lvl=0, type='active'):
        self.game_state = game_state # Класс ответственный за основные параметры игры
        self.name = name  # Имя навыка
        self.type = type  # Тип навыка: 'active' или 'passive'
        self.sfx = sfx  # Звуковой эффект навыка
        self.img = img  # Изображение, связанное с навыком
        self.trans = trans  # Анимация навыка
        self.lvl = lvl  # Уровень, на котором навык доступен

    # Метод для добавления навыка персонажу.
    def addSkill(self, char):
        # Добавление активного навыка
        if self.type == "active" and self not in char.skills:
            char.skills.append(self)
        # Добавление пассивного навыка
        elif self.type == "passive" and self not in char.p_skills:
            char.p_skills.append(self)

    def useSkill(self):
        # Установка значений в game_state вместо использования глобальных переменных
        self.game_state.damage = self.pwr
        self.game_state.mp_lost = self.mp_cost
        self.game_state.atk_sfx = "audio/battle/skills/" + self.sfx + ".ogg"
        self.game_state.msg_skill = self.name
        self.game_state.s_trans = self.trans

class PassiveSkill(Skill):
    # Конструктор для пассивных навыков.
    def __init__(self, game_state, name, sfx=None, img=None, trans=None, lvl=0, type='passive'):
        super(PassiveSkill, self).__init__(name, game_state, sfx, img, trans, lvl, type)
        # Пассивные навыки могут иметь дополнительные свойства и методы

class ActiveSkill(Skill):
    # Конструктор для активных навыков.
    def __init__(self, game_state, name, pwr, mp_cost, sfx='sword', targ='enemy', targs=1, type='active', trans=None, img=None, dice=[2,8], acc=0, lvl=0, back_row=False):
        super(ActiveSkill, self).__init__(game_state, name, sfx, img, trans, lvl, type)
        self.pwr = pwr  # Мощность навыка
        self.mp_cost = mp_cost  # Стоимость использования навыка в мане
        self.targ = targ  # Цель навыка (например, враг)
        self.targs = targs  # Количество целей
        self.dice = dice  # Данные для броска (например, для вычисления урона)
        self.acc = acc  # Точность навыка
        self.lvl = lvl  # Уровень, с которого навык доступен
        self.back_row = back_row  # Доступность навыка для заднего ряда


class SkillManager:
    def __init__(self, game_state):
        self.game_state = game_state # Класс ответственный за основные параметры игры
    
    # Функция для проверки возможности использования навыка
    def skillChk(self, player, radar):
        # Проверка, блокируется ли навык радаром
        if self.radarFX(player, radar):
            return True
        else:
            self.game_state.skill_affected_targets.append(player)  # Добавление игрока в список целей навыка
            return False

    # Функция для эффекта радара (блокировки атаки)
    def radarFX(self, player, radar):
        self.game_state.radar_block = False
        # Проверка наличия радара у игрока
        if radar in player.p_skills:
            self.game_state.miss_roll = self.game_state.renpy.random.randint(1, 10)  # Случайный бросок
            if self.game_state.miss_roll > 2:
                self.game_state.renpy.play("audio/battle/skills/defend.ogg")  # Воспроизведение звука защиты
                self.game_state.radar_block = True
                self.game_state.skill_text = "blOcK!"
                self.game_state.renpy.pause(1, hard=True)  # Пауза
                return False
            else:
                return True
        else:
            return True

    def canTarget(self, monster):
        if self.game_state.renpy.get_screen("select_monster") and monster not in self.game_state.picked_targets:
            if not monster.dead:
                return True
        return False

    # Функция для применения эффектов после использования навыка
    def afterFX(self, target):
        # Применение эффекта навыка вампиризма
        if self.game_state.b_skill.img == "lifedrain":
            self.game_state.current_player._hp += target.finaldmg / 2
        # Применение эффекта навыка дренажа души
        if self.game_state.b_skill.img == "souldrain":
            self.game_state.current_player._hp += target.finaldmg

    # Функция для определения, может ли игрок использовать навык
    def sensIf(self, skill):
        # Проверка достаточности маны для использования навыка
        if self.game_state.current_player.mp > skill.mp_cost:
            # Проверка условий для навыка обмена местами
            if skill.img == "magicswap":
                # Навык недоступен, если остался один монстр
                if (monsters_total - self.game_state.monsters_dead) <= 1:
                    return False
            return True
        else:
            return False