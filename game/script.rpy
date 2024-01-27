label start_battle:
    $ battle_manager.prepareBattle(enemies=current_battle_monsters)
    jump battle_loop

label battle_loop:
    call battle from _call_battle
    $ battle_manager.restorehp()
    $ battle_manager.restoremp()
    jump battle_loop
