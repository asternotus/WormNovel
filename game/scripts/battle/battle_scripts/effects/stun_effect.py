from game.scripts.battle.battle_scripts.effects.effect import Effect

class StunEffect(Effect):
    def __init__(self):
        super().__init__("stunned", 1)
        self.image = "images/effects/stunned.png"