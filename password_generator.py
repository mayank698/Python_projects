import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


nr_numbers = int(input("Enter number of numbers: "))
nr_symbols = int(input("Enter number of symbols: "))
nr_letters = int(input("Enter number of letters: "))

# Simple password
password = ""

for x in range(0, nr_numbers):
    password += random.choice(numbers)

for y in range(0, nr_symbols):
    password += random.choice(symbols)

for z in range(0, nr_letters):
    password += random.choice(letters)

# print(password)

# Hard password
password_list = []

for x in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for y in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for z in range(0, nr_letters):
    password_list.append(random.choice(letters))

# print(f"Before shuffle: {password_list}")
random.shuffle(password_list)
# print(f"After shuffle: {password_list}")

password1 = ""
for char in password_list:
    password1 += char
print(f"Your password is:{password1}")
