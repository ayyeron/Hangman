import random
from words import words
import string
from images import lives_visual_dict
words = ["Kwantlen", "Rai", "Zimmerman", "statue", "iceberg", "Trip", "Food", "egg", "bacon", "Water", "Snow", "Rain", "Trouble", "Dog", "Cat", "bird", "Monster", "Trust", "Try", "Balcony", "Twist", "Drink", "Type", "Orange", "Market",  ]

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word or 'Kwantlen' in word or 'Rai' in word or 'Zimmerman' in word:
        word = random.choice(words)


    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    live = 6

    while len(word_letters) > 0 and live > 0:
        print('you now have',  live, 'lives left and you have used this letters: ', ' '.join(used_letters))

        word_list = [ letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[live])
        print('Your current Word: ', ' '.join(word_list))

        user_letter = input('guess a letter: ').upper()
        import time
        time.sleep(1)
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                live = live - 1
                print(lives_visual_dict[live])

                print(" Letter is not in the word, so im going to steal one of your lives away hehe.")    

        elif user_letter in used_letters:
            print("you are already picked that dummy. PICK AGAIn BUT NOT THE SAME LETTER PLEASE")

        else:
            print("THAT CHARACTER DOES NOT EXIST SMH.")

    if live == 0:
        print(lives_visual_dict[live])
        print('you deadd sorry bozo, the word was', word)
        print(' Bet you wont play again hehee', '!!')
    else:
        print(' YOU GOT IT RIGHT OMG GOOD 4 U, The word was', word, '!!')
        print(' Bet you wont play again hehee', '!!')

user_input = input("Enter your name: ")
print(user_input)

hangman()