import random
game = ["Rock" , "Paper" , "Scissors"]
Rock= "✊"
Paper = "🖐️"
Scissors = "✌️"
game_icons = { "Rock" : "✊", "Paper" : "🖐️", "Scissors" : "✌️" }

print("Welcome to the Rock, Paper, Scissors game:")
help = input("Press Enter to continue or type (Help) for the rules. ").capitalize()
if help == "Help":
  print("""\n.                           ******Rules******
                        1) You choose and the computer chooses
                        2) Rock smashes Scissors -> Rock wins
                        3) Scissors cut Paper -> Scissors win
                        4) Paper covers Rock -> Paper wins""")
  
user_choice = input("\n Enter your choice (Rock, Paper, Scissors): ").capitalize()

computer_choice = random.choice(game)

if user_choice not in game:
  print("Invalid choice. Please run the program again and choose Rock, Paper, or Scissors. ")
else:
    if user_choice == computer_choice:
        print(f"Equalized with computer \n You chose {game_icons[user_choice]} and the computer chose {game_icons[computer_choice]}")
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print(f"You chose {Rock} ")
            print(f"Computer chose {Scissors}")
            print("You win! Rock smashes Scissors")
        elif computer_choice == "Paper":
            print(f"You chose {Rock} ")
            print(f"Computer chose {Paper}")
            print("You Lose! Paper covers Rock")
    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            print(f"You chose {Scissors}")
            print(f"Computer chose {Paper}")
            print("You win! Scissors cut Paper")
        elif computer_choice == "Rock":
            print(f"You chose {Scissors}")
            print(f"Computer chose {Rock}")
            print("You Lose! Rock smashes Scissors")
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print(f"You chose {Paper}")
            print(f"Computer chose {Rock}")
            print("You win! Paper covers Rock")
        elif computer_choice == "Scissors":
            print(f"You chose {Paper}")
            print(f"Computer chose {Scissors}")
            print("You Lose! Scissors cut Paper")
