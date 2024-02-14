size = input("Enter the size of your pizza: ")
peproni = input("Do you want peproni on your pizza: ")
cheese = input("Do you want some extra cheese: ")
bill = 0

if size == "S":
    bill += 120

elif size == "M":
    bill += 140

elif size == "L":
    bill += 160

if peproni == "Y":
    bill += 20

if cheese == "Y":
    bill += 40

print(f"Your final bill is: {bill}")
