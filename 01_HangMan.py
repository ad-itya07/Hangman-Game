import random
from HangManPICS import HANGMANPICS
from HangManLogo import HANGMANLOGO

print(HANGMANLOGO)
word_list = ["ardvark" , 'baboon' , 'camel' , 'apple' , 'boots' , 'Centipede']

rand_word  = random.choice(word_list)

ans_list = ['_' for i in range(len(rand_word))]
print(ans_list)
print(HANGMANPICS[0])

word_guess = 0
man_life = 0

while (man_life<7):
    guess = input("Guess a letter: ").lower()

    if guess in rand_word:
        for i in range(len(rand_word)):
            letter = rand_word[i]
            if guess == letter:
                ans_list[i] = guess
                word_guess+=1
    
    else:
        man_life+=1

    print(HANGMANPICS[man_life])
    print(f"{''.join(ans_list)}")
    print("")

    if (man_life==6):
        print("Game Over")
        break

    elif (word_guess==len(rand_word)):
        print("You Won")
        break
      

