print("Welcome to 'Whose wallet?'")
print("You will give me a list of names, and I will pick a person to pay")
names_str = input("If your ready, enter the names separated by a comma").lower()
names = names_str.split(", ")
import random
length = len(names) -1
random_number = random.randint(0,length)
random_person = names[random_number]
print(f"Please ask '{random_person}' to take his wallet out. Dinner is on him")