students_height = input().split()
# print(students_height)

for x in range(0, len(students_height)):
    students_height[x] = int(students_height[x])

sum = 0
for n in students_height:
    sum += n
print(f"The total height is {sum}")

number_of_students = 0
for students in students_height:
    number_of_students += 1
print(f"Number of students is {number_of_students}")

average = round(sum/number_of_students)
print(f"The average is {average}")
