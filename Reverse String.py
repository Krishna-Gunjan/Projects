while True:
    try:
        a = input("Enter your string: ")
        break
    except:
        print("Invalid Input! Please input a valid string.")
try:
    print("The reversed string value will be " + a[::-1])
except:
    print("The string cannot be reversed.")
    while True:
        try:
            a = input("Enter your string: ")
            try:
                print("The reversed string value will be " + a[::-1])
            except:
                print("The string cannot be converted")
        except:
            print("Invalid Value! Please input aa valid value.")
