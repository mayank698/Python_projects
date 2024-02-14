import random

list1 = ['', '', '']
list2 = ['', '', '']
list3 = ['', '', '']

map = [list1, list2, list3]
position = input("Enter where you want to hide the treasure: ")
# B3
letter = position[0].lower()
# B 
abc = ['a', 'b', 'c']
letter_index = abc.index(letter)
# 1
number_index = int(position[1])-1
# 3-1 = 2 
map[number_index][letter_index] = 'X'
# map[2][1] 
print(f"{list1}\n{list2}\n{list3}")
