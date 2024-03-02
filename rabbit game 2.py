print("Welcome to place the rabbit")

field = [ 
    ['🌿' , '🌿' , '🌿'], 
    ['🌿' , '🌿' , '🌿'], 
    ['🌿' , '🌿' , '🌿'] 
]

print (f"{field[0]} \n{field[1]} \n{field[2]}")
print("Where should the rabbit go? 🐇")

position = input("Please, choose a row & a column (e.g., 13): ") #21

row = int(position[0]) - 1 #2
column = int(position[1]) - 1 #1

field[row][column] = "🐇"

print("Success .....")

print (f"{field[0]} \n{field[1]} \n{field[2]}")



############################################################################

print("Welcome to the Rabbit's Place")

# Initialize the field
field = [
    ['🌿', '🌿', '🌿', '🌿'],
    ['🌿', '🌿', '🌿', '🌿'],
    ['🌿', '🌿', '🌿', '🌿'],
    ['🌿', '🌿', '🌿', '🌿'],
    ['🌿', '🌿', '🌿', '🌿'],
    ['🌿', '🌿', '🌿', '🌿'],
    ['🌿', '🌿', '🌿', '🌿'],
    ['🌿', '🌿', '🌿', '🌿']
]

# Display the initial field
for row in field:
    print(' '.join(row))
    
print("Where should the rabbit go? 🐇")

# Get user input for the position
position = input("Please, choose a row & a column (e.g., 13): ")

# Extract row and column from the user input
row = int(position[0]) - 1
column = int(position[1]) - 1

# Update the field with the rabbit's position
field[row][column] = '🐇'

print("Success! The rabbit has been placed.")

# Display the updated field
for row in field:
    print(' '.join(row))
