image white = "#FFFFFF"

image bb1 = "images/bg/1.webp"
image bb2 = "images/bg/2.webp"
image bb3 = "images/bg/3.webp"

image act_first_prologue_street = "images/bg/act_first_prologue_street.png"
image act_first_prologue_police = "images/bg/act_first_prologue_police.png"
image act_first_prologue_running = "images/bg/act_first_prologue_running.png"
image act_first_prologue_onground = "images/bg/act_first_prologue_onground.png"

image space_item1 = "images/bg/space_item1.webp"
image space_item2 = "images/bg/space_item2.webp"
image space_item3 = "images/bg/space_item3.webp"
image space_item4 = "images/bg/space_item4.webp"

image interview_office = "images/bg/interview_office.png"
image interview_office_photo = "images/bg/interview_office_photo.png"
image interview_office_sword = "images/bg/interview_office_sword.png"
image interview_office_endbringer = "images/bg/interview_office_endbringer.png"

image worm_title = "images/bg/worm_title.png"
image act_first_title = "images/bg/act_first_title.png"

image knight_costume_smile = "images/char/knight_costume_smile.png"
image knight_costume_widesmile = "images/char/knight_costume_widesmile.png"
image knight_costume_confused = "images/char/knight_costume_confused.png"
image knight_costume_angry = "images/char/knight_costume_angry.png"

image legion_idle = "images/char/legion_idle.png"

image worm_story_room = "images/bg/worm_story_room.png"

image worm_story_healing = "images/bg/worm_story_healing.png"
image worm_story_fire = "images/bg/worm_story_fire.png"
image worm_story_airplain = "images/bg/worm_story_airplain.png"
image worm_story_said_zion = "images/bg/worm_story_said_zion.png"
image worm_story_nuclear = "images/bg/worm_story_nuclear.png"
image worm_story_help_people = "images/bg/worm_story_help_people.png"
image worm_story_triggers = "images/bg/worm_story_triggers.png"
image worm_story_many_skills = "images/bg/worm_story_many_skills.png"
image worm_story_comix = "images/bg/worm_story_comix.png"

image worm_story_behemoth = "images/bg/worm_story_behemoth.png"
image worm_story_protactorate = "images/bg/worm_story_protactorate.png"
image worm_story_leviathan = "images/bg/worm_story_leviathan.png"
image worm_story_two_endbringers = "images/bg/worm_story_two_endbringers.png"
image worm_story_war = "images/bg/worm_story_war.png"

image player_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "game_state.current_player == spark","images/char/glow/player_battle.webp",
    "spark.dead == True","images/char/blank.webp",
    "True", "images/char/player_battle.webp")
image yu_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "game_state.current_player == knight","images/char/glow/yu_battle.webp",
    "knight.dead == True","images/char/blank.webp",
    "True", "images/char/yu_battle.webp")

image radar_anim = At("images/anim/radar.webp", idle_sway)
