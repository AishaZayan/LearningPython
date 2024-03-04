names = input("Enter the first and last name of your friends separated by a comma: ").split(", ")
Abbreviated_names = []

for i in names:
  name_parts = i.split()
  print(name_parts)
  first_name = name_parts[0]
  last_name = name_parts[1]
  first_letter = first_name[0]
  last_letter = last_name[0]
  cute = first_letter + "." + last_letter + "."
  Abbreviated_names.append(cute)

print("Abbreviated names:")
for w in Abbreviated_names:
 print(w)
