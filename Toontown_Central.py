import random
import time
from Toon import Toon, Task       
from print_speed import print_medium as pm 
from print_speed import print_medium as print_medium
from print_speed import print_slow as ps
from print_speed import print_slow as print_slow
from Enemy import Flunky
from hq import HQ
def return_to_playground(player):
    main(player)
def enter_silly_street(player):
    from new_silly_street import main as Silly_street_main
    Silly_street_main(player, return_to_playground)

def enter_loopy_lane(player):
    from loopy_lane import main as loopy_lane_main
    loopy_lane_main(player, return_to_playground)

def get_valid_input(prompt, valid_choices=None):
    while True:
        user_input = input(prompt)
        if user_input.strip() == "":
            print_medium("Oops! Try again.")
            continue
        if valid_choices is not None and user_input not in valid_choices:
            print_medium("...what are you doing? (choose valid number)")
            continue
        return user_input
    
def start_anywhere(player=None):
    if not player:
        player = Toon.create_default_player()
        print(f"Player created: {player.name}, {player.animal}, {player.color}")    
    return player
    
def gag_shop(player):
    
        print_medium(f"Welcome to the Gag Shop, {player.name}!")
        print_medium("Here, you can buy Gags to use in battle!")
        print()
        print_medium("Clerk: Each gag only costs 1 Jellybean, and I'VE ONLY THE FINEST WARES IN THE LAND.")
        time.sleep(.5)
        unlocked_gags = player.get_unlocked_gags()
        selected_gag = None
        while True:
            print()
            print_medium("Current inventory:")
            player.view_inventory()
            print()
            print("Available gags on the shelves:")
            for idx, gag in enumerate(unlocked_gags, start=1):
                print(f"{idx}. {gag.name} - Damage: {gag.damage} - Hit Chance: {gag.hit_chance}"),
            
            print_medium("0: Leave Gag Shop.")
            print("99: Delete Gags")
            print()
            
            
            gag_choice = input()
            selected_gag=player.get_gag_from_input(gag_choice, unlocked_gags)
            
            if selected_gag == 'exit' :
                print_slow("Leaving the gag shop...")
                print()
                for idx, central_movement in enumerate(central_movement_choice, start=1):
                    print(f"{idx}. {central_movement}")
                    print()
                print("8: Save Game")
                print("9: Load Game")
                break
            
            if gag_choice == '99':
                print("Which gag would you like to delete? (enter 0 to cancel)")
                for idx, gag in enumerate(player.inventory, start=1):
                    print(f"{idx}. {gag.name}")

                gag_number = input()

                if gag_number.isdigit():
                    gag_number = int(gag_number)
                    
                    if gag_number == 0:
                        print_medium("Canceled.")
                        selected_gag = None
                        continue
                    
                    elif 1 <= gag_number <= len(unlocked_gags):
                        selected_gag_to_delete = player.get_gag_from_input(str(gag_number), player.inventory)

                        if selected_gag_to_delete:
                            while True:
                                print(f"How many {selected_gag_to_delete.name} would you like to delete? (enter 0 to cancel)")
                                quantity_str = input()

                                if quantity_str == '0':
                                    print_medium("Canceled.")
                                    break

                                elif quantity_str.isdigit() and int(quantity_str) > 0:
                                    quantity = int(quantity_str)
                                    player.remove_gag(selected_gag_to_delete.name, quantity)
                                    print_slow("Anything else?")
                                    selected_gag = None
                                    break
                                    
                    else:
                        print("Invalid selection. Please choose a valid gag number.")
                        
                else:
                    print("Please enter a valid number.")
                            
            
            
            if selected_gag is None:
                print_slow("Im sorry, we dont have any of those. anything else?")
                
            
            else:
                while True:
                    print(f"How many {selected_gag.name} would you like to buy? (enter 0 to cancel)")
                    quantity_str = input()
                    if quantity_str == '0':
                        print_medium("Canceled.")
                        break
                
                    elif quantity_str.isdigit() and int(quantity_str) > 0:
                        quantity = int(quantity_str)
                        
                        player.buy_gag(selected_gag.name, quantity)

                        #print_medium(f"You purchased {quantity} {selected_gag} gags!")
                        print_slow("Anything else?")
                        break
