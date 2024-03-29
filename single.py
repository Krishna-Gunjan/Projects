import os
import random

def Rules():
    print("""You have chosen to play single player mode. The Rules are:
                1. You have to choose from one of the following
                        Stone / Paper / Scissor
                2. You can choose when to end the game.
                3. At the end, player with most wins wins the game.""")
    while True:
        flag = input("Enter \"start\" or \"end\" to start or end the game: ")
        if flag == "start":
            break
        os.system('cls')
    hand = choose()
    my_hand = computer()
    num_of_win_of_player, num_of_win_of_computer = score_board(hand, my_hand)
    new_game(num_of_win_of_player, num_of_win_of_computer)
    
def choose():
    while True:
        hand = input("Choose your hand(Stone/Paper/Scissor): ")
        if hand == "Stone" or hand == "Paper" or hand == "Scissor":
            break
        else:
            os.system('cls')
            print("Oops! seems you made an error. Try Again")
    return hand

def computer():
    possible_hand = ["Stone", "Paper", "Scissor"]
    my_hand = random.choice(possible_hand)
    return my_hand

num_of_win_of_player = 0
num_of_win_of_computer = 0

def score_board(hand, my_hand):
    global num_of_win_of_computer, num_of_win_of_player
    possible_wins = {
                "Stone" : "Scissor",
                "Scissor" : "Paper",
                "Paper" : "Stone"
                }
                
    if hand == my_hand:
        print("It's a tie")
        print("Your hand: " + hand)
        print("Computer's hand: " + my_hand)
    else:
        if possible_wins[hand] == my_hand:
            num_of_win_of_player += 1
            os.system('cls')
            print(" Number of Wins of Player: ", num_of_win_of_player)
        else:
            num_of_win_of_computer += 1
            os.system('cls')
            print("Number of Wins of Computer: ", num_of_win_of_computer)
            
    return num_of_win_of_player, num_of_win_of_computer

def new_game(num_of_win_of_player, num_of_win_of_computer):
    print("Will you like to play another round?")
    while True:
        flag = input("Enter \"Y\" or \"N\" to play another game or end it: ")
        if flag == "Y":
            os.system('cls')
            choose()
        elif flag == "N":
            os.system('cls')
            Result(num_of_win_of_player, num_of_win_of_computer)
            return

def Result(num_of_win_of_player, num_of_win_of_computer):
    print("Number of games won by the player: ", num_of_win_of_player)
    print("Number of games won by the computer: ", num_of_win_of_computer)
    if num_of_win_of_player == num_of_win_of_computer:
        print("It's a Tie")
    elif num_of_win_of_computer > num_of_win_of_player:
        print("Computer Wins!")
    else:
        print("Player Wins!")
    
Rules()