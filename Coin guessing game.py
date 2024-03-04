import random
print("Welcome to the Coin Guessing Game!")
print("choose a method to toss the coin:")

Method = input ("1. Using random.random()\n2. Using random.randint()\nEnter your choice (1 or 2):")
user_guess = input("Enter your guess (Heads or Tails):")
if Method =="1":
  random_number = random.random()
  if random_number < 0.5:
     computer_choice = "Heads"
  else:
     computer_choice = "Tails"
elif Method == "2":
  import random
  random_number = random.randint(0,1)
  if random_number == 0:
     computer_choice= "Heads"
  else:
     computer_choice = "Tails" 
else:
  print("Invalid choice. Please select 1 or 2.")
if user_guess.lower() == computer_choice.lower():
  print("Congratulations!You won!")
else:
  print("Sorry, you lost!")
  print(f"The computer choice was:{computer_choice}")
  
  
  
    


    
