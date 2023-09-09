import random
from print_speed import print_medium as pm 
from print_speed import print_medium as print_medium
from print_speed import print_slow as ps
from print_speed import print_slow as print_slow
from Toon import Toon
from Enemy import Flunky
import time



def is_valid_input(self, input_str):
        if input_str == '0':
            return True
        for idx, gag_name in enumerate(self.inventory, start=1):
            if input_str.lower() == str(idx) or input_str.lower() == gag_name.lower():
                return True
        return False
            
    

def start_battle(player,level):
    flunky = Flunky(1) #create a level one flunky
    targets = [flunky]
    print()
    print()
    print_medium("-----------------------------------------------")
    print_slow("You have exited the tutorial building...")
    print_slow("You have encountered a Flunky in combat!")
    print_medium("-----------------------------------------------")
    print()
    print()
    
    flunky_begin_phrase = random.choice(flunky.begin_battle_phrases)
    print_slow(f"Flunky: {flunky_begin_phrase}")
    print()
    
    while player.health > 0 and flunky.health > 0:
        print_medium("________________________")
        print_medium(f"Your health: {player.health}|")
        print_medium(f"Flunky Level {level} health: {flunky.health}|")
        print_medium("---------------------------")
        print()
        
        #players turn
        while True:
            choice = player.get_battle_input(targets)
            if choice == "0":
                print_medium("You attempt to run...")
                if random.random() < 0.5:
                    print_medium("...You successfully escaped the battle!")
                    from Toontown_Central import main as Toontown_Central_main
                    Toontown_Central_main(player)
                else:
                    print_slow("... You couldnt escape this time!")
                    break
            if choice.isdigit() and 1 <= int(choice) <= len(player.inventory):
                chosen_gag_name = player.inventory[int(choice) - 1]
                if player.gag_counts.get(chosen_gag_name, 0) > 0:
                    player.use_gag(flunky, chosen_gag_name)
                    break
                else:
                    print_medium("You are out of that gag! Choose another.")
            #checkpoint 1       
            
    
        
        if flunky.health <=0:
            print_slow("Congratulations! you defeated the Flunky!")
            print_slow(".....)")
            print_medium("Thank you so much for doing that! I feel safer already!")
            print_medium("I can tell you are going to go far in Toontown!")
            print_medium("Many more Toons are in danger, and im sure you will be rewarded well for your help!")
            print_medium("At the playground there will be an HQ that you can get tasks from to help Toontown for rewards!")
            print_slow("...which reminds me!, heres 8 jellybeans for helping me out, you can buy more gags or ice cream with it!")
            print()
            print_slow(".....*You have recieved 8 jellybeans!")
            (print)
            jellybean_reward = 8
            player.earn_jellybeans(jellybean_reward)
            print_medium("Just through the tunnel is the Playground, Toontown Central. From there you will find plenty more to do!")
            print_slow("Good luck, and thanks again!")
            print()
            input("Press enter to go through the tunnel...")
            from Toontown_Central import main as Toontown_Central_main
            Toontown_Central_main(player)
            print()
            print()
        if player.health <= 0:
            print_slow("...Oh no, you've been defeated and are now sad!")
            break
        
        #flunkys turn
        print_medium("__________________")
        print_medium("It's the Flunky's turn!")
        flunky_attack_name, attack_damage, hit = flunky.attack()
        flunky_attack = next(attack for attack in flunky.attacks if attack["name"] == flunky_attack_name)
        flunky_attack_phrases = flunky_attack["phrases"]
        flunky_attack_phrase = random.choice(flunky_attack_phrases)
        if hit:
            print_medium("-----------------------------------------------")
            print_slow(f"Flunky: {flunky_attack_phrase}")
            print_medium(f"The Flunky used {flunky_attack_name} and hit!")
            print_medium(f"The Flunky dealt {attack_damage} damage to you!")
            print()
            player.health -= attack_damage
    
        else:
            print_slow(f"Flunky: {flunky_attack_phrase}")
            print_medium(f"The Flunky used {flunky_attack_name} but missed!")
            print()
        if player.health <= 0:
            print_slow("...Oh no, you've been defeated and are now sad!")
            print_slow("...........")
            print_slow("...Head low, You slowly make your way back to the playground...")
            print_slow("Cheer up. Ice cream heals all wounds.")
            from Toontown_Central import main as Toontown_Central_main
            Toontown_Central_main(player)
       
    
