#! /usr/local/bin/python3
import random
import string


file = open ('words.txt')
text = file.read().split()
# print(text)
file.close()

easy_level = [ 
    word.upper()
    for word in text
    if 4 <= len(word) <= 6
]

normal_level = [ 
    word.upper()
    for word in text
    if 6 <= len(word) <= 8
]

hard_level = [ 
    word.upper()
    for word in text
    if 8 <= len(word)
]

guesses = []

def get_difficulty():
    difficulty = input('\nPlease select a difficulty (e - easy, n - normal, h - hard):')
    if difficulty == 'e':
        word = random.choice(easy_level)
    elif difficulty == 'n':
        word = random.choice(normal_level)
    elif difficulty == 'h':
        word = random.choice(hard_level)
    else:
        return get_difficulty()
    print(f'\nYour random word is {len(word)} characters long.')
    return word

def get_guess_list(guess_list):
    guess = input('Guess a letter:').upper()
    if len(guess) != 1:
        print('Please guess only a SINGLE letter')
    else:
        guess_list.append(guess)
    return guess_list


def display_word(word, guess_list):
    return [letter if letter in guess_list else '_' for letter in word]

def wrong_guess_set(word, guess_list):
    return sorted(set(
        letter
        for letter in guess_list
        if not letter in word
    ))

def game_play(word):
    guess_list = []
    while True:
        guesses_remaining = 8 - len(wrong_guess_set(word, guess_list))
        print(f"\nIncorrect letters: {' '.join(wrong_guess_set(word, guess_list))}")
        print(f"Mystery Word: {' '.join(display_word(word, guess_list))}")
        print(f"You have {guesses_remaining} guesses remaining.")
        if "_" not in display_word(word, guess_list):
            print(f'\nCongratulations! You\'ve won! Your word was {word}\n')
            play_again()
            return
        if guesses_remaining == 0:
            print(f'\nGAME OVER, Your word was {word}\n')
            play_again()
            return
        guess_list = get_guess_list(guess_list)


def play_again():
    if input('Would you like to play again? (y/n):') == 'y':
        new_word = get_difficulty()
        game_play(new_word)
    return


if __name__ == '__main__':
    word = (get_difficulty())
    game_play(word)





# # Global constraints
# NUM_TURNS = 8
# CURRENT_USER_TURN = 0

# def filtered_by_difficulty(words, desired_difficulty):


# def get_word_to_guess(desired_difficulty):
# words = read_words(WORDS_FILE)
# filtered = filter_by_difficulty(words, desired_difficulty)
# return choice(filtered)

# def goalWord():
#     with open("words.txt","r") as allWords:
#         wordList = allWords.read()
#         wordList = wordList.split()
#         easy_words = [
#             for word in wordList:
#             if 4 <= len(word) <= 6
#                 easy_words.append(word.upper())
#             return random.choice(easyWords)
#         ]
#         normal_words = [
#         for word in wordList:
#             if 6 <= len(word) <= 8
#                 normal_words.append(word.upper())
#         return random.choice(normalWords)
#         ]
#         hard_words = [
#         for word in wordList:
#             if 8 <= len(word)
#         return random.choice(hard.upper())
#         ]




