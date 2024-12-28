import time

def combat(player, enemy): 
    while player.health != 0 or enemy.hp != 0: 
        print("Player Turn")
        time.sleep(1.25)
        player.attack(enemy)
        if enemy.hp <= 0: 
            print("Congratulations, you have won!")
            print(f"{enemy.name}Health: 0")
            break
        else: 
            pass
        enemy.viewStats()
        time.sleep(1.25)
        print("Enemy Turn")
        time.sleep(1.25)
        enemy.attack(player)
        if player.health <= 0: 
            print("Player Health: 0")
            print("Game Over!")
            exit()
        else: 
            player.viewStats()
        time.sleep(1.25)