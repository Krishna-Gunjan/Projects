import random

def restraints():
    
    print(""" THE RULES:
                    1. You can guess as many time as you want
                    2. After each incorrect guess a hint will be given
                    3. The lower the numbers of guesses you took, the better
                    4. The guess will always be in the range of start and end
                    5. Invalid value for guess will not afftect the score
          """)
    
    while True:
        try:
            start = int(input("Enter an integar value as the start point: "))
            end = int(input("Enter an integar value as the end point: "))
            break
        except:
            print("Invalid Value! Please input a valid integar value.")
    number_to_guess = random.randrange(start, end)
                
    guesses = 1
    while True:
        try:
            guess = int(input("Enter your guess: "))
            break
        except:
            print("Invalid Input! Please enter an valid integar value.")
            
            

    while guess != number_to_guess:
        if number_to_guess%guess == 0:
             print("A factor, didn't see that coming or did")
             guesses += 1
             while True:
                 try:
                     guess = int(input("Enter your guess: "))
                     break
                 except:
                     print("Invalid Input! Please enter an valid integar value.")


        elif guess > number_to_guess:
            print("A little to high, I guess")
            guesses += 1
            while True:
                try:
                    guess = int(input("Enter your guess: "))
                    break
                except:
                    print("Invalid Input! Please enter an valid integar value.")
        elif guess < number_to_guess:
             print("A little to low, I guess")
             guesses += 1
             while True:
                 try:
                     guess = int(input("Enter your guess: "))
                     break
                 except:
                     print("Invalid Input! Please enter an valid integar value.")

    print("You win!")
    print("Lets see how you did:", guesses)
    if guesses == end - start:
        print("It took you all the possible answers to win, worthy of an F")
    elif guesses > end - start:
        print("How did you even manage that, I am speechless")
    elif guesses < end - start:
        if guesses == 1:
            print("Luck or skill, who knows but what I know is the performance is worth an A")
        elif guesses <= (end - start)//2:
            print("An average performance, but you know what else is an averange, a B!")
        elif guesses >= (end - start)//2:
            print("Took you long enough, at most a C.")

                    
    
restraints()
