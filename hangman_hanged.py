import random
from words import words
import string
alphabet = "ABCDEFGHIJKLMNOPRSTUVYZXW"
def get_valid_word(words):
    word = random.choice(words) #ramdomly chooses something from list
    while "-" in word or " " in word:
        word = random.choice((words))
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    length = len(word)
    letter = input("Lütfen harf giriniz:").upper()
    printed_word =["-" for i in word]

    while len(word_letters) > 0:
        print("You have used these letters :", used_letters)


        word_list = [letter if letter in used_letters else "-" for letter in word]

        user_letter = input("guess a letter: ").upper()
        if user_letter in alphabet - used_letters :
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                print("\nYour letter,", user_letter, "is not in the word.")

        elif user_letter in used_letters:
            print("\nYou have already guessed that letter. Guess another letter.")
        else:
            print("That is not a valid letter.")
    print("You have found the word yuppi!!")
    print(word_list)
hangman()