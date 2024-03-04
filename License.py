age = int(input ("Please Enter Your Age:"))
License = input ("Do you have a License? (yes/no):")
if age >= 18 and License.lower() == "yes":
  print("you can drive")
elif age < 18 or License.lower() == "no":
  print ("Sorry you can't drive")
else:
  print(f"Sorry, your antery of[{License}] is not understood")