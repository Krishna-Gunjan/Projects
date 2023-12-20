while True:
    try:
        a = int(input("Enter the first number: "))
        break
    except:
        print("Invalid Value! Please input a valid output.")

while True:
    try:
        b = int(input("Enter the second number: "))
        break
    except:
        print("Invalid Value! Please input a valid output.")

print("The following Arthimetic Function can be performed.")
print("=======================================================================")
print("The sum of both number:", a+b)
print("=======================================================================")
print("The diffrence of both number:", a-b)
print("=======================================================================")
print("The product of both number:", a*b)
print("=======================================================================")
try:
    print("The quotient of both number:", a/b)
except:
    print("The quotient of both numbers is undefined")
print("=======================================================================")
print("The first number raised to the power of the second number:", a**b)
print("=======================================================================")
try:
    print("The remainder of both number:", a%b)
except:
    print("The remainder of both numbers are undefined")
print("=======================================================================")
print("The root of both number:", a**1/2, b**1/2)