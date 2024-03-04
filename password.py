import random
import string

print("Welcome to the Password Generator! ")

#هسأله عن عدد الرموز والأحرف والأرقام اللي عايزها
total_number_of_characters = int(input("Enter the total number of characters in thr password: "))

#استفسار العدد
number_of_letters = int(input("Enter the number of letters in the password: "))
number_of_numbers = int(input("Enter the number of numbers in the password: "))
number_of_symbols = int(input("Enter the number of symbols in the password: "))

#جمع أعدادهم
num_of_characters = number_of_letters + number_of_numbers + number_of_symbols
if num_of_characters != total_number_of_characters:
  print("Invalid input. The sum of letters, numbers, and symbols doesn't match the password")
else:
  #اختيار الأحرف
  letters = random.choices(string.ascii_letters, k=number_of_letters)
  #اختيار الأرقام
  numbers = random.choices(string.digits, k=number_of_numbers)
  #اختيار الرموز
  symbols = random.choices(string.punctuation, k=number_of_symbols)
  #جمع الأحرف و الأرقام و الرموز
  all_characters = letters + numbers + symbols
  #ترتيب الأحرف و الرموز والأرقام
  random.shuffle(all_characters)
  password = "".join(all_characters)
  print(f"Generated password: {password}")
  