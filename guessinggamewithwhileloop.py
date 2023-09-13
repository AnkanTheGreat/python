import random
highest =10
answer = random.randint(1,highest)
print(answer)
guess = 0
print("Please guess a number between 1 and {} : ".format(highest))



while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("You've guessed it correctly")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else :
             print("Please guess lower")
