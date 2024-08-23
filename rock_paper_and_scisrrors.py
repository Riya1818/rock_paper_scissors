import random
print("welcome to rock, paper and scissors game")
print("press 0 for rock, 1 for paper and 2 for scissors")

choice=int(input("rock,paper or scissors?"))
computer_choice=random.randint(0,2)
if choice==0:
    print("you chose rock.")
    if computer_choice==0:
        print(f"the computer chose {computer_choice}.")
        print("draw")

    elif computer_choice==1:
        print(f"the computer chose {computer_choice}.")
        print("you lost.")

    else:
        print(f"the computer chose {computer_choice}.")
        print("you won.")

elif choice==0:
    print("you chose paper.")
    if computer_choice==0:
        print(f"the computer chose {computer_choice}.")
        print("you won")

    elif computer_choice==1:
        print(f"the computer chose {computer_choice}.")
        print("draw")

    else:
        print(f"the computer chose {computer_choice}.")
        print("you lost.")

else:
    print("you chose scissors.")
    if computer_choice==0:
        print(f"the computer chose {computer_choice}.")
        print("you lost")

    elif computer_choice==1:
        print(f"the computer chose {computer_choice}.")
        print("you won.")

    else:
        print(f"the computer chose {computer_choice}.")
        print("draw")
print("thanks for playing with us :)")