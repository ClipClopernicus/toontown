
from print_speed import print_slow as ps
from print_speed import print_medium as pm
import time
from Toon import Toon

def main():
    while True:
        print("Welcome to a text based adventure game based on the game Toontown!")
        print("               Not affilated with Disney")
        print()
        print("                  MAIN MENU                ")
        print()
        print("1. New game")
        print()
        print("2. Load game")
        print()

        choice = input("Enter your choice: ").strip()
                
        if not choice.isdigit():
            ps("Oops! Okay speed demon, lets try this again... (input valid number)")
            time.sleep(.7)
            continue

        choice = int(choice)
        
        if choice == 1:
            ps("Starting new game...")
            ps("Would you like to play the tutorial or skip it?")
            print()
            print("1: Enter Tutorial")
            print()
            print("0: Skip Tutorial")
            print()
            from toontorial import main as toontorial_main
            decision = input("Press Enter to continue or type 0 to skip tutorial.")
            if decision == "1":
                toontorial_main()
            elif decision == "0":
                while True:
                    pm("Enter your toon's name, and then press enter (You will always need to press enter after typing your selection!)")
                    player_name = input()
                    pm(f"So, your name is {player_name}, Correct?")
                    print("1.Yes")
                    print("2.No")
    
                    player_confirmation = input().lower()
                    if player_confirmation == "1" or "yes" in player_confirmation:
                        break
                    elif player_confirmation == "2" or "no" in player_confirmation:
                        continue
                    
                    else:
                        print("huh? Okay, lets try this again.")
                        time.sleep(.8)
                        continue

                #Get player's animal choice
                animal_choices = ["Cat", "Dog", "Mouse"]
                while True:
                    pm("Choose your animal:")
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
                    ps("Choose your color:")
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
                from Toontown_Central import main as Toontown_Central_main
                Toontown_Central_main(player)
        elif choice == 2:
            Toon.load_game()
           
if __name__ == "__main__":
    main()