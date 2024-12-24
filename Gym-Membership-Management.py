import os
import time

def clear_sceen():
  os.system('cls' if os.name == 'nt' else 'clear')

class Member:
  def __init__(self, first_name, last_name, ID, status):
    self.first_name = first_name
    self.last_name = last_name
    self.ID = ID
    self.status = status

  def display_members(self):
    print(f"First name: {self.first_name}")
    print(f"Last name: {self.last_name}")
    print(f"Membership ID: {self.ID}")
    print(f"Membership Status: {self.status}")

def create_member():
  first_name = input("Enter first name: ")
  last_name = input("Enter last name: ")
  ID = input("Enter membership ID: ")
  status = input("Enter membership status, Or click enter: ")
  if status == "active":
    status = "active"
  else:
    status = "inactive"

  return Member(first_name, last_name, ID, status)

new_members = []
while True:
  print("Welcome to Gym Membership Managment\n\n\n")
  print("Choose an Action:\n\n1. Add new member\n2. Display all members\n3. Search for a member\n4. Exit\n\n")
  choice = input("Enter your choice: ")
  if choice == "1":
    clear_sceen()
    time.sleep(2)
    new_members.append(create_member())
    print("Member added successfully!")
    
  elif choice == "2":
    clear_sceen()
    time.sleep(2)
    if new_members:
      time.sleep(1)
      print(f"Displaying all members....\n")
      for i in new_members:
        i.display_members()
        print("_" * 20)
      time.sleep(2)
    else:
      print("Sorry, didn't find any members to display...")
      time.sleep(3)
      clear_sceen()

  elif choice == "3":
    clear_sceen()
    print("Search by:\n\n1. Membership ID\n2. First Name\n3. Membership Status\n\n")
    searching_choice = input("Enter your choice: ")
    if searching_choice == "1":
      ID_search = input("Enter the membership ID to search: ")
      not_found = True
      for i in new_members:
        if i.ID == ID_search:
          time.sleep(2)
          clear_sceen()
          print("\nMember/s is/are found:")
          i.display_members()
          print("_" * 20)
          not_found = False
      if not_found:
        print("Sorry, didn't find any member with that ID...")
        time.sleep(3)
    elif searching_choice == "2":
      first_name_search = input("Enter the first name to search: ")
      not_found = True
      for i in new_members:
        if i.first_name == first_name_search:
          time.sleep(2)
          print("\nMember/s is/are found:")
          i.display_members()
          print("_" * 20)
          not_found = False

      if not_found:
        print("Sorry, didn't find any member with that name...")
        time.sleep(3)
    elif searching_choice == "3":
      status_search = input("Enter the membership status to search (active/inactive): ")
      not_found = True
      for i in new_members:
        if i.status == status_search:
          time.sleep(2)
          print("\nMember/s is/are found:")
          i.display_members()
          print("_" * 20)
          not_found = False
      if not_found:
          print("Sorry, didn't find any member with that status...")
          time.sleep(3)
    else:
      print("Invalid choice... Please try again...")
      time.sleep(2)
      clear_sceen()

  elif choice == "4":
    print("Exiting...")
    time.sleep(5)
    break
  else:
    print("Invalid choice... Please try again...")
    time.sleep(2)
    clear_sceen()    