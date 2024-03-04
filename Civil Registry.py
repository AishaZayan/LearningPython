is_egyptian = input ("Are you Egyptin? Type 'yes' or 'No':").lower()

if is_egyptian == "yes":
  print ("That's great. That's the first step")
  is_18 = input ("are you above 18 ? Type 'yes' or 'No':").lower()
 
  if is_18 == "yes":
    print("You can have an ID")
  else:
    print("Sorry, You have to be 18 or older")
    print("Try again when you are 18")

else:
  print("Sorry, an Egyptian ID is only for Egyptians")