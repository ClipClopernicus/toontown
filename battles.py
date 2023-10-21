import random
import Enemy
from print_speed import print_medium as pm 
from print_speed import print_slow as ps
from hq import HQ
from Toontown_Central import return_to_playground
import time
in_battle = False
def return_to_playground_callback(player):
    ps("Returning to playground...")
    return_to_playground(player)
class Battle:
    
    def __init__(self, player, enemy, return_to_playground_func):
        self.player = player
        self.enemy = enemy
        self.in_battle = True
        self.return_to_playground_func = return_to_playground_func
        self.exp_earned = {
            "throw": 0,
            "squirt": 0,
            "drop": 0
        }
    def apply_effects(self, gag, enemy, damage_dealt):
        for effect, value in gag.effects.items():
            if effect == "heal":
                healing_amount = min(damage_dealt*value['value'], self.player.max_health - self.player.health)
                self.player.health = min(self.player.max_health, self.player.health + round(healing_amount))
                print(f"{self.player.name} healed for {round(healing_amount)} laff points!")
               
            elif effect == "soak":
                self.enemy.is_soaked = True
                self.enemy.soak_duration = gag.effects['soak']['duration']
                enemy.apply_soak_effect(value['duration'])
                print(f"Soak applied with duration {self.enemy.soak_duration}")
                 
    
    def update_effects(self):
        if self.soak_duration > 0:
            self.soak_duration -= 1
            if self.soak_duration == 0:
                self.enemy.is_soaked = False
    
    def check_battle_outcome(self):
        if self.enemy.health <=0:
            return "player_win"
        elif self.player.health <= 0:  # Adjust the condition based on your HP tracking logic
            return "player_lose"
        else:
            return "ongoing"
                    
    def enemy_name(self):
        return self.enemy.__class__.__name__
    
    def end_turn(self):
            
            if self.enemy:
                if self.enemy.soak_duration > 0:
                    if self.enemy.soak_delay:
                        self.enemy.soak_delay = False
                    else:
                        self.enemy.soak_duration -= 1

                    if self.enemy.soak_duration == 0:
                        self.enemy.is_soaked = False
                
    def fight(self):
        
        enemy_begin_phrase = random.choice(self.enemy.begin_battle_phrases)
        ps(f"{self.enemy.type_name}: {enemy_begin_phrase}")
        while self.player.health > 0 and self.enemy.health >0 and self.in_battle:
            self.player_turn()

            if self.enemy.health <= 0:
                ps(f"Congratulations! you've defeated the {self.enemy.type_name}!")
                time.sleep(.5)
                self.end_battle()
                return True
                
            self.enemy_turn()
            if self.player.health <=0:
                ps("...Oh no, you've been defeated and are now sad!")
                ps("The Cogs take all your gags!")##
                
                for gag in self.player.inventory: # remove gags
                    gag.quantity = 0
                    
                ps("...........")
                ps("...Head low, You slowly make your way back to the playground...")
                ps("Cheer up. Ice cream heals all wounds.")
                self.return_to_playground_func(self.player)
                self.in_battle = False
                break
           
    ## remove all gags
    
    def player_turn(self):
        pm("________________________")
        pm(f"Your health: {self.player.health}|")
        pm(f"{self.enemy.type_name} level {self.enemy.level} health: {self.enemy.health}|")
        if self.enemy.is_soaked:
            pm(f"The {self.enemy.type_name} is soaked for {self.enemy.soak_duration} more turns!")
        pm("---------------------------")
        print()
        total_gag_count = self.player.total_gag_count
        #players turn
        while True:
            pm("It's your turn! Choose an action:")
            print("0: Run!!!")
                                            
            for idx, gag in enumerate(self.player.inventory, start=1):
                print(f"{idx}. {gag.name} ({gag.quantity})")
            print()
            print(f"{total_gag_count}/{self.player.max_inventory_capacity}")
            print()
            print()
            
            choice_str = input()
            if not choice_str.isdigit():
                pm("Theres no gag there! (Enter a valid number.)")
                continue
            
            choice = int(choice_str)
            
            if choice == 0:
                ps("You attempt to run...")
                if random.random() < 0.6: #60% chance to run successfully
                    print("You successfully run away from the battle!")
                    self.return_to_playground_func(self.player)
                    self.in_battle = False
                    break
                else:
                    ps("...You couldn't escape this time!")
                    break
            
            elif 1 <= choice <= len(self.player.inventory):
                chosen_gag = self.player.inventory[choice - 1]
                if chosen_gag.quantity > 0:
                    self.player.use_gag(self.enemy, chosen_gag, self)
                    break
                
                else:
                    pm("You are out of that gag! choose another.")
                continue
                
            else:
                pm("Not so good with numbers? Try again!")


    
    def enemy_turn(self):
        pm("__________________")
        pm(f"It's the {self.enemy.type_name}'s turn!")   
        
        enemy_attack_name, damage_dealt, hit = self.enemy.attack()
        
        enemy_attack = next(attack for attack in self.enemy.attacks if attack["name"] == enemy_attack_name)
        
        enemy_attack_phrase = random.choice(enemy_attack["phrases"]) 
        
        if hit:
            print("-----------------------------------------------")
            ps(f"{self.enemy.type_name}: {enemy_attack_phrase}")
            pm(f"The {self.enemy.type_name} used {enemy_attack_name} and hit!")
            pm(f"The {self.enemy.type_name} dealt {damage_dealt} damage to you!")
            print()
            self.player.health -= damage_dealt
        else:
            ps(f"{self.enemy.type_name}: {enemy_attack_phrase}")
            pm(f"The {self.enemy.type_name} used {enemy_attack_name} but missed!")
            print()
        self.end_turn()    
        
    def check_level_up(self, gag_type):
        current_level = self.player.track_levels[gag_type]
        current_exp = self.player.exp[gag_type]
        exp_threshold = self.player.exp_thresholds[gag_type][current_level]
        
        #print(f"Checking level up for {gag_type}")  # New print statement
        #print(f"Current level: {current_level}")  # New print statement
        #print(f"Current exp: {current_exp}")  # New print statement
        #print(f"Exp threshold: {exp_threshold}")  # New print statement
        
        if current_exp >= exp_threshold:
            self.player.track_levels[gag_type] += 1
            new_level = self.player.track_levels[gag_type]
            
            exp_threshold = self.player.exp_thresholds[gag_type][new_level]
            
            print()
            print(f"After leveling up: New level: {new_level}, New threshold: {exp_threshold}")  # Debug statement
            print()
            #print(f"\r{gag_type.capitalize()} {current_exp} / {exp_threshold}", end="", flush=True)
            #print()
            for gag in self.player.attacks[gag_type]:
                if gag.level == new_level:
                    self.player.add_new_gag(gag.name, gag.type, increment_level=False)
                    break
            return new_level, exp_threshold
        else:
            return current_level, exp_threshold
               
    def end_battle(self):
        #give out exp, items, task progress etc

        self.player.check_tasks(self.enemy)
        
        exp = self.player.exp
        exp_earned_in_battle = self.player.exp_earned_in_battle
        
        print()
        pm("Battle ended. You are dancing! EXP earned in this battle:")
        time.sleep(.5)
        for gag_type in exp:
            initial_exp = exp[gag_type]
            exp_earned = exp_earned_in_battle[gag_type]
            current_level = self.player.track_levels[gag_type]
            exp_threshold = self.player.exp_thresholds[gag_type][current_level]
            
              
            if current_level > 0:
                print(f"{gag_type.capitalize()} Exp {initial_exp} / {exp_threshold} + {exp_earned} ... = ", end="", flush=True)    
            
                for i in range(exp_earned):
                    print(f"\r{gag_type.capitalize()} Exp {initial_exp} / {exp_threshold} + {exp_earned} ... = {initial_exp + i + 1} / {exp_threshold}", end="", flush=True)
                    time.sleep(.2)
                    
                exp[gag_type] += exp_earned
                
                print()
                
                
                self.player.track_levels[gag_type], self.player.exp_thresholds[gag_type][current_level] = self.check_level_up(gag_type)
                
                print(f"\r{gag_type.capitalize()} Exp {self.player.exp[gag_type]} / {self.player.exp_thresholds[gag_type][current_level]}")
                
                
            time.sleep(0.7)    
            print()    
            exp_earned_in_battle[gag_type] = 0
        #if i != exp_earned:
            #print("\r" + "" * (len(gag_type) + len(str(initial_exp)) + len(str(exp_earned)) + len(str(exp_threshold)) + 18) + "\r", end="", flush=True)
        
    def miniquest_exp_gain(player, track_to_gain, exp_earned):
    # Get the current state before EXP gain
       
        
        initial_exp = player.exp[track_to_gain]
        current_level = player.track_levels[track_to_gain]
        exp_threshold = player.exp_thresholds[track_to_gain][current_level]
        
        # Display the initial state
        print(f"{track_to_gain.capitalize()} Exp {initial_exp} / {exp_threshold} + {exp_earned} ... = ", end="", flush=True)
        
        # Dynamically display EXP gain
        for i in range(exp_earned):
            print(f"\r{track_to_gain.capitalize()} Exp {initial_exp} / {exp_threshold} + {exp_earned} ... = {initial_exp + i + 1} / {exp_threshold}", end="", flush=True)
            time.sleep(.08)
        
        # Update the player's EXP
        player.exp[track_to_gain] += exp_earned
        
        # Print the final state
        print()
        
        # Check if the player levels up and handle it appropriately
        new_level, new_exp_threshold = player.check_player_level_up(track_to_gain)  # Adjust this call as necessary to fit your check_level_up method
        
        # Display the final EXP and threshold
        print(f"\r{track_to_gain.capitalize()} Exp {player.exp[track_to_gain]} / {new_exp_threshold}")    
    
    
            