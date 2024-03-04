int_secondes =  int(input ("Enter the duration in secondes: \n"))
hours = int_secondes // 3600
minutes = (int_secondes % 3600) // 60
secondes = int_secondes % 60
print (f"The duraction is: {hours} hours, {minutes} minutes, {secondes} secondes.")