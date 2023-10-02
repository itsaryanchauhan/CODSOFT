import random
choice = input("DO you want to play Rock, Paper, Scissors with me? Enter y for yes and n for no: ")

Options = ["rock", "paper", "scissors"]

while choice == "y":
    user = input("Choose Rock, Paper or Scissors: ")
    computer = random.choice(Options)

    if computer == "rock" and user == "paper":
        print("You WIn!")
    elif computer == "rock" and user == "scissors":
        print("You Lose!")
    elif computer == "paper" and user == "scissors":
        print("You Win!")
    elif computer == "paper" and user == "rock":
        print("You Lose!")
    elif computer == "scissors" and user == "rock":
        print("You Win!")
    elif computer == "scissors" and user == "paper":
        print("You Lose!")
    elif computer == user:
        print("Draw")
    print("You chose " + user + " while computer chose " + computer)
    choice = input("Do you want to play again? Enter y for yes and n for no: ")


print("Thanks FOr Playing!")


