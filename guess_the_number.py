import random

print("-------------------------------------------------------------------------")
print("-----------------------Python Number Guessing Game-----------------------")
print("-------------------------------------------------------------------------")

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)
guess = None

is_running = True

guesses = 0

while is_running:
    guess = input(f"Enter a number between {lowest_num} and {highest_num}: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
           print(f"Invalid Guess!!! Please enter a number between {lowest_num} and {highest_num}") 
        elif guess > answer:
            print("Too high!!! Try Again!")
        elif guess < answer:
            print("Too low!!! Try Again!")
        else:
            print(f"You've guessed the correct Answer!!!")
            print(f"Correct answer was: {answer}")
            print(f"No. of guesses taken to find the correct answer: {guesses}")
            is_running = False
    else:
        print(f"Invalid Choice!!! Please enter a number between {lowest_num} and {highest_num}")
        
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")