from areas import Street
from Enemy import Big_Cheese
from print_speed import print_medium as pm 
from print_speed import print_slow as ps
import time
from battles import Battle
import random

def main(player, return_to_playground_callback):
    
    buildings_in_loopy_lane = [
        "Jest for Laughs",
        "Cogs.inc"
    ]
    loopy_lane = Street(name="Loopy Lane", cogs=[], buildings=buildings_in_loopy_lane )

    print()
    print()
    pm("-----------------------------------------------")
    print()
    pm("You have entered Loopy Lane.")
    print()
    pm("-----------------------------------------------")
    print()
    print()
    time.sleep(.5)
    
    for _ in range(5):
        loopy_lane.spawn_random_cog()
        
    while True:
        print(f"Your current laffpoints: {player.health}") 
        print()   
        loopy_lane.display_choices()
        print("0: Leave.")
        print()
        choice = input("Enter your choice: ").strip()
        
        if not choice.isdigit():
            ps("Oops! Okay speed demon, lets try this again... (input valid number)")
            time.sleep(.7)
            continue
        
        choice = int(choice)
        
        if 1 <= choice <= len(loopy_lane.cogs):
            choice -= 1
            print(f"You choose to fight the {loopy_lane.cogs[choice].cog_class} : {loopy_lane.cogs[choice].type_name} (level {loopy_lane.cogs[choice].level})")
            battle = Battle(player, loopy_lane.cogs[choice], return_to_playground_callback)
            battle_fight_result = battle.fight()
            
            if battle_fight_result:
                del loopy_lane.cogs[choice]
                
        elif choice == 0:
            return_to_playground_callback(player)
            ps("Leaving loopy lane..")
            break
        
        elif len(loopy_lane.cogs) < choice <= len(loopy_lane.cogs) + len(loopy_lane.buildings):
            choice = choice - len(loopy_lane.cogs) - 1
            
            print(f"You enter: {loopy_lane.buildings[choice]}")
            
            if loopy_lane.buildings[choice] == "Jest for Laughs":
            
                    jokes = [
                        ("Why don't scientists trust atoms?", "Because they make up everything."),
                        ("Why don't programmers like nature?", "It has too many bugs."),
                        ("Why don’t skeletons fight each other?", "They don’t have the guts."),
                        ("What do you get when you cross a snowman and a vampire?", "Frostbite.")
                    ]

                    def get_random_joke():
                        return random.choice(jokes)
                    
                    if not player.mini_quest_completed:
                        exit_outer_loop = False
                        while True:
                            pm("Welcome to Jest for Laughs! We've usually got better jokes than laughing lessons...")
                            pm("But its hard to be silly when the cogs have taken over the building next door!")
                            pm("Say.... Would you be willing to take it back ")
                            print("0: Leave.")
                            print("1: Yes!")
                            print("2: No.")
                    
                    
                            choice_str = input()
                            if not choice_str.isdigit():
                                pm("Please enter a valid number.")
                                continue
            
                            laughing_choice = int(choice_str)
                        
                            if laughing_choice == 0:
                                break
                                    
                            elif laughing_choice == 1:
                                while True:
                                    pm("Great! in order for you to be successful, i can tell you everything i know so far.")
                                    pm("There is a Big Cheese level 8 Cog in there, hes got 79 health!")       
                                    pm("In order to prepare you for this big fight, I can teach you some of what i know...")
                                    print("1: Gain Throw EXP")
                                    print("2: Gain Squirt EXP")
                                    print()
                            
                                    choice_str = input()
                                    if not choice_str.isdigit():
                                        pm("Please enter a valid number.")
                                        continue
                                    
                                    exp_choice = int(choice_str)
                                    if exp_choice in [1,2]:
                                        if exp_choice ==1:
                                            track_to_gain = "throw"
                                        elif exp_choice ==2:
                                            track_to_gain = "squirt"
                                            
                                        exp_earned = 25
                                        
                                        #new_level, new_exp_threshold = 
                                        Battle.miniquest_exp_gain(player, track_to_gain, exp_earned)
                                        
                                        player.mini_quest_completed = True
                                        ps("That should give you an edge in battle!, Come back to see me when its all done!")
                                        ps("....You leave the building, back onto Loopy Lane.")
                                        exit_outer_loop = True
                                        break
                                    
                                    else:
                                        pm("Please enter a valid number.")
                                    continue
                                    
                            elif laughing_choice == 2:
                                        print("Oh... I understand. Let me know if you change your mind.")
                                        break
                            else:
                                pm("Please enter a valid number.")
                                continue
                            if exit_outer_loop:
                                break
                                    
                    elif player.mini_quest_completed:
                        if player.big_cheese_defeated:
                            while True:
                                pm("Welcome to Jest for Laughs! We've got better jokes than laughing lessons!")
                                pm("I heard about your victory against the Big Cheese! You're a true hero!")
                                pm("Would you like to hear a joke??")
                                print("0: Leave.")
                                print("1: Yes!")
                                print("2: No.")
                                
                                question, answer = get_random_joke()        
                                choice_str = input()
                                if not choice_str.isdigit():
                                    pm("Please enter a valid number.")
                                    continue
                
                                laughing_choice = int(choice_str)
                            
                                if laughing_choice == 0:
                                    break
                                elif laughing_choice == 1:
                                    pm(f"{question}")
                                    input()
                                    pm(f"{answer}")
                                    time.sleep(.07)
                                    print()
                                    continue
                                
                                elif laughing_choice == 2:
                                    print("Oh... okay... are you sure?")
                                    continue
                                else:
                                    pm("Please enter a valid number.")
                                    continue
                                
                        elif not player.big_cheese_defeated:
                            while True:
                                pm("Welcome to Jest for Laughs! We've usually got better jokes than laughing lessons...")
                                pm("Oh, its you again!") 
                                pm("If you are having trouble defeating the big cheese, Try just getting good!")
                                pm("Hahaha just kidding. Im sure the Toon HQ has rewards for you that can help you in the fight if you help them out!")
                                print("0:Leave")
                                print("1:Cry")
                                choice_str = input()
                                if not choice_str.isdigit():
                                    pm("Please enter a valid number.")
                                    continue
                
                                laughing_choice = int(choice_str)
                            
                                if laughing_choice == 0:
                                    break
                                elif laughing_choice == 1:
                                    pm("Its gonna be okay. Save some of those tears for your squirt gags and go destroy them all!")
                                    continue
                                else:
                                    pm("Please enter a valid number.")
                                    continue
                                
            elif loopy_lane.buildings[choice] == "Cogs.inc":
                while True:
                    pm("There is a Big Cheese in there! Are you sure you want to go in there???")
                    print("1.Yes!")
                    print("2.WHat??? No way!")
                    choice = input().strip()
                    if choice == "1" or choice.lower() == "yes":
                        ps("You gulp as you slowly open the door...")
                        big_cheese = Big_Cheese(8)
                        battle = Battle(player, big_cheese, return_to_playground_callback)
                        battle.fight()
                        battle_outcome = battle.check_battle_outcome()
                        if battle_outcome == "player_win":
                            player.big_cheese_defeated = True
                            ps("Big Cheese: I'll have you fired for this...")
                            ps("Congratulations! You have defeated the Big Cheese! You are a legend among Toons!")
                            ps("Thank you so much for taking the time to play this game, it really means a lot more to me than you know...")
                            pm("Its more than just some silly project. And you are a true friend. I owe you big time.")
                            time.sleep(.8)
                            pm("I could add more areas, more enemies, ways to fight multiple at once, etc. Im not sure the direction i want to go.")
                            pm("let me know what you think.")
                            # Add code to grant a reward to the player
                            break
                        elif battle_outcome == "player_lose":
                            ps("You fought valiantly but were defeated. Better luck next time!")
                        else:
                            battle_outcome == "player_lose"
                            ps("You fought valiantly. Better luck next time!")
                    elif choice == "2" or choice.lower() in ("what??? no way!", "no", "no way"):
                        pm("You decide not to go in.")
                        break
                    else:
                        pm("Invalid choice. Please try again.")
        else:
            pm("Enjoying exploring? keep trying, maybe you will find something eventually!")
            time.sleep(.8)
            print()
            continue
            
if __name__ == "__main__":
    main()

