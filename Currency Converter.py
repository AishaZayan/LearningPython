import time
import os

dollar = print("""
  ||====================================================================||
  ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
  ||(100)==================|OCTUCODE RESERVE NOTE |================(100)||
  ||\\$//        ~         '------========--------'                \\$//||
  ||<< /        /$\              // ____ \\                         \ >>||
  ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
  ||<<|        \\ //           || <||  >\  ||                        |>>||
  ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)===================|OCTUCUDE RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
""")

exchage_rates = {
  "" : dollar,
  "USD" : 1.0,
  "EUR" : 0.85,
  "EGP" : 30.9,
  "RMB" : 6.5,
}

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')


def display_rates():
  print("Welcome to 'Currency Converter'!\n")
  for currency in exchage_rates:
    print(f"\n{currency} : {exchage_rates[currency]} ")


def currency_converter():
  clear()
  display_rates()

  from_currency = input("\nChoose a currency to convert from: ").upper()
  while True:
    amount = float(input("Enter the amount: "))
    confirmation = input(f"\nYou enterd {amount} {from_currency}. Confirm? (Y/N): ").upper()
    if confirmation =="Y":
      break

  clear()
  display_rates()
  to_currency = input("\nChoose a currency to convert to: ").upper()
  print("Analayzing you request...Please wait...")
  time.sleep(2)
  print(f"Checking for {to_currency} bestrates avaliable...Please wait.")
  time.sleep(3)
  print(f"Getting a discount priece for {from_currency}...Please wait.")
  time.sleep(3)


  if from_currency not in exchage_rates or to_currency not in exchage_rates:
    print("Invalide currency...Conversion canceled.")
    time.sleep(2)
    display_rates()

  new_rate = exchage_rates[to_currency] / exchage_rates[from_currency]
  converted_amount = amount * new_rate

  clear()
  print(f"Preparing the deal from {from_currency} to {to_currency}... Please wait!")
  time.sleep(2)
  print(f"Exchange rate: 1 {from_currency} = {new_rate} {to_currency} \n \n")
  time.sleep(2)
  print(f"{amount} {from_currency} is equal to {round(converted_amount)} {to_currency}")
  time.sleep(1)

  accept_transaction = input("Do you accept this transaction? (Y/N): ").lower()
  if accept_transaction == "y":
    print("Transaction succesfull!")
  else:
    print("Transaction canceled!")
    
  another_conversion = input("Do you want to start a new conversion? (Y/N): ").lower()
  if another_conversion == "y":
    currency_converter()
  else:
    print("Tanks for using 'Currency Converter'")

currency_converter()

