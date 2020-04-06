import time
from Entity import Entity
import random as rand
items_file = "Items.txt"
entities_file = "Entities.txt"

def load_items(file):
    with open(file) as f:
        lines = f.readlines()
        
    dictionary = {}
    for line in lines:
        if "weapon" not in line:
            fields = line.split()
            name = fields[0]
            dictionary[name] = []
            dictionary[name].append(fields[1])
            dictionary[name].append(fields[2])
            dictionary[name].append(fields[3])
            dictionary[name].append(fields[4])
            
    return dictionary


def load_entities(file):
    with open(file) as f:
        lines = f.readlines()
    
    attributes = ['health','stamina','attack','damage','defense']
    dictionary = {}
    for line in lines:
        if "name" not in line:
            fields = line.split()
            name = fields[0]
            dictionary[name] = []
            for i in range(len(attributes)):
                dictionary[name].append(fields[i+1])
    return dictionary
            

def combat(attacker, defender):
    attack_stats = attacker.calculate_attack()
    defence = defender.current_defense
    
    attack_roll = rand.randint(1,20) + attack_stats['attack']
    print("attacked for ", attack_roll)
    time.sleep(1)
    if attack_roll > defence:
        print("hit")
        time.sleep(1)
        dmg_roll = rand.randint(1, attack_stats['damage'])
        defender.health -= dmg_roll
        print("dealt", dmg_roll, "damage")
    else:
        print("attack missed")
        
            
items = load_items(items_file)
entities = load_entities(entities_file)

orc = Entity(entities['Gelfing'], items)
player = Entity(entities['Player'], items, player=True)

while orc.health > 0 and player.health > 0:
    print("Player Health", player.health, "Player Stamina", player.stamina, "Orc Health", orc.health)
    combat(orc, player)
    print("Player Health", player.health, "Player Stamina", player.stamina, "Orc Health", orc.health)

    combat(player, orc)
    
if player.health >= 0:
    print("You win")
else:
    print("You lose")
    

        