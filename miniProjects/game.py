import random


attempts = 0
my_score = 0
computer_score = 0

choices = ["kağıt", "taş", "makas"]

while attempts <= 5:
    random_choices = random.choice(choices)
    user_input = input("kağıt, taş or makas: ")

    if user_input == "kağıt" and random_choices == "makas":
        print("Computer choice: " + random_choices)
        print("computer won")
        computer_score += 1
    elif user_input == "taş" and random_choices == "kağıt":
        print("Computer choice: " + random_choices)
        print("computer won")
        computer_score += 1
    elif user_input == "makas" and random_choices == "taş":
        print("Computer choice: " + random_choices)
        print("computer won")
        computer_score += 1
    elif user_input == random_choices:
        print("Draw!!")
    else:
        print("Computer choice: " + random_choices)
        print("You won")
        my_score += 1


    attempts += 1


print(f"Your score is {my_score}")
print(f"computer score is {computer_score}")

if my_score > computer_score:
    print("You are the winner congrats")
else:
    print("Computer is the winner")
