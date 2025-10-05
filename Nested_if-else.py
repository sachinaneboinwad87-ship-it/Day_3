# Nested if-else statement

number = int(input("Enter a number: "))

if number < 0:
    if number % 2 == 0:
        print("Number is negative and even")
    else:
        print("Number is negative and odd")
elif number == 0:
    print("Number is zero")
else:
    if number % 2 == 0:
        print("Number is positive and even")
    else:
        print("Number is positive and odd")