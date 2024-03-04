print("""
☠️
""")
print("welcome to my island!")
print("There are two doors in front of you.a 🚪 red door and a 🚪 blue door")
Choice_one = input("Which door do you want to open?").lower()

#التحقق من اختيارات المستخدم
if Choice_one =="red":
  print("Great! know you entered a room.")
  print("You found three boxes: 🎁 white, 🎁 black, and 🎁 green")
  Choice_two = input("Which box do you open?").lower()
  if Choice_two == "white":
    print("You opend a box filled with snakes  🐍🐍🐍")
  elif Choice_two == "black":
    print("You opened a box filled with spiders 🕷️🕷️🕷️")
  elif Choice_two == "green":
    print("Congratulations! You found the treasure 💰💰💰")
  else:
    print("Invalid  choice! 🤷🚫🤷🚫🤷🚫")
elif Choice_one == "blue":
  print("You opend the crocodile door 🐊🐊🐊")
  print("Game over.")
else:
  print("Invalid  choice! 🤷🚫🤷🚫🤷🚫")