def main():
    print_slow("Welcome to Toontown! create your Toon here, and then you will be thrown into the action!")
    print("(you can press enter to speed up the text! also if you click on the terminal you might pause it)")
    print("To load game, enter the corresponding input after typing your name.")
    print()
    
    #Get player's name
    while True:
        print_medium("Enter your toon's name, and then press enter (You will always need to press enter after typing your selection!)")
        player_name = input()
        print_medium(f"So, your name is {player_name}, Correct?")
        print("1.Yes")
        print("2.No")
        print("9:Load Game.")
        player_confirmation = input().lower()
        if player_confirmation == "1" or "yes" in player_confirmation:
            break
        elif player_confirmation == "2" or "no" in player_confirmation:
            continue
        elif player_confirmation =='9':
                Toon.load_game()
        else:
            print("huh? Okay, lets try this again.")
            time.sleep(.8)
            continue

    #Get player's animal choice
    animal_choices = ["Cat", "Dog", "Mouse"]
    while True:
        print_slow("Choose your animal:")
        for idx, animal in enumerate(animal_choices, start=1):
            print(f"{idx}. {animal}")
            
        animal_choice = input()
        
        if animal_choice.isdigit():
            animal_choice = int(animal_choice)
            if 1 <= animal_choice <= len(animal_choices):
                player_animal = animal_choices[animal_choice - 1]
                break
            elif animal_choice == 666:
                player_animal = "Demon"
                print("Demon? Ohhh... Are you sure you want to be here in toontown? Alright... just play nice.")
                break
            else:
                print("Oops! Try again.")
                time.sleep(1)
                continue
        else:
            player_animal = "unknown"
            print("Oops! Try again.")
            time.sleep(.8)
            continue

    
    #Get player's animal color
    color_choices = ["Red", "Blue", "Yellow"]
    while True:
        print_slow("Choose your color:")
        for idx, color in enumerate(color_choices, start= 1):
            print(f"{idx}. {color}")
            
        color_choice = input()
        
        if color_choice.isdigit():
            color_choice = int(color_choice)
            if 1 <= color_choice <= len(color_choices):
                player_color = color_choices[color_choice - 1]
                break
            else:
                print("Oops! Try again.")
                time.sleep(.8)
                continue
        else:
            color_choice = "unknown"
            print("Oops! Try again.")
            time.sleep(.8)
            continue

    player = Toon.create_new_player(name=player_name, animal=player_animal, color=player_color)
    
    
    
    print_slow(f"Welcome {player_name} the {player_color} {player_animal}! We need your help. Cogs have infiltrated Toontown! ")
    decision = input("Press Enter to continue or type 0 to skip tutorial.")
    if decision == "0":
        from Toontown_Central import main as Toontown_Central_main
        Toontown_Central_main(player)
    else:

        print_medium("Cogs are robots programmed to ruin fun and replace it all with businesses, offices, and work!")
        print_medium("It's up to any Toon willing to fight back to save Toontown!")
        print_medium("We can use gags and tricks to defeat the cogs, such as throwing pies, or dropping anvils!")
        input("Press Enter to continue...")
        print_medium("The cogs will fight back though, and if you get hit enough you will become sad!")
        print_medium("Dont let your laffpoints(health) reach 0!")
        print()
        print_slow("This is what your laffpoints are at, and what gags you have...")
        player.view_inventory()
        print()
        input("Press enter to continue")
        print_slow(".....")
        print_slow("Speaking of cogs!!! There's a Flunky outside right now!")
        print_medium("If you could please defeat him for me I'd reward you with Jellybeans!")
        print_medium("Here are some gags to help you, you can throw cupcake or squirt this squirting flower at him!")
        print()
        print()
        print_slow("..... *You have recieved 2 cupcakes and 2 squirting flowers!")
        player.give_gags(["Cupcake", "Squirting Flower"], quantity=2)
        input("Press enter to go outside and fight the Flunky!")
        #battle
        start_battle(player,1)
        input("Press enter to enter the playground")
        from Toontown_Central import main as Toontown_Central_main
        Toontown_Central_main(player)
    
if __name__ == "__main__":
    main()