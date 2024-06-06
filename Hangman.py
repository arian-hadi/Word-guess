import random
from Words import words
import string
def get_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives = 6

    while len(word_letter) > 0 and lives > 0:
        print("The letters you have guessed: ", " " .join(used_letter))
        print(f"You have {lives} lives left")
        word_list = [letter if letter in used_letter else "_" for letter in word]
        print("The word is ", " ".join(word_list))
        input_letter = input("Type in a letter: ").upper()
        if input_letter in alphabet - used_letter:
            used_letter.add(input_letter)
            if input_letter in word_letter:
                word_letter.remove(input_letter)
            elif input_letter not in word_letter:
                lives = lives - 1
                print("The word was incorrect!")
        elif input_letter in used_letter:
            print("You have already guessed that letter".upper())
        else:
            print("You typed in an invalid character".upper())
    if lives > 0:
        print(f"Yay the word was {word}")
    else:
        print(f"You lost:( The word was {word}")
hangman()