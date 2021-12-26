import random
from hangman_arts import logo, stages
from hangman_words import word_list
#uisng python random module to choose a random word from list
final_word = random.choice(word_list)
dash = []
lives = 6
print(logo)
#creating a for loop and checking the length of final_word and genrating _ according to number of words choosen randomly
for l in range(0, len(final_word)):
    dash.append("_")
print(f"{' '.join(dash)}")

game_end = False
#creating a while loop taking input of user and checking length of final_word and replacing position of that word with _
while not game_end:
    guess = input("Guess a letter:").lower()

    if guess in final_word:
        print(f"You've already guessed {guess}")

    for position in range(0, len(final_word)):
        letter = final_word[position]
        if letter == guess:
            dash[position] = letter
    if guess not in final_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(stages[lives])
    #checking that our input word is not there then sub -1 from lives
    if guess not in final_word:
        lives -= 1
        if lives == 0:
            game_end = True
            print("Sus child saftey warning !!!!!! dangerous content ahead you just killed someone")
    print(f"{' '.join(dash)}")
    # checking if _ is not there in dash then changing game_end to true and displaying  you win
    if "_" not in dash:
        game_end = True
        print("you win")
