import os
books = {}
def clear():
  os.system("cls") if os.name == "nt" else os.system("clear")

def Add_book():
  while True:
    clear()
    ISBN = int(input("Enter ISBN: "))
    title = input("Enter title: ")
    author = input("Enter author: ")
    books[ISBN] = {"Title":title, "Author":author, "Avaliable":True}
    print(f"Book {title} by {author} added to the catalog with ISBN {ISBN}")
    choice = input("Do you want to add another book? (y-n): ")
    if choice.lower() != "y":
      break
    elif choice.lower() == "y":
      continue

def BookCheckOut():
  while True:
   clear()
   ISBN = int(input("Enter ISBN to check out: "))
   if ISBN in books:
    if books[ISBN]["Avaliable"] == True:
      books[ISBN]["Avaliable"] = False
      print(f"Book'{books[ISBN]['Title']}' checked out")
    else:
      print(f"Book'{books[ISBN]['Title']}' os already checked out")
   else:
    print("Sorry! we don't have this ISBN in the catalog")  

   choice = input("Do you want to check out another book? (y-n): ")
   if choice.lower() != "y":
     break
   elif choice.lower() == "y":
     continue

def BookCheckIn():
  while True:
    clear()
    ISBN = int(input("Enter ISBN to check in: "))
    if ISBN in books:
      if books[ISBN]["Avaliable"] == False:
        books[ISBN]["Avaliable"] = True
        print(f"Book {books[ISBN]['Title']} checked in")
      else:
        print(f"Book {books[ISBN]['Title']} is in the catalog")  
    else:
      print("Sorry! we don't have this ISBN in the catalog")  

    choice = input("Do you want to check in another book? (y-n): ")
    if choice.lower() != "y":
      break
    elif choice.lower() == "y":
      continue

def list_books():
  while True:
    clear()
    print("\nLibrary catalog: ")
    for ISBN in books:
      book_info = books[ISBN]

      print(
        f"ISBN : {ISBN}, Title: {book_info['Title']}, Author : {book_info['Author']}, Avaliable : {book_info['Avaliable']}"
      )
    choice = input("Do you want to go back to the main menu? (y-n): ")
    if choice.lower() == "y":
      break
    elif choice.lower() != "y":
      continue
    
while True:
  print("""
  Menu:
  1. Add Book
  2. Check Out Book
  3. Check In Book
  4. List Books
  5. Exit
  """)
  choice = int(input("Enter your choice (1-5): "))

  if choice == 1:
    Add_book()

  elif choice == 2:
    BookCheckOut()

  elif choice == 3:
    BookCheckIn()

  elif choice == 4:
    list_books()

  elif choice == 5:
    print("Exiting the program...")
    break

  else:
    print("Invalid choice")
    continue