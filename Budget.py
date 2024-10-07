import os 
def clear():
  os.system("cls") if os.name == "nt" else os.system("clear")

def sum(budget, num, per):
  return budget - (num * per)

while True:
  budget = int(input("Enter your spending budget: "))
  item = input("Enter the item you want to buy: ")
  num = int(input(f"How many {item}s do you want to buy? "))
  per = int(input(f"Enter the price per {item}: "))
  total = sum(budget, num, per)
  if total >= 0:
    print("Purchase successful! Enjoy your new item.")
    user_chioce = input("Do you want to continue? (y/n): ").lower()
    if user_chioce == "y":
      clear()
      continue
    else:
      break
  else:
    print("Warning: your purchase exceeds your daily budget!")
    user_chioce = input("Do you want to continue? (y/n): ").lower()
    if user_chioce == "y":
      clear()
      continue
    else:
      break