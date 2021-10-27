import time
import random
import sys

# 2 second pause is made after the text is printed
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# Intro of what is happening
def intro():
    print_pause("You find yourself in an abandoned alley "
                "late in the night.")
    print_pause("It's getting cold here...")
    print_pause("Your goal is to safely come home.")
    

# Validation of the player's input
def valid_input(message_to_print, options):
    while True:
        response = input(message_to_print).lower()
        for option in options:
            if option in response:
                response = option
                return response
        print_pause("Sorry, I don't understand!")
        print_pause("Choose something from the list!")
  

# Things that happen when the player meets a scary man
def scary_man(item, again_list):
    if item == "gun":
        print_pause("You pointed the gun at the man, he got scared "
                    "and ran away.")
        print_pause("You may continue your way.")
    elif item == "holy water" or item == "ball":
            print_pause("It isn't something effective against the scary man.")
            print_pause("You lost as you didn't manage to come home safely.")            
            play_again(again_list)


# Things that happen when the player meets an angry dog
def angry_dog(item, again_list):
    if item == "ball":
        print_pause("With throwing the ball you distructed the dog.")
        print_pause("The dog run after the ball! You may continue your way.")
    elif item == "gun" or item == "holy water":
            print_pause("It wasn't effective against the dog! The dog became mad.")
            print_pause("You've also got beaten by the dog, "
                "and you won't come back home.")
    play_again(again_list)

        
# Things that happen when the player meets a vampire
def vampire(item, again_list):
    if item == "holy water":
        print_pause("You splashed water in vampires' faces.")
        print_pause("They disappeared!")
        print_pause("You may continue your way.")
    elif item == "ball" or item == "gun":
        print_pause("You can't kill vampires with that "
                    "if you didn't know that...")
        print_pause("You lost! You've also become a vampire, and "
                    "you won't come back home.")
        play_again(again_list)


# Using an item in the bagpack against enemies
def act_1(enemy, item, items_trunk, again_list, enemies):
    # No repeatition during a game   
    enemies.remove(enemy)
    if enemy == "scaryman":
        scary_man(item, again_list)
    elif enemy == "angrydog":
        angry_dog(item, again_list)
    elif enemy == "vampire":
        vampire(item, again_list)
    items_trunk.append(item)


#  Exchanging an item in the bagpack
def act_2(enemy, item, items_trunk, again_list, enemies):
    print_pause("You came to the ancient trunk.")
    print_pause(f"Which item do you want to exchange {item} for?\n")
    items_trunk.append(item)
    print_pause(f" - {items_trunk[0].capitalize()}\n"
                f" - {items_trunk[1].capitalize()}\n")
    item = valid_input("Enter a name of the item.\n", items_trunk)
    print_pause(f"You just put {item} in your bagpack and returned to the {enemy}.")
    items_trunk.remove(item)
    act_1(enemy, item, items_trunk, again_list, enemies)

    
# Picking an item from the ["ball", "gun", "holy water"] list
def find_trunk(items_trunk):
    print_pause("On your way home, you find an ancient trunk with "
                "three different items in it.")
    print_pause("You can choose only one item.")
    print_pause("What do you want to take?\n")
    print_pause(f" - {items_trunk[0].capitalize()}\n"
                f" - {items_trunk[1].capitalize()}\n"
                f" - {items_trunk[2].capitalize()}\n")
    item = valid_input("Enter a name of the item.\n", items_trunk)
    print_pause(f"You put {item} in your bagpack and continued going home")
    items_trunk.remove(item)
    return item


# A choice of actions after meeting an enemy:
# 1.use an item against the enemy.
# 2.return to the trunk and pick another item.
def meet_enemy(item, items_trunk, actions, again_list, enemies):
    # Enemy is chosen in a random order    
    enemy = random.choice(enemies)
    print_pause(f"Oh nooo, you've been approached by a {enemy}.")
    print_pause("What's your next step?\n")
    print_pause(f" 1. Take {item} out of the bag.\n"
                " 2. Run back fast to the ancient trunk to exchange your item.\n")
    action = valid_input("Enter '1' or '2'.\n", actions)
    if action == '1':
        act_1(enemy, item, items_trunk, again_list, enemies)
    elif action == '2':
        act_2(enemy, item, items_trunk, again_list, enemies)


# After the game is over, the user can play the game again
def play_again(again_list):
    print_pause("Do you want to play again?")
    response = valid_input("Enter 'yes' or 'no'.\n", again_list)
    if response == "yes":
        print_pause("Great! Restarting the game...\n")
        play_game()
    elif response == "no":
        print_pause("Thanks for playing! See you next time.\n")
    sys.exit()


def body(items_trunk, enemies, actions, again_list):
    while len(enemies) != 0:
        item = find_trunk(items_trunk)
        meet_enemy(item, items_trunk, actions, again_list, enemies)
    print_pause("Congrats!")
    print_pause("You defeated all enemies and safely came home!")
    play_again(again_list)


def play_game():
    items_trunk = ["ball", "gun", "holy water"]
    enemies = ["scary man", "angry dog", "vampire"]
    actions = ['1', '2']
    again_list = ["yes", "no"]
    intro()
    body(items_trunk, enemies, actions, again_list)

play_game()
