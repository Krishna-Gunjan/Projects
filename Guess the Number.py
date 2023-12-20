import os
import subprocess

def game_mode():
    while True:
        print("""Welcome to Guess the Number. 
                1. Enter 'single' for single player
                2. Enter 'double' for double player
          """)
        mode = input("Select a game mode: ")
        if mode == "single" :
            os.system('cls')
            subprocess.run(["python", r"D:\Krishna\Projects\Beginner\Guess the Number\Guess the Number 1.py"])
            return
        elif mode == "double":
            os.system('cls')
            subprocess.run(["python", r"D:\Krishna\Projects\Beginner\Guess the Number\Guess the Number 2.py"])
            return
        os.system('cls')

game_mode()