central_movement_choice = ["Earn Jellybeans", "Enter the Gag Shop", "Enter Silly Street","Enter Loopy Lane", "Check Inventory, health, and Toontasks", "Buy ice cream to heal", "Enter Toon HQ"]            
def Toon_hq(player):
    hq = HQ(player)

    print()
    print_medium(f"Welcome to the Toon HQ, {player.name}!")
    print(f"If you complete 5 tasks we will give you a bonus reward! {player.tasks_completed}/5")
    print("Let us know if you are having trouble completing a task and you can remove it for a new one!")
    ready_for_turn_in = any(task.status == "ready for turn-in" for task in player.current_tasks)
                            
    if ready_for_turn_in:
        print_medium("I see you have a task to turn in! Thanks for all your help!")
        hq.turn_in_tasks()
        print()
        print_medium("Would you like another task?")
    else:
        print_medium("Here, you can see what kind tasks the toons of Toontown Central need help with!")
        pm("Heres a list of the current tasks we have.")
        print()
    time.sleep(.5)
    while True:
         
        if player.task_counts == 0:
            pm("________________________")
            print(f"Your current tasks:{player.task_counts}/{player.max_task_capacity}")
            print("No current tasks.")
            pm("-----------------------")
            print()
        else:
            pm("________________________")
            print(f"Your current tasks: {player.task_counts}/{player.max_task_capacity}")
            for task in player.current_tasks:
                print(f"{task.description}")
            pm("-----------------------")
            print()
        
        tasks = hq.get_random_tasks()
        
        print("Available tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. Task: {task.description}    Reward: {task.reward_description}")
        
        print("0: Leave HQ, back to playground.")
        print("999: Remove task.")
        print()
        
        valid_choices = [str(i) for i in range(len(tasks) + 1)] + ['999']
        choice_str = get_valid_input("Choose a task number: ", valid_choices)
        choice = int(choice_str)
        
        if choice == 0:
            ps("Leaving the hq...")
            print()
            for idx, central_movement in enumerate(central_movement_choice, start=1):
                print(f"{idx}. {central_movement}")
                print()
            print("8: Save Game")
            print("9: Load Game")
            break
        elif choice == 999:
            print("Your current tasks:")
            for idx, task in enumerate(player.current_tasks, 1):
                print(f"{idx}. {task.description}")
            
            abandon_choice = int(input("Which task do you want to abandon? Enter the number (or 0 to cancel): "))
            
            if abandon_choice == 0:
                return
            elif 1 <= abandon_choice <= len(player.current_tasks):
                task_to_remove = player.current_tasks[abandon_choice - 1]
                player.remove_task(task_to_remove)
                continue
            else:
                print("Invalid choice!")
                continue
            
        chosen_task = tasks[choice - 1]
        hq.assign_task_to_toon(player,chosen_task)
        time.sleep(.4)
        
        
        
            
                           
def main(player):
    
        print()
        print()
        print_slow("...")
        print_medium(f"Hello {player.name} the {player.color} {player.animal}! Welcome to Toontown Central! This is a safe area.")
        print("Here, you can earn Jellybeans with which you can purchase gags!")#gamble?
        print("The Toon HQ has tasks you can complete for rewards!")
        print("If you are feeling brave, you can venture off onto Loopy Lane and fight the cogs who are trying to take over Toontown!")
        print_medium("What would you like to do?")
        print()
        print(f"Your current laffpoints: {player.health}")
        print()
        
        central_movement_choice = ["Earn Jellybeans", "Enter the Gag Shop", "Enter Silly Street","Enter Loopy Lane", "Check Inventory, health, and Toontasks", "Buy ice cream to heal", "Enter Toon HQ"]
            
        earn_jellybean_phrases = [
                "You helped out old man Jenkins and earned 4 jellybeans!",
                "You played a game on the trolley and earned 4 jellybeans!",
                "You went fishing and earned 4 jellybeans!"
            ]
        
        for idx, central_movement in enumerate(central_movement_choice, start=1):
                print(f"{idx}. {central_movement}")
                print()
        print("8: Save Game")
        print("9: Load Game")
        while True:
            choice = input()
    
            if choice == '1':
            #make dat money
                if player.jellybeans == player.max_jellybean_capacity:
                    print("Your jellybean jar is full!")
                else:
                    jellybean_reward = 4
                    player.earn_jellybeans(jellybean_reward)
                    random_phrase = random.choice(earn_jellybean_phrases)
                    print(random_phrase)
                
            elif choice == '2':
            #enter gag shop
                gag_shop(player)
            elif choice == '3':
            #Enter silly street
                if player.health < 1:
                    print_medium("You are sad! Heal up first before leaving the playground.")
                else:
                    enter_silly_street(player)
            
            elif choice == '4':
                if player.health < 1:
                    print_medium("You are sad! Heal up first before leaving the playground.")
                else:
                    ps("Entering Loopy lane...")
                    enter_loopy_lane(player)
                    
            elif choice == '5':
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
                    
            elif choice == '6':
                if player.jellybeans >=5: #buy icecream
                    print_medium("You buy and eat a delicious ice cream, healing your wounds!")
                    player.health = player.max_health
                    player.jellybeans -=5
                else:
                    print("You don't have enough jellybeans to buy ice cream.")
                    
            elif choice == '7': #enter toon hq
                Toon_hq(player)
                
            elif choice == '8':
                player.save_game()
                
            elif choice =='9':
                player.load_game()
            elif choice == '69': #easter egg
                player.give_gags(["Cupcake", "Squirting Flower"], quantity=2)
                print("NICE! You found 2 cupcakes and 2 squirting flowers!")
                
            elif choice == "":
                print_slow("Oops! Okay speed demon, lets try this again...")  
                time.sleep(.4)
                            
            elif choice == ValueError:
                print_medium("...how did you do that?")
            else:
                print_medium("Enjoying exploring? keep trying, maybe you will find something eventually!")
                time.sleep(.4)
            
if __name__ == "__main__":
    player = start_anywhere()    
    main(player)
