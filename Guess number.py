import random
import os

def clear_screan():
  os.system("cls") if os.name == "nt" else os.system("clear")
    
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
computer_choice = random.choice(numbers)
while True:
  clear_screan()
  user_choice = input("Please guess a number between 1 and 10: ")
  if user_choice == computer_choice:
    print("Congratulation! You gessed the correct number")
    break
  else:
    print("Wrong guess. Please try again")
    input("Press any key to continue...")