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
    used_letters = list()
    word = get_valid_word(words)
    printed_word = ["-" for i in word]
    length = len(word)
    letter = input("Lütfen harf giriniz:").upper()
    printed_word =["-" for i in word]
    if letter in alphabet:
        print("Harf alfabenin içinde\n")
        while "-" in printed_word:
            print("Döngüdeyiz\n")
            used_letters.append(letter)

            printed_word = [letter if letter == i else "-" for i in word]
            print(word)
            print(letter, "\n")
            print(used_letters)
            letter = input("Lütfen harf giriniz:").upper()

    else:
        print("Invalid syntax")
        hangman()
hangman()