import random

options = ("rock", "paper", "scissor")

is_running = True

while is_running:
    
    computer = random.choice(options)
    player = None
    
    while player not in options:
        player = input("Enter your choice: (rock, paper, scissor): ")
        
    if player == computer:
        print("It's a tie")
    elif player == "paper" and computer == "rock":
        print("You win!!!")
    elif player == "rock" and computer == "scissors":
        print("You win!!!")  
    elif player == "scissors" and computer == "paper":
        print("You win!!!") 
    else:
        print("you lose!!!")

    print(f"Your Choice:       {player}")
    print(f"Computer's Choice: {computer}")   
         
    if not input("Play Again? (y/n): ").lower() == "y":
        is_running = False
            