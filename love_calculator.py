name1 = input("Enter the name: ")
name2 = input("Enter the name: ")
true_count = 0
love_count = 0

combined_names = name1+name2
lower_case = combined_names.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
# print(type(t))
first_digit = t+r+u+e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

second_digit = l+o+v+e
score = int(str(first_digit)+str(second_digit))
# Check score
if (score < 10) or (score > 90):
    print(f"Your score is {score}, stay away.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, good to go")
else:
    print(f"Your score is {score}")
