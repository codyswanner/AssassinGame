"""
1. Input players
2. Generate randomly-ordered list
3. When given a player name, reveal that player's target
4. When told a player is eliminated, remove that player from list and adjust targets
5. Respond with names of remaining players in new random order when asked
6. Track who eliminated whom?
"""
import random

f = open("players_list.txt", "w+")

next_player = ""
players = []

while next_player.lower() != "done":
    next_player = input("Name of player: ")
    if next_player.lower() == "list players":
        for p in players:
            print(p)
    elif next_player.lower() == "done":
        break
    else:
        players.append(next_player)

random.shuffle(players)

user_input = ""
while user_input != "exit":
    user_input = input("Enter command: ")
    if user_input.lower() == "reveal target":
        assassin = input("Whose target should be revealed?  ")
        if assassin in players:
            assassin_index = players.index(assassin)
            target_index = assassin_index + 1
            if target_index == len(players):
                target_index = target_index - len(players)
            print(assassin + "'s target is: " + players[target_index])
        else:
            print("Error: that is not a valid player name!")

    elif user_input.lower() == "eliminate player":
        target = input("Who is elimated?  ")
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

    elif user_input.lower() == "remaining players":
        display_players = players
        random.shuffle(display_players)
        print(display_players)
    elif user_input.lower() == "help" or user_input.lower() == '"help"':
        print("Available commands are:")
        print("reveal target -- shows the target of a given player")
        print("remaining players -- shows who is still in the game")
    elif user_input.lower() == "exit":
        break
    else:
        print('Invalid command, for help type "help"')



for p in players:
    f.write(p + "\n")
f.close()





