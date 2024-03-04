import random
pin_code = random.randint(100,999)

user_input = int(input("Enter (10,9) PIN code:"))
while user_input != pin_code:
  if user_input > pin_code:
    print("Your guess is larger than my number")
  else:
    print("Your guess is lower than my number")
    user_input= int(input("Enter anthor number")) 
print("You won")