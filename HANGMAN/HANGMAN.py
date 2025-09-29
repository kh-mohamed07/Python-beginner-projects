import random
import string 
from words_list import words 

def get_valid_word(words):
    word=random.choice(words)
    while ' ' in word or '-' in word:
        word=random.choice(words)
    return word.upper()


def status_display(target_word, guessed_letters, lives):
        current_status=' '.join([letter if letter in guessed_letters else '_' for letter in target_word])
        print(f'Word: {current_status} \nlives left: {lives} \nguessed_letters:{' '.join(guessed_letters)} ')

def hangman():
    target_word=get_valid_word(words)
    target_word_letters=set(target_word)
    alphabet=set(string.ascii_uppercase)
    guessed_letters=set()
    lives=6
    while lives>0 and len(target_word_letters)>0:
        status_display(target_word, guessed_letters, lives)
        user_guess=input('\nGuess a letter: ').upper()
        if user_guess in alphabet - guessed_letters:
            guessed_letters.add(user_guess)
            if user_guess in target_word_letters:
                target_word_letters.remove(user_guess)
                print('Nice guess,correct \n')
            else: 
                lives=lives-1
                print('False, the letter u just guessed is not in the target word \n')
        elif user_guess in guessed_letters:
            print('try again , you already guess this letter \n')
        else :
            print('invalid character!! \n')
    if lives==0:
        print('You lost the game')

    elif len(target_word_letters)==0:
        print('Congrats!! YOU WON 🎉')
    print(f'the word is: {target_word}')

again='yes'
while again.lower()=='yes':
    hangman()
    while True:
        again=input('do u want to play again? (yes or no) ')
        if again.lower() in ('yes' , 'no'):
            break
        else: 
            print("please answer by 'yes' or 'no' ")
            







    