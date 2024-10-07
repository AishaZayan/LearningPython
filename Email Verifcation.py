import time

def Verify_email(email):
  if "@" in email and "." in email:
    return True
  else:
    return False
    
    

def user_name_email(name, email):
  if Verify_email(email) == True:
    print(f"User {name} with email {email} was successfully added!")
  else:
    print(f"Invalid email format for user {name}. Registration failed")

user_name = input("Enter a user name: ")
email = input("Enter your email: ")
print("Checking user name....please wait")
time.sleep(3)
print("Validating email adress...")
time.sleep(3)

user_name_email(user_name, email)