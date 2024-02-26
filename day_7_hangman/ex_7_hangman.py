import random

word_list = ['banana', 'apple', 'orange', 'watermelon', 'avocado']

# pick a word
word = random.choice(word_list)
blanks = ['_'] * len(word)
print(blanks)

lives_lost = 0
while lives_lost < 7:
    guessed_letter = input("Guess a letter: ")
    if guessed_letter in word:
        for i,l in enumerate(word):
            if l == guessed_letter:
                blanks[i] = l
        
        print(blanks)
        
        if '_' not in blanks:
            print("You won")
            break
    else:
        lives_lost += 1
        print("lives lost: ", lives_lost)
else:
    print("You lost")