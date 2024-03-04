print("**** Welcome to ishop calculator ****\n")
number_of_items = int(input("How many items are there in your basket today? \n"))
names = []
prices = []
if number_of_items > 0:
  print("\nLet's get to counting them ....")
  for i in range(1,number_of_items+1):
    name_of_item = input(f"Please tell me the name of the item number {i} ")
    names.append(name_of_item)
    price_of_item = float(input(f"What's the price of {name_of_item} \n$"))
    prices.append(price_of_item)
  see_items = input("Would you like to see your entire basket items? ").lower()
  if see_items == "yes":
    print(names)
    see_price = input("Would you like to see how much it'll cost? ").lower()
    if see_price == "yes":
      print("\nBuying these items will cost:")
      print(sum(prices))
    else:
      input("Press Enter to exit .....")
  else:
    input("Press Enter to exit .....")
else:
  print("Seems like you are not in the mood for shopping today")
input("Press Enter to exit .....")
