import random


exit=False
user_points=0
computer_points=0

while exit == False:
    options=["rock","paper","scissor"]
    user_input=input("Choose rock paper or scissors:")
    computer_input=random.choice(options)

    if user_input == "exit":
        print("game ended")
        print("you won a total score of"+str(user_points)+"and the computer total score is"+str(computer_points))
        exit=True

    if user_input == "rock":
          if computer_input == "rock":
            print("your input is rock")
            print("computer input is rock")
            print("it is tie!")
          elif computer_input == "paper":
            print("your input is rock")
            print("computer input is paper")
            print("computer wins!")
            computer_points +=1
          elif computer_input == "scissor":
            print("your input is rock")
            print("computer input is scissor")
            print("you wins!")
            user_points +=1
          elif user_input == "paper":
           if computer_input == "rock":
            print("your input is paper")
            print("computer input is rock")
            print("you wins!")
            user_points +=1
          elif computer_input == "paper":
            print("your input is paper")
            print("computer input is paper")
            print("it's a tie!")
          elif computer_input == "scissor":
            print("your input is paper")
            print("computer input is scissor")
            print("computer wins!")
            computer_points +=1

          elif user_input == "scissor":
           if computer_input == "rock":
            print("your input is scissor")
            print("computer input is rock")
            print("computer wins!")
            computer_points +=1
          elif computer_input == "paper":
            print("your input is scissor")
            print("computer input is paper")
            print("you wins!")
            user_points+=1
          elif computer_input == "scissor":
            print("your input is scissor")
            print("computer input is scissor")
            print("it's a tie!")
            
    elif user_input != "rock" or user_input != "paper" or user_input!= "scissor":
        print("Invalid input")

