from hangman_word_selections import words
import random

# Chose word, defining variable
word = random.choice(words)
lives = 0

print("Let's play hangman")

letter_in_word_list = []
letter_used_list = []
display = [letter if letter in letter_used_list else '- ' for letter in word]

# creates a list of the letters in the word selected
for letter in word:
   letter_in_word_list.append(letter)

# while the player has less than 7 incorrect guesses,
while lives < 7:
    print('\n' + 'Remaining guesses: ' + str((7 - int(lives))))
    print('Letters used: ', ' '.join(letter_used_list))
    print("Current word: ", ' '.join(display))
    guess = input('Guess a letter: ')
    if guess in letter_used_list:
        print('You already guessed that letter')
    elif guess in letter_in_word_list:
        letter_used_list.append(guess)
        display = [letter if letter in letter_used_list else '- ' for letter in word]
        if '- ' in display:
            continue
        else:
            print('You Win! The word was: ' + word)
            break
    else:
        letter_used_list.append(guess)
        lives += 1
        if lives == 7:
            print('You lose! The word was: ' + word)
