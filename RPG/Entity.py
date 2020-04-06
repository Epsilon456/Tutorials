# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:25:04 2020

@author: Epsilon
"""
import random as rand
class Item:
    def __init__(self, stat_list):
        self.attack = stat_list[0]
        self.damage = stat_list[1]
        self.defense = stat_list[2]
        self.stamina = stat_list[3]
        

class Entity:
    def __init__(self, stat_list, items, player=False):
        self.health = int(stat_list[0])
        self.stamina = int(stat_list[1])
        self.attack = int(stat_list[2])
        self.damage = int(stat_list[3])
        self.defense = int(stat_list[4])
        self.player = player
        
        self.current_defense = self.defense
        
        self.items = []
        for item_name in items:
            item_object = Item(items[item_name])
            self.items.append([item_name, item_object])
            
    def check_moves(self):
        available_moves = []
        string = "Select attack:\n"
        for i in range(len(self.items)):
            item = self.items[i]
            if self.add_modifier(self.stamina,item[1].stamina) <= self.stamina:
                string += str(i)+") "+item[0] + "\t"
                string += "ATK"+item[1].attack+"\t"
                string += "DMG"+item[1].damage+"\t"
                string += "STA"+item[1].stamina+"\t"
                string += "DEF"+item[1].defense+"\n"
                available_moves.append(i)
        return string, available_moves
    
    def select_move(self):
        menu_string, moves_list = self.check_moves()
        
        if self.player == True:
            selected_move = -1
            while selected_move not in moves_list:
                selected_move = int(input(menu_string))
                if selected_move not in moves_list:
                    print("Move not available.\nPlease pick a different move")
        else:
            selected_move = -1
            while selected_move not in moves_list:
                selected_move = rand.randint(1,len(self.items))
            
        
        move = self.items[selected_move][1]
        print("Used ", self.items[selected_move][0])
        
        return move
                
    def add_modifier(self, base,modifier):
        sign = modifier[0]
        number = int(modifier[1:])
        
        if sign == "+":
            return base+number
        if sign == "-":
            return base-number

    def calculate_attack(self):
        weapon = self.select_move()
        attack = self.add_modifier(self.attack, weapon.attack)
        damage = self.add_modifier(self.damage, weapon.damage)
        defense = self.add_modifier(self.defense, weapon.defense)
        stamina = self.add_modifier(self.stamina, weapon.stamina)
        
        self.current_defense = defense
        self.stamina = stamina
        
        return {'attack':attack, 'damage':damage}
        

        
        
        
                
                
                
            
            
            
        
        
    
        
        
        