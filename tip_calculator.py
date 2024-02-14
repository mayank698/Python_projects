bill = int(input("Enter the bill: "))
percent = int(
    input("Enter the amount of tip you want to give in percent: "))
people = int(input("Enter no of persons to split the bill into: "))

percent_tip = (percent/100)*bill
# print(percent_tip)
new_bill = bill + percent_tip
# print(new_bill)
split_amount = round(new_bill/people, 2)
print(f"Each person should pay {split_amount} rupees")
