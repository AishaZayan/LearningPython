Str_length = input ("please type Lenght: \n")
Str_width = input ("please type Width: \n")

Length = float (Str_length)
Width = float (Str_width)

Str_meter = input ("How much for 1 meter? \n")
Meter = float (Str_meter)

Area = Length * Width
Cost = Area * Meter

Str_Area = str (Area)
Str_cost = str (Cost)

print("the total area is: " + Str_Area)
print("Give the guy : " + "$"+ Str_cost)
