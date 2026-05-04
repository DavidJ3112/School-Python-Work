import random
import time

player_data = {
    "first_name": input('Input First name player '),
    "last_name": input('Input last name player '),
    "max_hp": int(input('Hp Count player ')),
    "hp": 0,
    "def": 5,
    "strenth": 10,
    "total heals": 3,
}

enemy_data = {
    "first_name": input('Input First name enemy '),
    "last_name": input('Input last name enemy '),
    "max_hp": int(input('Hp Count enemy ')),
    "hp": 0,
    "def": 5,
    "strenth": 10,
    "total heals": 3,
}

enemy_data["hp"] = enemy_data["max_hp"]
player_data["hp"] = player_data["max_hp"]


def guard(def_player):
    attack_def_player = random.uniform(def_player, def_player * 3.3)
    attack_def_player = int(f'{attack_def_player:.0f}')
    attack_cycle(player_data["strenth"],attack_def_player)

def heal():
    if player_data["total heals"] > 0 and player_data["hp"] < player_data["max_hp"]:
        healamount = random.randint(10, 20)
        player_data["hp"] = player_data["hp"] + healamount
        player_data["total heals"] -= 1
        print(f'healed {healamount}')
    else:
        print('no remaining heals or healing needed')

    if player_data["hp"] > player_data["max_hp"]:
                player_data["hp"] = player_data["max_hp"]

def attack():
    player_atk_dmg = random.uniform(player_data["strenth"], player_data["strenth"] * 1.6)
    player_atk_dmg = int(f'{player_atk_dmg:.0f}')
    attack_cycle(player_atk_dmg, player_data["def"])


def attack_cycle(player_atk, player_def):
    global enemy_data,player_data
    enemy_atk = enemy_data["strenth"]
    enemy_def = enemy_data["def"]
    for i in range(enemy_data["total heals"]):
        if random.random() < 0.30 or enemy_data["total heals"] < 1 or enemy_data["hp"] == enemy_data["max_hp"]:
            if random.random() < 0.50:
                enemy_atk = int(f'{random.uniform(enemy_data["strenth"], enemy_data["strenth"]*1.2):.0f}')
                enemy_def = enemy_data["def"]
                break
            else:
                enemy_def = int(f'{random.uniform(enemy_data["def"], enemy_data["def"]*2.3):.0f}')
                enemy_atk = 0
                break
        else:
            if enemy_data["total heals"] > 0 or enemy_data["hp"] < enemy_data["max_hp"]:
                healamount = random.randint(10, 20)
                enemy_data["hp"] = enemy_data["hp"] + healamount
                enemy_data["total heals"] -= 1
                print(f'{enemy_data["first_name"]} {enemy_data["last_name"]}, healed {healamount}')
            if enemy_data["hp"] > enemy_data["max_hp"]:
                enemy_data["hp"] = enemy_data["max_hp"]

    player_damage = int(f'{enemy_atk * (100 / (100 + player_def)):.0f}')
    enemy_damage = int(f'{player_atk * (100 / (100 + enemy_def)):.0f}')
    
    player_data["hp"] -= enemy_damage
    enemy_data["hp"] -= player_damage

    if player_data["total heals"] <= 6:
        player_data["total heals"] += 1
    if enemy_data["total heals"] <= 6:
        enemy_data["total heals"] += 1

    print(f'{player_data["first_name"]} did {player_damage} damage')
    print(f'{enemy_data["first_name"]} did {enemy_damage} damage')

run = True
while run:
    if player_data["hp"] <= 0:
        print(f'\033[91m{player_data["first_name"]} {player_data["last_name"]} you have failed this city\033[0m')
        break
    if enemy_data["hp"] <= 0:
        print(f'\033[92m{player_data["first_name"]} {player_data["last_name"]} you have are this city hero\033[0m')
        break
    
    action_quastion = True
    action = ''
    while action_quastion:
        try:
            action = int(action)
            action_quastion = False
        except:
            action_quastion = True
            print("\033[2J\033[H")
            print(f'Player {player_data["first_name"]} {player_data["last_name"]}, \033[91mHp : {player_data["hp"]}\033[0m, \033[92m Remaining heals:{player_data["total heals"]} \033[0m')
            print(f'Enemy: {enemy_data["first_name"]} {enemy_data["last_name"]},  \033[91mHP : {enemy_data["hp"]}\033[0m, \033[92m Remaining heals:{enemy_data["total heals"]} \033[0m')

            print('-'*50)

            print('what interation do you want to do?')
            action = input('\033[94m1: guard\033[0m, \033[92m2: Heal\033[0m, \033[91m3: Attack\033[0m ')

    if action == 1:
        guard(player_data["def"])
    elif action == 2:
        heal()
    elif action == 3:
        attack()
    else:
        print('invailid')
    time.sleep(1.5)