weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight/(height*height)
print(bmi)
if bmi < 18:
    print("You are underweight.")
elif bmi < 25:
    print("You have normal weight.")
elif bmi > 28:
    print("You have slightly high bmi.")
