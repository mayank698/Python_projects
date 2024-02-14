import random
import os
from hangman_assets import word_list, logo, stages

print(logo)

selected_word = random.choice(word_list)
# print(selected_word)
dashes = []
n = len(selected_word)

for i in range(n):
    dashes += "_"

lives = 6

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in dashes:
        print(f"You already guessed the letter {guess}.")

    for position in range(n):
        letter = selected_word[position]
        if guess == letter:
            dashes[position] = letter

    if guess not in selected_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You loose.")
    print(' '.join(dashes))

    if "_" not in dashes:
        end_of_game = True
        print("You win.")
    
