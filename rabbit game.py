print("Welcome to place the rabbit")
field = ['🌿' , '🌿' , '🌿']
field2 = ['🌿' , '🌿' , '🌿']
field3 = ['🌿' , '🌿' , '🌿'] 

print(field)
print(field2)
print(field3)

allowed_places = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]

print("Where should the rabbit go? 🐇")
Number = input("Please choose a row and a column ")

if Number in allowed_places:
    if Number == "11":
        field[0] = "🐇"
    elif Number == "12":
        field[1] = "🐇"
    elif Number == "13":
        field[2] = "🐇"
    elif Number == "21":
        field2[0] = "🐇"
    elif Number == "22":
        field2[1] = "🐇"
    elif Number == "23":
        field2[2] = "🐇"
    elif Number == "31":
        field3[0] = "🐇"
    elif Number == "32":
        field3[1] = "🐇"
    elif Number == "33":
        field3[2] = "🐇"
        
    print("Success")
    print(field)
    print(field2)
    print(field3)
else:
  print("Sorry! Please follow the instructions")