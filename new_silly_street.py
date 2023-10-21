from areas import Street
from Enemy import Big_Cheese
from print_speed import print_medium as pm 
from print_speed import print_slow as ps
import time
from battles import Battle
import random
def main(player, return_to_playground_callback):
    
    buildings_in_silly_street = [
        "Laughing Lessons",
        "Cogs.inc"
    ]
    silly_street = Street(name="Silly Street", cogs=[],  buildings=buildings_in_silly_street )

    print()
    print()
    pm("-----------------------------------------------")
    print()
    pm("You have entered Silly Street.")
    print()
    pm("-----------------------------------------------")
    print()
    print()
    time.sleep(.5)
    for _ in range(5):
        silly_street.spawn_random_cog()
        
    while True:
        print(f"Your current laffpoints: {player.health}")
        print()    
        silly_street.display_choices()
        print("0: Leave.")
        print()
        choice = input("Enter your choice: ").strip()
        
        if not choice.isdigit():
            ps("Oops! Okay speed demon, lets try this again... (input valid number)")
            time.sleep(.7)
            continue
        
        choice = int(choice)
        
        if 1 <= choice <= len(silly_street.cogs):
            choice -= 1
            print(f"You choose to fight the {silly_street.cogs[choice].cog_class} : {silly_street.cogs[choice].type_name} (level {silly_street.cogs[choice].level})")
            battle = Battle(player, silly_street.cogs[choice], return_to_playground_callback)
            battle_fight_result = battle.fight()
            
            if battle_fight_result:
                del silly_street.cogs[choice]
                
        elif choice == 0:
            return_to_playground_callback(player)
            ps("Leaving Silly Street..")
            break
        
        elif len(silly_street.cogs) < choice <= len(silly_street.cogs) + len(silly_street.buildings):
            choice = choice - len(silly_street.cogs) - 1
            
            print(f"You enter{silly_street.buildings[choice]}")
            
            if silly_street.buildings[choice] == "Laughing Lessons":
            
                while True:
                    jokes = [
                    ("What goes 'Ha Ha Ha Thud'?", "Someone laughing his head off."),
                    ("What do you call a bear with no teeth?", "A gummy bear!"),
                    ("Why did the tomato turn red?", "Because it saw the salad dressing!")
                ]

                    def get_random_joke():
                        return random.choice(jokes)
                    question, answer = get_random_joke()
                    
                    pm("Welcome to Laughing lessons! Would you like a lesson?")
                    print("0: Leave.")
                    print("1: Yes!")
                    print("2: Nah.")
                    print("3: Let me give YOU one!")
                    
                    choice_str = input()
                    if not choice_str.isdigit():
                        pm("Please enter a valid number.")
                        continue
            
                    laughing_choice = int(choice_str)
                        
                    if laughing_choice == 0:
                        break
                            
                    if laughing_choice == 1:
                                pm(f"{question}")
                                input()
                                pm({answer})
                                time.sleep(.07)
                                print()
                                continue
                            
                    if laughing_choice == 2:
                                print("Oh... okay... are you sure?")
                                continue
                            
                    if laughing_choice == 3:
                                response = input("Tell me your joke:")
                                if response.lower() == "knock knock":
                                    pm("whos there?")
                                    response_two = input()
                                    input("continue...")
                                    print(f"{response_two} who?")
                                    print("HAHA THATS A GOOD ONE!")
                                    print()
                                    continue
                                else:
                                    laugh_responses = ["I've heard that one before. I find Knock Knock jokes hilarious though!", "Sorry, I spaced out. Can you repeat it real fast?"]
                                    laugh_response = random.choice(laugh_responses)
                                    pm(laugh_response)
                                    print()
                                    continue
            elif silly_street.buildings[choice] == "Cogs.inc":
                while True:
                    pm("There is a Big Cheese in there! Are you sure you want to go in there???")
                    print("1.Yes!")
                    print("2.What??? No way!")
                    choice = input().strip()
                    if choice == "1" or choice.lower() == "yes":
                        ps("You gulp as you slowly open the door...")
                        big_cheese = Big_Cheese(8)
                        battle = Battle(player, big_cheese, return_to_playground_callback)
                        battle.fight()
                        battle_outcome = battle.check_battle_outcome()
                        if battle_outcome == "player_win":
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