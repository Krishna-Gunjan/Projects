while True:
    try:
        my_string = input("Enter your string: ")
        reversed_string = my_string[::-1]
        print("The reversed string will be", reversed_string)
        break
    except:
        print("Invalid Input! Please input a valid string.")