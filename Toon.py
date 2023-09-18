import random
from print_speed import print_medium as print_medium
from print_speed import print_slow as print_slow
import time
import pickle
from math import floor


class Gag:
    def __init__ (self, name, gag_type, damage, hit_chance, exp, level, effects=None):
        self.name = name
        self.type = gag_type
        self.damage = damage
        self.hit_chance = hit_chance
        self.effects = effects or {}
        self.level = level
        self.exp = exp
        
    def apply_effects(self, player, enemy):
        for effect, value in self.effects.items():
            if effect == 'heal':
                healing_amount = min(value, player.max_health - player.health)
                player.health = min(player.max_health, player.health + round(healing_amount))
                print(f"{player.name} healed for {round(healing_amount)} laff points!")
               
            elif effect == 'soak':
                enemy.apply_soak_effect(value) # add effect to enemy class
class Toon:
    
    def __init__(self, health, jellybeans, max_jellybean_capacity, max_inventory_capacity, max_task_capacity, total_gag_count, name, animal, color):
        self.max_health = 15
        self.health = min(health, self.max_health)
        self.max_jellybean_capacity = max_jellybean_capacity
        self.jellybeans = min(jellybeans, self.max_jellybean_capacity)
        self.name = name
        self.animal = animal
        self.color = color
        self.inventory = ["Cupcake", "Squirting Flower"]
        self.max_inventory_capacity = max_inventory_capacity
        self.attacks = {#name, gag_type, damage, hit_chance, exp, level, effects=None
            "throw": [
                Gag("Cupcake", "throw", 6, 0.75, 2, 1, {"heal": {"value": 0.2}}),
                Gag("Fruit Pie Slice", "throw", 12, 0.75, 4, 2, {"heal": {"value": 0.2}}),
                Gag("Cream Pie Slice", "throw", 20, 0.75, 6, 3, {"heal": {"value": 0.2}}),
                Gag("Birthday Cake Slice","throw", 30, 0.75, 8, 4, {"heal": {"value": 0.2}}),
                Gag("Fruit Pie", "throw", 40, 0.75, 10, 5, {"heal": {"value": 0.2}}),
                
                # ... (other throw gags)
            ],
            "squirt": [
                Gag("Squirting Flower", "squirt", 4, 0.95, 2, 1, {"soak": {"duration": 2}}),### fix exp back to 2
                Gag("Glass of Water", "squirt", 8, 0.95, 4, 2, {"soak": {"duration": 2}}),
                Gag("Squirt Gun", "squirt", 13, 0.95, 6, 3,{"soak": {"duration": 2}}),
                Gag("Water Balloon", "squirt", 21, 0.95, 8, 4, {"soak": {"duration": 3}}),
                Gag("Water Seltzer", "squirt", 30, 0.95, 10, 5, {"soak": {"duration": 3}}),
                # ... (other squirt gags)
            ],
            "drop": [
                Gag("Plant Pot", "drop", 10, 0.6, 2, 1),
                Gag("Garbage Sack", "drop", 20, 0.6, 4, 2),
                Gag("Anvil", "drop", 30, 0.6, 6, 3),
                Gag("1 Ton Weight", "drop", 45, 0.6, 8, 4),
                Gag("Metal Safe", "drop", 60, 0.6, 10, 5),
                # ... (other drop gags)
            ],
            # ... (other gag types)
        }

        self.gag_counts = {gag_name: 0 for gag_name in self.inventory}
        total_gag_count = sum(self.gag_counts.values())
        self.total_gag_count = total_gag_count
        
        self.exp_earned_in_battle = {
            "throw": 0,
            "squirt": 0,
            "drop": 0
        }
        self.exp = {
            "throw": 0,
            "squirt": 0,
            "drop": 0
        }
        self.track_levels = {
            "throw": 1,
            "squirt": 1,
            "drop": 0
        }
        self.exp_thresholds = {
            "throw": {0: 0, 1: 10, 2: 50, 3: 100, 4: 250},
            "squirt": {0: 0, 1: 10, 2: 50, 3: 100, 4: 250},
            "drop": {0: 0, 1: 10, 2: 50, 3: 100, 4: 250},
        }
        
        
        self.current_tasks = []
        self.task_counts = 0
        self.max_task_capacity = max_task_capacity
        self.completed_tasks = set()
        
        
        
    def save_game(self):
        try:  
            with open('savegame.dat', 'wb') as file:
                self.view_inventory() #view inventory
                if self.task_counts == 0:
                    print("Your current tasks:")
                    print("No current tasks.")
                    print()
                else:
                    for task in self.current_tasks:
                        print("Your current tasks:")
                        print(f"Task {task.description}:{task.progress}/{task.target_progress}")
                        print()
                pickle.dump(self, file)
            print_slow("Game saved!")
        except Exception as e:
            print(f"Failed to save the game: {e}")
            
    @classmethod       
    def load_game(cls):
        try:    
            with open('savegame.dat', 'rb') as file:
                player = pickle.load(file)
                
            player.view_inventory() #view inventory
            if player.task_counts == 0:
                print("Your current tasks:")
                print("No current tasks.")
                print()
            else:
                for task in player.current_tasks:
                    print("Your current tasks:")
                    print(f"Task {task.description}:{task.progress}/{task.target_progress}")
                    print()
            
            print_slow(f"Game loaded! Welcome {player.name}")
        
            from Toontown_Central import main as Toontown_Central_main
            Toontown_Central_main(player)
            
        except Exception as e:
            print(f"Failed to load the game: {e}") 
            

    def create_new_player(name="", animal="", color=""):
        player = Toon(health=15, jellybeans=0, max_jellybean_capacity=30, max_inventory_capacity=10, max_task_capacity=1, total_gag_count=0, name=name, animal=animal, color=color)
        return player
    
    def create_default_player():
        return Toon.create_new_player(name="Tester", animal="Demon", color="Red")
    
    def take_damage(self, damage):
        self.health -= damage
        self.health = max(0, self.health)
        
    def increase_health(self, amount=1):
        self.max_health += amount
    
    def add_new_gag(self, gag_name, gag_type, increment_level=True):
        #print(f"Adding new gag: {gag_name}, Type: {gag_type}, Increment Level: {increment_level}")
        if gag_name not in self.inventory:
            self.inventory.append(gag_name)
            self.gag_counts[gag_name] = 0
            print_medium(f"Congratulations! You unlocked a new {gag_type} gag called {gag_name}!")
            
            if increment_level:
                self.track_levels[gag_type] += 1
                next_level = self.track_levels[gag_type]
            
                for gag in self.attacks[gag_type]:
                    if gag.level == next_level:
                        self.inventory.append(gag.name)
                        self.gag_counts[gag.name] = 0

                        break
            
            else:
                self.track_levels[gag_type] = 1    
        else:
            print_medium("You've already unlocked this gag!")
            
    def increase_max_inventory(self, amount=1):
        self.max_inventory_capacity += amount
    def increase_max_task_capacity(self, amount=1):
        self.max_task_capacity += amount
                
    def earn_jellybeans(self, amount):
        self.jellybeans += amount
        self.jellybeans = min(self.jellybeans, self.max_jellybean_capacity)
        
        for task in self.current_tasks:
            if task.task_type == "earn_jellybeans" and task.progress + amount <= task.target_progress:
                task.progress += amount
                print_medium(f"Task {task.description}:{task.progress}/{task.target_progress}")
                if task.is_complete() and task.status != "completed":
                    task.status = "ready for turn-in"
                    print_medium(f"Task {task.description}:{task.progress}/{task.target_progress} Completed! Go back to the HQ to turn in the task!")
                
                            
    def view_inventory(self):
        total_gag_count = sum(self.gag_counts.values())
        print()
        print_medium(f"Your current laffpoints: {self.health}")
        print_medium(f"Your inventory: ({total_gag_count}/{self.max_inventory_capacity})")
        print_medium(f"Jellybeans: ({self.jellybeans}/{self.max_jellybean_capacity})")
        for gag_type in self.track_levels:
            
            current_level = self.track_levels[gag_type]
            current_exp = self.exp[gag_type]
            exp_threshold = self.exp_thresholds[gag_type][current_level]
            
              
            print_medium(f"{gag_type.capitalize()} EXP: {current_exp} / {exp_threshold} (Level {current_level})")
        # a dictionary to store the counts of each gag type
        for idx, gag_name in enumerate(self.inventory, start=1):
            count_str = f" ({self.gag_counts.get(gag_name, 0)})"
            print(f"{idx}. {gag_name}{count_str}")
    
    def is_gag_unlocked(self, gag_name):
        return gag_name in self.inventory
    
    def get_unlocked_gags(self): 
        unlocked_gags = []
        for gag_type in self.attacks:
            for gag in self.attacks[gag_type]:
                if self.is_gag_unlocked(gag.name):
                    unlocked_gags.append(gag)
        return unlocked_gags
      
    def get_gag_counts(self):
        return self.gag_counts
        
    def buy_gag(self, gag_name, quantity=1):
        if self.jellybeans < quantity:
            print_medium("You don't have enough jellybeans to buy a gag.")
            return
                
        if self.total_gag_count + quantity > self.max_inventory_capacity:
            print_medium("You cant carry that many gags.")
            return
        
        if gag_name not in self.gag_counts:
            print_medium("We don't have any of those im afraid.")
            return
        
        self.jellybeans -= quantity
        self.gag_counts[gag_name] += quantity
        self.total_gag_count += quantity
        print_medium(f"You bought {quantity} {gag_name} gag!")   
        return self.inventory.index(gag_name)
               
    
            
            
    def get_gag_name_from_input(self,input_str):
        if input_str =="0":
            return "exit"
        try:
            idx = int(input_str)
            if 1 <= idx <= len(self.inventory):
                return self.inventory[idx - 1]
        except ValueError:
            pass
        
        input_str_lower = input_str.lower()
        for gag_name in self.inventory:
            if input_str_lower == gag_name.lower():
                return gag_name
        return None
    
    def give_gags(self, gag_names, quantity):
        for gag_name in gag_names:
            if gag_name in self.inventory:
                self.gag_counts[gag_name] += quantity
            else:
                print(f"warning: invalid gag")

    def use_gag(self, target, gag_name, battle_instance):
        if gag_name in self.inventory:
            corresponding_gag = None
            for gag_type in self.attacks.values():
                for gag in gag_type:
                    if gag.name == gag_name:
                        corresponding_gag = gag
                        break
                if corresponding_gag:
                    break
            
            if corresponding_gag:
                self.gag_counts[gag_name] = max(0, self.gag_counts[gag_name] - 1)
                self.total_gag_count -= 1
                
                attack_damage = corresponding_gag.damage
                hit_chance = corresponding_gag.hit_chance
                
                if battle_instance.enemy.is_soaked:
                    hit_chance = min(1.0, hit_chance +0.10)
                    
                
                damage_dealt, hit = self.attack_logic(target, attack_damage, hit_chance)
                
               
        
            #damage calculation for the players attack
    
            if hit:
                print("-----------------------------------------------")
                print(f"You used {gag_name} and hit!")
                print(f"You deal {attack_damage} damage.")
                print()

                battle_instance.apply_effects(corresponding_gag, target, damage_dealt)
                
                self.exp_earned_in_battle[corresponding_gag.type] += corresponding_gag.exp
                
               
            else:
                print("-----------------------------------------------")
                print(f"You used {gag_name} but missed!")
                print()
             
        else:
            print("You don't have that gag in your inventory.")
            return False
    
    def choose_attack(self): # random attack maybe for npc later? needs updating with new gag class
        return random.choice(self.attacks)
    
    
    def attack(self, target):
        chosen_attack = self.choose_attack()
        attack_name = chosen_attack["name"]
        attack_damage = chosen_attack["damage"]
        hit_chance = chosen_attack["hit_chance"]
        
        damage_dealt, hit = self.attack_logic(target, attack_damage, hit_chance)
        return attack_name, damage_dealt, hit
    
    
            
    def attack_logic(self, target, damage, hit_chance):
            if random.random() < hit_chance:
                target.health -= damage
                return damage, True
            else:
                return 0, False
    def is_valid_input(self, input_str): #this is used for valid choices in the gag shop i think, could also be used in battle to make sure the user has grace when choosing an option
        if input_str == '0':
            return True
        for idx, gag_name in enumerate(self.inventory, start=1):
            if input_str.lower() == str(idx) or input_str.lower() == gag_name.lower():
                return True
        return False
    
    def get_valid_choice():
        while True:
            choice = input()
            
            if choice.isdigit() and 0<= int(choice) <= 4:
                return int(choice)
            print_medium("sorry, what was that? (invalid number)")
            
    def get_battle_input(self, targets): #supposed to handle the input of gag choices and running in a battle
        while True:
            print_medium("It's your turn! Choose an action:")
            print("0: Run!!!")
            for idx, gag_name in enumerate(self.inventory, start=1):
                count_str = f" ({self.gag_counts.get(gag_name, 0)})"
                print(f"{idx}. {gag_name}{count_str}")
            if len(targets) > 1:
                print("choose a target:")
                for idx, target in enumerate(targets, start=1):
                    print(f"{idx}: {target.name} - Health: {target.health}")
                    
            choice = input()
            
            if self.is_valid_input(choice):
                return choice 
            else:
                print_medium("Invalid choice. Try again!")
            
    def perform_battle_action(self, choice, target): #supposed to perform the input in a battle but using it before got stuck in a loop
        if choice == "0":
            print_medium("You attempt to run...")
            if random.random() < 0.5:
                print_medium("...You successfully escaped the battle!")
            else:
                print_slow("... You couldnt escape this time!")
        elif choice.isdigit() and 1 <= int(choice) <= len(self.inventory):
            chosen_gag_name = self.inventory[int(choice) - 1]
            if self.gag_counts.get(chosen_gag_name, 0) > 0:
                self.use_gag(target, chosen_gag_name)
              
            else:
                print_medium("You are out of that gag! Choose another.")
            
        #else:
            #print_medium("Not so good with numbers? Try again!")
            
    def add_task(self, task):
        if not isinstance(task, Task):
            raise ValueError("expected a Task object but recieved a different type")
        if len(self.current_tasks) < self.max_task_capacity:
            self.current_tasks.append(task)
            self.task_counts += 1
            print()
            print_medium(f"Task '{task.description}' added!")
            print()
            print()
            time.sleep(.7)
        else:
            print_medium("You are at your task limit! progress further to increase this.")
            print()
            print()
            time.sleep(.7)
            
    def view_tasks(self):
        for task in self.current_tasks:
            print(task.description)
            
    def complete_task(self, task_name):
        task_to_complete = next((task for task in self.current_tasks if task.task_name == task_name), None)
        if task_to_complete:
            task_to_complete.complete(self)
            
        else:
            print_slow("Task not found!")
            
    def check_tasks(self, defeated_enemy):################????????????

        for task in self.current_tasks:
            task.check_task(defeated_enemy, self)
                
