"""
1. Input players
2. Generate randomly-ordered list
3. When given a player name, reveal that player's target
4. When told a player is eliminated, remove that player from list and adjust targets
5. Respond with names of remaining players in new random order when asked
6. Track who eliminated whom?
"""
import random

###################################################
# functions

def reveal_target(assassin):
    if assassin in players:
            assassin_index = players.index(assassin)
            target_index = assassin_index + 1
            if target_index == len(players):
                target_index = target_index - len(players)
            print(assassin + "'s target is: " + players[target_index])
    else:
        print("Error: that is not a valid player name!")

def eliminate_player(target):
    if target in players:
            target_index = players.index(target)
            players.remove(target)
            reveal_next_target = input("Would you like to reveal your next target? (y/n): ")
            while reveal_next_target.lower() not in ("y", "n"):
                print("Please enter 'y' or 'n' only (without quotes)")
                reveal_next_target = input("Would you like to reveal your next target? (y/n): ")
            if reveal_next_target == "y":
                print("Your next target is: " + players[target_index])
            else:
                print("That is not a valid player name!")

def show_remaining_players():
    display_players = players
    random.shuffle(display_players)
    print(display_players)

def show_help():
    available_commands = (
        "reveal target -- shows the target of a given player",
        "remaining players -- shows who is still in the game",
        "eliminate target -- removes target from the game and optionally shows player's next target")
    print("Available commands are:")
    for command in available_commands:
        print(command)

# end functions
###################################################

f = open("players_list.txt", "w+")

next_player = ""
players = []

# TODO: create a "add player" function
# TODO: prevent entry of empty string as a player name (if user hits enter without text, prompt them to type "done" to finish player entry)
while next_player.lower() != "done":
    next_player = input("Name of player: ")
    if next_player.lower() == "list players":
        for p in players:
            print(p)
    elif next_player.lower() == "done":
        break
    else:
        players.append(next_player)

# Shuffle the players into a random list
# The player below you on the list is your target
random.shuffle(players)

# wrap into user input handler function?
user_input = ""
while user_input != "exit":
    user_input = input("Enter command: ")
    
    if user_input.lower() == "reveal target":
        assassin = input("Whose target should be revealed?  ")
        reveal_target(assassin)

    elif user_input.lower() == "eliminate player":
        target = input("Who is elimated?  ")
        eliminate_player(target)

    elif user_input.lower() == "remaining players":
        show_remaining_players()

    elif user_input.lower() == "help" or user_input.lower() == '"help"':
        show_help()

    elif user_input.lower() == "exit":
        break
    else:
        print('Invalid command, for help type "help"')



for p in players:
    f.write(p + "\n")
f.close()





