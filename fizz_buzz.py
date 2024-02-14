# divisble by 3 = fizz
# divisble by 5 = buzz
# divisble by 15 = fizzbuzz
target = int(input("Enter the last number: "))

for i in range(1, target+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
