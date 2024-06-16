import random

def choose_word():
    words = ["cat","dog","car","programing","code ","python","laptop","word","phone","papaya"]
    return random.choice(words)
# the above is to choose a random word from the given list of words to be used in the game
def word_status(word,guessed_letters):
    display =""
    for letter in word :
        if letter in guessed_letters:
            display+=letter
        else:
            display+="_"
    return display
# this funcition is to returthe corectly geussed words as them self and the incorectly guessed words as un underscore
def word_guessing_game():
    secret_word=choose_word()# to pass the word chosen from the above choose_word function
    guessed_letters =[]#this is empty because at the start of the game the gused words 0
    attempts=7 # to track the number of attempts we have left

    print("word guessing game")
    print("******************")
    print("secret word :",word_status(secret_word,guessed_letters))
 
    while attempts > 0 :
        guess =input("guess a letter: ").lower()#to make all the words entered lower

        if len(guess) != 1 or not guess.isalpha():#to make sure the word enter is only one and make sure the player only enters alphabeths
            print("you must enter a single letter")
            continue
        if guess in guessed_letters :
            print("you already guessed that letter")#to make sure the word is only gussed one time
            continue
        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(f"no letter '{guess}'occurs in the word")
            print(f"you have{attempts} attempts remaining")
        else:
            occurences=secret_word.count(guess)
            print(f"letter'{guess}'occurs {occurences} times")

        current_status = word_status(secret_word,guessed_letters)
        print("secret word:",current_status)#checking current progress

        if "_" not in current_status:
            print("congrtulations ! yoy guessed thhe word")
            break

    if "_" in current_status :
        print("you ran out of attempts the word was{secret_word}")


word_guessing_game()