class Task:
    def __init__(self, description, reward_callback, reward_description, task_name, target_progress, task_type, task_detail, reward_type):
        self.task_name = task_name
        self.description = description
        self.reward_callback = reward_callback
        self.reward_description = reward_description
        self.reward_type = reward_type
        self.status = "not started"
        self.progress = 0
        self.target_progress = target_progress
        self.task_type = task_type
        self.task_detail = task_detail

    
    def is_complete(self):
        return self.progress >= self.target_progress
    
    def matches_task(self, enemy): #returns the info of the info of defeated enemies to attempt to match the 
        if self.task_type =="category":
            return enemy.category == self.task_detail
        if self.task_type == "level":
            return enemy.level >= int(self.task_detail) # need to make sure its greater or equal to for level
        if self.task_type == "type_name":
            return enemy.type_name == self.task_detail
            
        else:
            print("no match buckaroo")
            return False
        
    def check_task(self, defeated_enemy,player):
        if self.matches_task(defeated_enemy):
            self.progress_tasks(player)
        print(f"Task {self.description}:{self.progress}/{self.target_progress}")
            
    def progress_tasks(self,player):
        self.progress +=1
        if self.is_complete() and self.status != "completed":
            self.status = "ready for turn-in"
            print_medium(f"Task {self.description}:{self.progress}/{self.target_progress} Completed! Go back to the HQ to turn in the task!")
            print()
                
    def complete(self, player):
        if self.status != "completed":
            self.status = "completed"
            self.reward_callback()
            print(f"Task '{self.description}' completed!")
            print(f"Your reward is'{self.reward_description}'.")
            print("(You have been healed to full health for turning in a task!")
            player.health = player.max_health
            
            
player = Toon.create_default_player()      