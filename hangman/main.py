"""
This project is to create a hangman game.
"""
import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

# create a list containing "_" 
display = []
for _ in range(word_length):
    display.append("_")

while not end_of_game:
    guess = input("Please guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed '{guess}'")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that is not in the word.\nYou have {lives} lives left.")
        if lives == 0:
            end_of_game =True
            print("You loss!")

    if "_" not in display:
        end_of_game = True
        print("You Win!")
    
    print(stages[lives])


    







