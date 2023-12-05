import random
from Art import logo

end_game = False

user_guess = []
def num():
    return random.randint(1,100)

num_chosen = num()
number_attempts = 0

def guess():
    global number_attempts ,end_game
    number = int(input("Make a guess : "))
    user_guess.append(number)
    number_attempts  += 1

    if number > num_chosen:
        print("Too high.\n Guess again.")
    elif number < num_chosen:
        print("To low.\n Guess again.")
    else:
       end_game = True
       print(f"Congratulations! You guessed the number {num_chosen} in {number_attempts } attempts.")
       
        
           
hard_length = 5
easy_length = 10

print(logo)   
print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100\n")

mode = input("Choose a difficulty\nType 'easy' or 'hard': ")
if mode == 'hard':
    print(f"You have {hard_length} attempt remaining to guess the number.")
    guess()
    while number_attempts  < hard_length:
        guess()
        print(f"You have {hard_length - number_attempts } attempt remaining to guess the number.")
    else:
        print(f"You've run out of attempts. The correct number was {num_chosen}.")
elif mode == 'easy':
    print(f"You have {easy_length} attempt remaining to guess the number.")
    guess()
    while number_attempts  < easy_length:
        guess()
        print(f"You have {easy_length - number_attempts } attempt remaining to guess the number.")
    else:
        print(f"You've run out of attempts. The correct number was {num_chosen}.")
    