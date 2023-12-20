import subprocess
import os
from getpass import getpass

def game_mode():
    mode = ''
    while True:
        mode = input("""Please Choose a game mode to play: 
                            1. Enter "single" for single player
                            2. Enter "double" for two player
                     Game mode to play: """)
        os.system("cls")
        if mode == 'single' or mode == 'double':
            break

    if mode == 'single':
        subprocess.run(["python",  r"D:\Krishna\Projects\Beginner\Guess the Number.py"])

    else:
        Rules()

def Rules():
    print(""" THE RULES:
                    1. You can guess as many time as you want
                    2. After each incorrect guess a hint will be given
                    3. The lower the numbers of guesses you took, the better
                    4. The guess will always be in the range of start and end
                    5. Invalid value for guess will not afftect the score
                    6. After each game your position as the guesser will swap
                    7. If you choose to replay, please keep in mind that instead of your scoreboard, the opponents scoreboard will be updated
          """)
    while True:
        flag = input("Enter \" start \" to play: ")
        os.system("cls")
        if flag == "start":
            break
    
    os.system('cls')

    num_to_guess = first_player()
    guesses, lower_limit, upper_limit = second_player(num_to_guess)
    result(guesses, lower_limit, upper_limit, num_to_guess)
    player_1, player_2 = score_board(guesses)
    new_game(player_1, player_2)

def first_player():
    print("You are the First player. Your role is to provide a number which the second player has to guess.")

    while True:
        try:
            print("To maintain secrecy, the number given will not be shown on the terminal")
            num_to_guess = int(getpass("Enter the number to guess: "))
            break
        except:
            os.system('cls')
            print("Invalid Input! Please enter a valid integar value.")

    return num_to_guess
def second_player(num_to_guess):
    lower_limit = num_to_guess - 10
    upper_limit = num_to_guess + 10
    guesses = 0
    print("You are the second player. Your job is to guess the number given by the second player.")
    print("The number given lies between the range", lower_limit, "to", upper_limit)

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses += 1
            os.system('cls')
            if guess == num_to_guess:
                os.system('cls')
                break
            else:
                os.system('cls')
                print("Wrong Guess, Try Again!")

        except:
            os.system("cls")
            print("Invalid Input! Please enter a valid integar value.")
    
    return guesses, lower_limit, upper_limit

def result(guesses, lower_limit, upper_limit, num_to_guess):
    print("You Win! Let's take a look at your performance")
    print("Number of Guesses =", guesses)
    print("Number to Guess  =", num_to_guess)
    if guesses == upper_limit - lower_limit:
        print("It took you all the possible answers to win, worthy of an F")
    elif guesses > upper_limit - lower_limit:
        print("How did you even manage that, I am speechless")
    elif guesses < upper_limit - lower_limit:
        if guesses == 1:
            print("Luck or skill, who knows but what I know is the performance is worth an A")
        elif guesses <= (upper_limit - lower_limit)//2:
            print("An average performance, but you know what else is an averange, a B!")
        elif guesses >= (upper_limit - lower_limit)//2:
            print("Took you long enough, at most a C.")

player_1 = []
player_2 = []
num_of_games = 1

def score_board(guesses):
    global num_of_games

    if num_of_games%2 == 0:
        player_2.append(guesses)
    else:
        player_1.append(guesses)
        
    num_of_games += 1

    return player_1, player_2

def winner(player_1, player_2):
    max_score_for_player_1 = max(player_1)
    max_score_for_player_2 = max(player_2)

    if max_score_for_player_1 > max_score_for_player_2:
        print("Winner is Player 2")
    else:
        print("Winner is Player 1")

def new_game(player_1, player_2):
    while True:
        try:
            print("Will you like to play another game")
            flag = input("Enter \" yes \" or \" no \": ")
        except:
            os.system('cls')
            print("Invalid Input! Please answer with \"yes\" or \" no \" only")
        else:
            if flag == "yes":
                Rules()
                break
            elif flag == "no":
                winner(player_1, player_2)
                break

game_mode()