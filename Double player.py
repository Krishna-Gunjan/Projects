import os
from getpass import getpass

def Rules():
    print("""You have chosen to play duos. The rules are:
                1. You can choose from three valid option.
                        Stone/Scissor/Paper
                2. Your choosen option will be hidden from the other players.
                3. At the end, the one with most wins wins the game
            """)
    while True:
        flag = input("Enter \"start\" to start the Game: ")
        os.system('cls')
        if flag == "start" or flag == "Start" or flag == "START":
            break
    
    hand_1 = player_1()
    hand_2 = player_2()
    num_of_wins_of_player_1, num_of_wins_of_player_2 = scoreboard(hand_1, hand_2)
    new_game(num_of_wins_of_player_1, num_of_wins_of_player_2)

def player_1():
    print("                 PLAYER 1                 ")
    while True:
        hand_1 = getpass("Choose your hand (Stone/Paper/Scissor): ")
        if hand_1 == "Stone" or hand_1 == "Paper" or hand_1 == "Scissor":
            break
        else:
            os.system('cls')
            print("Please choose from one of the given options")
    
    os.system('cls')
    return hand_1

def player_2():
    print("                 PLAYER 2                    ")
    while True:
        hand_2 = getpass("Choose your hand (Stone/Paper/Scissor): ")
        if hand_2 == "Stone" or hand_2 == "Paper" or hand_2 == "Scissor":
            break
        else:
            os.system('cls')
            print("Please choose from one of the given options")
    os.system('cls')

    return hand_2

num_of_wins_of_player_1 = 0
num_of_wins_of_player_2 = 0

def scoreboard(hand_1, hand_2):
    global num_of_wins_of_player_1, num_of_wins_of_player_2

    possible_wins = {
        "Stone" : "Paper",
        "Scissor" : "Stone",
        "Paper" : "Scissor"
        }
    if hand_2 == hand_1:
        print("It's a Tie!")
        print("Number of wins of Player 1: ", num_of_wins_of_player_1)
        print("Number of wins of Player 2: ", num_of_wins_of_player_2)

    elif possible_wins[hand_1] == hand_2:
        print("Player 2 Wins!")
        num_of_wins_of_player_2 += 1
        print("Number of wins of Player 1: ", num_of_wins_of_player_1)
        print("Number of wins of Player 2: ", num_of_wins_of_player_2)
    
    elif possible_wins[hand_1] != hand_2:
        print("Player 1 Wins!")
        num_of_wins_of_player_1 += 1
        print("Number of wins of Player 1: ", num_of_wins_of_player_1)
        print("Number of wins of Player 2: ", num_of_wins_of_player_2)

    return num_of_wins_of_player_1, num_of_wins_of_player_2

def new_game(num_of_wins_of_player_1, num_of_wins_of_player_2):
    while True:
        print("Wil you like to play another round?")
        flag = input("Choose \"Y\" or \"N\" to start or end the Game.")
        if flag == 'Y':
            os.system('cls')
            player_1()
        elif flag == "N":
            os.system('cls')
            Result(num_of_wins_of_player_1, num_of_wins_of_player_2)
            return
        
def Result(num_of_wins_of_player_1, num_of_wins_of_player_2):
    print("Number of rounds won by Player 1: ", num_of_wins_of_player_1)
    print("Number of rounds won by Player 2: ", num_of_wins_of_player_2)
    if num_of_wins_of_player_1 == num_of_wins_of_player_2:
        print("It's a Draw")
    elif num_of_wins_of_player_2 > num_of_wins_of_player_1:
        print("Player 2 Won the Game!!")
    else:
        print("Player 1 Won the Game!!")


Rules()

