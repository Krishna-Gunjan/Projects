from getpass import getpass
import os

def Rules():
    print("""Hello There!, Welcome to a game of Hangman. Without further waiting, let's start with the rules:
                1. This is a two-player game
                2. The first player will provide a word with an adequate hint.
                3. The second player has to guess what the word is
                4. A maximum of 6 guesses will be given
                5. Invalid Inputs don't count as a guess
                6. Have Fun  
            """)
    ask = ''
    while ask != "start":
        ask = input("Enter \"start\" when you are ready: ")
    word_to_guess, hint, word_to_display, list_of_word = first_person()
    second_person(word_to_guess, hint, word_to_display, list_of_word)

def first_person():
    word_to_guess = getpass("Enter the word to guess: ")
    print("=====================================================================================================================")
    word_to_display = ["*"] * len(word_to_guess)
    list_of_word = list(word_to_guess)
    print("=====================================================================================================================")
    hint = input("Enter the hint for the word to guess: ")
    os.system('cls')
    return word_to_guess, hint, word_to_display, list_of_word

def second_person(word_to_guess, hint, word_to_display, list_of_word):
    guesses = 0
    guess = ''
    while guess != word_to_guess and guesses < 6:
        print("Length of word to guess: ", len(word_to_guess))
        print("The hint given: ", hint)
        guess = input("Enter your guess: ")
        for i in guess:
            if i not in list_of_word:
                guesses += 1
            while i in list_of_word:
                index = list_of_word.index(i)
                word_to_display[index] = list_of_word[index]
                list_of_word[index] = ' '
            os.system('cls')
            print(''.join(word_to_display))
            print("number of guesses left", 6 - guesses)
        if word_to_display == list(word_to_guess):
            print("You Won! You guessed the word:", ''.join(word_to_display))
            break
    if guesses == 6:
        print("You Lose! The word was:", word_to_guess)

Rules()