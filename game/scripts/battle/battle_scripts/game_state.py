class GameState:
    def __init__(self, renpy):
        self.renpy = renpy
        self.current_player = None  # Текущий игрок
        self.monsters = []  # Список монстров
        self.monsters_total = 0 # Общее количество монстров
        self.players = []  # Список игроков
        self.picked_targets = []  # Выбранные цели
        self.skill_targets = []  # Цели для навыков
        self.skill_affected_targets = [] # Цели подвергшиеся действию навыка
        self.radar_block = False  # Блокировка радара
        self.skill_text = ""  # Текст текущего навыка
        self.damage = 0  # Урон
        self.mp_lost = 0  # Потеря маны
        self.atk_sfx = ""  # Звуковой эффект атаки
        self.s_trans = None  # Трансформация навыка
        self.msg_skill = ""  # Сообщение о навыке
        self.monsters_dead = 0  # Количество мертвых монстров
        self.battle_end = False  # Флаг окончания битвы
        self.win = False  # Флаг победы
        self.monster_slot = None
        self.hit_t = []
        self.alive_players = [] # Список живых игроков
        self.mpdmg = 0
        self.battle_players = []
        self.battle_monsters = []
        self.missed_t = []
        self.picked_targs = []
        self.b_skill = "none"
        self.message = "none"
        self.msg_mons = ""
        self.miss_roll = 0
        self.curr_exp = 0
        self.party_list = []
        self.misstext = ""
        self.hp_lost = 0
        self.dropitem = None
        self.row1btn = False
        self.row2btn = False
        self.koplayer = None
        self.target = "none"
        self.misstext_list = ["ПромАх!", "ПромаХ!", "пРомах!", "пРоМаХ!"]
        self.sfx_whoosh = "audio/battle/whoosh1.ogg"
        self.sfx_monsterdead = "audio/battle/monsterdead1.ogg"

        self.initial_img_pos = -270
        self.initial_bar_pos = 102
        self.initial_dmg_pos = 294

        self.label_after_battle = ""

        self.planned_actions = []

        self.current_battle_background = "images/bg/1.webp"

        # BATTLES
        self.training_win_label = ""
        self.training_lose_label = ""

        # PLOT
        self.fahrenheit_rel = 0
        self.monument_rel = 0
        self.planar_rel = 0

        self.explotion_choice = True

        self.in_costume = True
        self.hero_costume = True

        self.press_conference_fails = 0

        self.attack_teen = True
        self.attack_resonance = True

        self.speak_with_teen = True
        self.speak_with_resonance = True

        self.battles = {"beat_nanoman" : False, "beat_resonance" : False, "beat_monument": False, "beat_planar": False}

        # 0 - fahrenheit
        # 1 - monument
        # 2 - planar
        # 3 - hospital
        self.act_first_weekend_place = 3

        self.first_monument_lose = True
        self.monument_win = True
        self.planar_win = True

    def add_monster(self, monster):
        self.monsters.append(monster)

    def update_current_player(self, player):
        self.current_player = player