import random

highest =10

answer = random.randint(1,highest)
print(answer) #TODO : Remove after testing
print("Please guess a number between 1 and {} : ".format(highest))
guess = int(input())



if guess == answer:
    print("Wow! You got it first time!")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Yay! You've guessed it right!")
    else:
        print("Sorry, you've not guessed correctly")
elif guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Yay! You've guessed it right!")
    else :
        print("Sorry, you've not guessed correctly")
else :
    print("Try again")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Yay! You've guessed it right!")
#     else:
#         print("Try again")
# elif guess > answer:
#     print("Please guess lower")
#     if guess == answer:
#         print("Yay! You've guessed it right!")
#     else:
#         print("Try again")
# else:
#     print("Wow! You got it first time!")