contacts = {}
while True:
  print("Contacts manegment \n")
  print("1-Add a contact")
  print("2-View contacts")
  print("3-Edit contact")
  print("4-Exit")
  user_choice = input("Please choose a number from 1-4: ")

  if user_choice == "1":
    contact_id = input("Enter the contact ID: ")
    contact_name = input("Please type a name: ")
    while True:
      contact_phone = input("Please type a phone number: ")
      if contact_phone.isdigit():
           break
      else:
        contact_phone = input("Please type a phone number: ")
    contacts[contact_id] = {
      "name":contact_name,
      "phone":contact_phone,
    }

    print(f"\n \n {contact_name} was added successfully... \n \n ")
  elif user_choice == "2":
    print(contacts)
  elif user_choice == "3":
    id_to_edit = input("Please enter an ID to edit: ")
    if id_to_edit in contacts:
      new_name = input("Enter a new name:  ")
      new_phone = input("Wnter a new phone: ")
      while True:
        if new_phone.isdigit():
             break
        else:
          new_phone = input("Wnter a new phone: ")
      contacts[id_to_edit] = {
        "name":new_name,
        "phone":new_phone
      }
      print("\n success... \n")
    else:
      print(f"Sorry, {id_to_edit} was not found.... \n")
  elif user_choice == "4":
    print("ok")
    break
  else:
    print("Invalid choice! ")