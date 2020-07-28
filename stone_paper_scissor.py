import random

list = ['s', 'p', 'sicr']

chance = 5
no_of_chance = 0
computer_score = 0
your_score = 0

print("Stone, paper, scissor Game")

while no_of_chance < chance:
    user_input = input("s for stone \np for paper \nsicr for scissor \n Enter your choice:")
    choice = random.choice(list)

    if user_input == choice:
        print("Tie")

    if user_input == "s" and choice == "p":
        computer_score = computer_score + 1
        print(f"your guess {user_input} and computer guess is {choice} \n")
        print(f"computer score : {computer_score} \nyour score : {your_score} \n ")

    elif user_input == "s" and choice == "sicr":
        your_score = your_score + 1
        print(f"your guess {user_input} and computer guess is {choice} \n")
        print(f"computer score: {computer_score} \nyour score : {your_score} \n")

    elif user_input == "p" and choice == "s":
        your_score_score = your_score + 1
        print(f"your guess {user_input} and computer guess is {choice} \n")
        print(f"computer score : {computer_score} \nyour score : {your_score} \n ")

    elif user_input == "p" and choice == "sicr":
        computer_score_score = computer_score + 1
        print(f"your guess {user_input} and computer guess is {choice} \n")
        print(f"computer score : {computer_score} \nyour score : {your_score} \n")

    elif user_input == "sicr" and choice == "s":
        computer_score = computer_score + 1
        print(f"your guess {user_input} and computer guess is {choice} \n")
        print(f"computer score : {computer_score} \nyour score : {your_score} \n")

    elif user_input == "sicr" and choice == "p":
        your_score = your_score + 1
        print(f"your guess {user_input} and computer guess is {choice} \n")
        print(f"computer score : {computer_score} \nyour score : {your_score} \n ")

    no_of_chance = no_of_chance + 1

print("Game over")

if computer_score > your_score:
    print("you lose")

if computer_score < your_score:
    print("you won")

print(f"your score : {your_score} and computer score : {computer_score}")