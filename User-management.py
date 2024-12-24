import os
import time

def clear_sceen():
  os.system('cls' if os.name == 'nt' else 'clear')

class User:
  def __init__(self, first_name, last_name, email, password, status="inactive"):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.password = password
    self.status = status

  def display_users(self):
    time.sleep(2)
    print(f"First name: {self.first_name}")
    print(f"Last name: {self.last_name}")
    print(f"Email: {self.email}")
    print(f"Password: {self.password}\n")
    
  
def create_user():
  first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")
  email = input("Enter your email: ")
  password = input("Enter your password: ")
  return User(first_name, last_name, email, password)

new_users = []
while True:
  print("Welcome to 'User Manegment'!\n\n")
  print("Choose an action: \n")
  print("1: Add new user.\n2: Display all users. \n3: Exit.\n")
  
  user_choice = input("Enter your choice: ")
  
  if user_choice == "1":
    clear_sceen()
    new_users.append(create_user())
    print("User addedd successfully! ")
    time.sleep(2)
  elif user_choice == "2":
    clear_sceen()
    if new_users:
      print("Displaying all users......")
      time.sleep(1)
      for i in new_users:
        i.display_users()
        print("\n___________________________\n")
      time.sleep(2)
    else:
      print("Sorry, didn't find any user to display!")
      time.sleep(3)
  elif user_choice == "3":
    print("Exiting...")
    time.sleep(4)
    break
  else:
    print("Invalid choice! Please try again.")
  
  