year = int(input("Enter any year: "))
# If any of the two condiitons is true it's a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Not a leap year.")
else:
    print("Not a leap year.")
