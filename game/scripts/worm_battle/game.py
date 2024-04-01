from random import choice

class Game:
    def __init__(self, renpy, game_state, battle, enemy, player):
        self.renpy = renpy
        self.game_state = game_state
        self.skill_slots = [None, None, None]
        self.selected_skills = []
        self.current_number = 0
        self.number_animation_running = False
        self.damage_text = "0"
        self.damage_color = "#FFFFFF"
        self.animation_counter = 0
        self.number_color = "#FFFFFF"
        self.should_close_panel = False
        self.show_confirm_button = True
        self.damage_animation_visible = False
        self.enemy = enemy
        self.player = player

        self.damage_thresholds = {0: 0, 1: 6, 2: 11, 3: 16}
        self.current_difficulty = 0
        self.slot_styles = ["skill_slot_blank", "skill_slot_blank", "skill_slot_blank"]
        self.skill_slot_style = "skill_slot_blank"

        self.enemy_dead = False
        self.player_dead = False

        self.death_animation_completed = False

        self.battle = battle

    def log_battle(self, text):
        with open('battle.txt', 'a') as file:  # Открывает файл для добавления текста ('a' означает append)
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
        self.renpy.hide_screen("damage_animation")
        self.renpy.hide_screen("damage_animation")
        self.renpy.hide_screen("damage_animation_enemy")
        self.renpy.hide_screen("check_end_game_conditions")

    def update_slot_styles_based_on_weakness(self):
        for i, skill in enumerate(self.skill_slots):
            if skill is None:
                self.slot_styles[i] = "skill_slot_blank"
            elif skill in self.enemy.weakness:
                if i < len(self.enemy.weakness) and skill == self.enemy.weakness[i]:
                    self.slot_styles[i] = "skill_slot_green"
                else:
                    self.slot_styles[i] = "skill_slot_yellow"
            else:
                self.slot_styles[i] = "skill_slot_red"

    def check_weakness(self, selected_skills):
        return selected_skills == self.enemy.weakness

    def apply_skills_or_enemy_attack(self, defender, is_enemy=False):
        if is_enemy:
            enemy_skill = choice(self.enemy.skills)
            damage = enemy_skill.apply(defender)
            self.show_damage_animation(damage, "player")
            
        else:
            total_damage = 0

            if self.current_number >= self.current_difficulty:
                if self.check_weakness(self.selected_skills):
                    total_damage += self.enemy.max_hp
                    self.enemy.hp -= max(total_damage, 0)
                else:
                    for skill in self.selected_skills:
                        total_damage += skill.apply(defender)
            self.show_damage_animation(total_damage, "enemy")

        if self.enemy.hp <= 0:
            self.enemy_dead = True
            self.death_animation_started = True
            self.game_state.battles[self.battle] = True
            self.renpy.show_screen("check_end_game_conditions")
            
        elif self.player.hp <= 0 and self.enemy.hp > 0:
            self.player_dead = True
            self.death_animation_started = True
            self.game_state.battles[self.battle] = False
            self.renpy.show_screen("check_end_game_conditions")
            

    def show_damage_animation(self, damage, target_name):
        if damage > 0:
            self.damage_text, self.damage_color = str(damage), "#FF0000"
        else:
            self.damage_text, self.damage_color = "Промах", "#FFFFFF"

        if target_name == "enemy":
            self.renpy.hide_screen("damage_animation")
            self.renpy.show_screen("damage_animation", damage_amount=damage, target="enemy")
        else:
            self.renpy.hide_screen("damage_animation_enemy")
            self.renpy.show_screen("damage_animation_enemy", damage_amount=damage, target="player")

        self.damage_animation_visible = damage > 0

    def add_skill_to_slot(self, skill_image):
        for i in range(len(self.skill_slots)):
            if self.skill_slots[i] is None:
                self.skill_slots[i] = skill_image
                self.renpy.restart_interaction()
                break

    def clear_slot(self, index):
        if self.skill_slots[index] is not None:
            self.skill_slots[index] = None
            self.renpy.restart_interaction()

    def animate_number(self):
        if self.number_animation_running and self.animation_counter < 20:
            self.current_number = self.renpy.random.randint(1, 20)
            self.animation_counter += 1
        else:
            self.number_animation_running = False
            self.update_number_color()
            self.should_close_panel = True

    def save_skills_and_start_number_animation(self):
        self.selected_skills.clear()
        self.selected_skills = [slot for slot in self.skill_slots if slot is not None]
        self.number_animation_running = True
        self.show_confirm_button = False

        self.current_difficulty = 10
        for skill in self.selected_skills:
            self.current_difficulty += skill.difficulty

        if self.check_weakness(self.selected_skills):
           self.current_difficulty = 10 
        
    def update_number_color(self):
        self.number_color = "#00FF00" if self.current_number >= self.current_difficulty else "#FF0000"

    def hide_skill_panel(self):
        self.renpy.hide_screen("skill_panel")
        self.should_close_panel = False
        self.apply_skills_or_enemy_attack(self.enemy)
        self.reset_for_next_turn()
        self.current_number = 0
        self.current_difficulty = 0
        self.number_color = "#FFFFFF"
        self.slot_styles = ["skill_slot_blank" for _ in range(3)]

    def reset_for_next_turn(self):
        self.selected_skills = []
        self.number_animation_running = False
        self.animation_counter = 0
        self.skill_slots = [None, None, None]
        self.show_confirm_button = True
        self.renpy.restart_interaction()
        self.apply_skills_or_enemy_attack(self.player, is_enemy=True)

    def hide_damage_animation(self):
        self.damage_animation_visible = False
        self.renpy.hide_screen("damage_animation")