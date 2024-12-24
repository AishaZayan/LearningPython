class Reciep:
  def __init__(self, name, ingeridients, cooking_time, instructions):
    self.name = name
    self.ingeridients = ingeridients
    self.cooking_time = cooking_time
    self.instructions = instructions

  def display_reciep(self):
    print("Displaying Reciep...")
    print(f"Name: {self.name}")
    print(f"Ingeridients: {self.ingeridients}")
    print(f"Cooking time: {self.cooking_time}")
    print(f"Instructions: {self.instructions}")

def creat_receip():
  
  name = input("Enter reciep name: ")
  ingeridients = input("Enter ingerdients (comma_seprated): ")
  cooking_time = input("Enter cooking time: ")
  instructions = input("Enter the cooking instructions: ")
  print("Reciep added successfully! \n")
    
  return Reciep(name, ingeridients, cooking_time, instructions)

print("Welcome to the Reciep Collection... \n")

reciep1 = creat_receip()
reciep1.display_reciep()