import random

rock = '''
  ____, O
   /   /M|
  /|MMMMMMMM
  {| | // |}
-_}| |/ \ |{_apx
'''

paper = '''
          __________
         |DAILY NEWS|
         |&&& ======|
         |=== ======|
         |=== == %%$|
         |[_] ======|
         |=== ===!##|
 ejm97   |__________|
'''

scissor = '''
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
'''

game_images = [rock, paper, scissor]
user_selects = int(input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSOR: "))

if user_selects >= 3 or user_selects < 0:
    print("Invalid choice. Try again!")
else:
    print(f"You choose: {game_images[user_selects]}")

    computer_choice = random.randint(0, 2)
    print(f"Computer choose: {game_images[computer_choice]}")

    if user_selects == 0 and computer_choice == 1:
        print("Computer wins.")
    elif user_selects == 0 and computer_choice == 2:
        print("You win.")
    elif user_selects == 1 and computer_choice == 0:
        print("You win.")
    elif user_selects == 1 and computer_choice == 2:
        print("Computer win.")
    elif user_selects == 2 and computer_choice == 0:
        print("Computer win.")
    elif user_selects == 2 and computer_choice == 1:
        print("You win.")
    else:
        print("It's a draw.")