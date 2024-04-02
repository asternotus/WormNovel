from random import choice

class Game:
    def __init__(self, renpy, game_state, battle, enemy, player):
        self.renpy = renpy
        self.game_state = game_state
        self.enemy = enemy
        self.player = player
        self.battle = battle

        # Инициализация слотов в соответствии с количеством слотов противника
        self.skill_slots = [None] * enemy.skill_slots_count
        self.selected_skills = []
        self.indicators_shown = False
        self.damage_text = "0"
        self.panel_is_closed = False
        self.confirm_button_shown = True
        self.damage_animation_visible = False
        self.slot_styles = ["skill_slot_blank"] * enemy.skill_slots_count

        self.enemy_dead = False
        self.player_dead = False
        self.death_animation_completed = False

    def log_battle(self, text):
        with open('battle.txt', 'a') as file:
            file.write(text + '\n') 

    def start_battle(self):
        self.renpy.show_screen("game_hint", hint_message="Выбор цели")

    def start_select_skills(self):
        self.renpy.show_screen("game_hint", hint_message="Выбор действий (от 1 до 3)")

    def finish_select_skills(self):
        self.renpy.show_screen("game_hint", hint_message="")

    def finish_damage_animation(self):
        self.renpy.show_screen("game_hint", hint_message="Выбор цели")

    def hide_all_battle_screens(self):
        self.renpy.hide_screen("battle_screen")
        self.renpy.hide_screen("game_hint")
        self.renpy.hide_screen("skill_info")
        self.renpy.hide_screen("skill_panel")
        self.renpy.hide_screen("damage_animation_enemy")
        self.renpy.hide_screen("check_end_game_conditions")

    def compare_skills_with_weakness(self):
        exact_matches = 0
        partial_matches = 0

        for i, skill in enumerate(self.selected_skills):
            if i < len(self.enemy.weakness) and skill == self.enemy.weakness[i]:
                exact_matches += 1
            elif skill in self.enemy.weakness:
                partial_matches += 1

        return [exact_matches, partial_matches]

    def apply_skills(self):
        # Нанесение урона игроку от противника
        enemy_skill = choice(self.enemy.skills)
        damage = enemy_skill.apply(self.player)
        self.show_damage_animation(damage, "player")

        # Проверка на победу игрока
        if self.compare_skills_with_weakness()[0] == len(self.enemy.weakness):
            self.enemy.hp = 0
            self.enemy_dead = True
            self.game_state.battles[self.battle] = True
            self.renpy.show_screen("check_end_game_conditions")

        # Проверка на поражение игрока
        if self.player.hp <= 0:
            self.player_dead = True
            self.game_state.battles[self.battle] = False
            self.renpy.show_screen("check_end_game_conditions")          

    def show_damage_animation(self, damage, target_name):
        if target_name == "enemy":
            pass
        else:
            self.renpy.hide_screen("damage_animation_enemy")
            self.renpy.show_screen("damage_animation_enemy", damage_amount=damage, target="player")

        self.damage_animation_visible = damage > 0

    def add_skill_to_slot(self, skill_image):
        for i in range(len(self.skill_slots)):
            if self.skill_slots[i] is None:
                self.skill_slots[i] = skill_image
                break
        self.renpy.restart_interaction()

    def clear_slot(self, index):
        if 0 <= index < len(self.skill_slots) and self.skill_slots[index] is not None:
            self.skill_slots[index] = None
            self.renpy.restart_interaction()

    def save_skills(self):
        self.selected_skills = [slot for slot in self.skill_slots if slot is not None]
        self.indicators_shown = True
        self.confirm_button_shown = False

    def hide_skill_panel(self):
        self.renpy.hide_screen("skill_panel")
        self.panel_is_closed = False
        self.reset_for_next_turn()
        self.slot_styles = ["skill_slot_blank"] * self.enemy.skill_slots_count

    def reset_for_next_turn(self):
        self.apply_skills()
        self.selected_skills = []
        self.indicators_shown = False
        self.skill_slots = [None] * len(self.skill_slots)  # Сброс слотов с сохранением их количества
        self.confirm_button_shown = True
        self.renpy.restart_interaction()